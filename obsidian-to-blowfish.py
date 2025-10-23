#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Obsidian到Blowfish格式转换脚本
将Obsidian的YAML列表格式转换为Blowfish主题需要的JSON数组格式
"""

import re
import os
import sys
import glob
from pathlib import Path

def convert_yaml_lists_to_json(content):
    """
    将YAML列表格式转换为JSON数组格式
    处理 Categories 和 tags 字段
    """
    # 匹配Categories字段（不区分大小写）
    categories_pattern = r'(?i)categories:\s*\n((?:\s*-\s*[^\n]+\n?)+)'
    
    def replace_categories(match):
        categories_block = match.group(1)
        # 提取所有列表项
        items = re.findall(r'-\s*([^\n]+)', categories_block)
        # 转换为JSON数组格式
        json_items = [f'"{item.strip()}"' for item in items]
        json_str = '[' + ','.join(json_items) + ']'
        return f'categories: {json_str}\n'
    
    # 匹配tags字段（不区分大小写）
    tags_pattern = r'(?i)tags:\s*\n((?:\s*-\s*[^\n]+\n?)+)'
    
    def replace_tags(match):
        tags_block = match.group(1)
        # 提取所有列表项
        items = re.findall(r'-\s*([^\n]+)', tags_block)
        # 转换为JSON数组格式
        json_items = [f'"{item.strip()}"' for item in items]
        json_str = '[' + ','.join(json_items) + ']'
        return f'tags: {json_str}\n'
    
    # 执行替换
    new_content = re.sub(categories_pattern, replace_categories, content)
    new_content = re.sub(tags_pattern, replace_tags, new_content)
    
    return new_content

def process_file(file_path):
    """
    处理单个文件
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        converted_content = convert_yaml_lists_to_json(content)
        
        if converted_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(converted_content)
            print(f"已转换: {file_path}")
            return True
        else:
            print(f"无需转换: {file_path}")
            return False
            
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")
        return False

def batch_convert(directory_path, pattern="*.md", recursive=False):
    """
    批量转换目录中的所有Markdown文件
    """
    if not os.path.exists(directory_path):
        print(f"目录不存在: {directory_path}")
        return
    
    # 查找所有Markdown文件
    if recursive:
        search_pattern = os.path.join(directory_path, "**", pattern)
        files = glob.glob(search_pattern, recursive=True)
    else:
        search_pattern = os.path.join(directory_path, pattern)
        files = glob.glob(search_pattern)
    
    if not files:
        print(f"在目录 {directory_path} 中没有找到匹配 {pattern} 的文件")
        return
    
    print(f"找到 {len(files)} 个文件，开始转换...")
    print("-" * 50)
    
    converted_count = 0
    for file_path in files:
        if process_file(file_path):
            converted_count += 1
    
    print("-" * 50)
    print(f"转换完成！共处理 {len(files)} 个文件，成功转换 {converted_count} 个文件")

def preview_changes(file_path):
    """
    预览文件变化
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        converted_content = convert_yaml_lists_to_json(original_content)
        
        if converted_content != original_content:
            print(f"\n文件: {file_path}")
            print("变化预览:")
            print("-" * 40)
            
            # 显示变化的部分
            original_lines = original_content.split('\n')
            converted_lines = converted_content.split('\n')
            
            for i, (orig, conv) in enumerate(zip(original_lines, converted_lines)):
                if orig != conv:
                    print(f"第{i+1}行:")
                    print(f"  原: {orig}")
                    print(f"  新: {conv}")
            print("-" * 40)
            return True
        else:
            print(f"无需转换: {file_path}")
            return False
            
    except Exception as e:
        print(f"预览文件 {file_path} 时出错: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Obsidian到Blowfish格式转换脚本")
        print("使用方法:")
        print("  python obsidian-to-blowfish.py <目录路径> [选项]")
        print("")
        print("选项:")
        print("  --recursive, -r     递归搜索子目录")
        print("  --preview, -p       仅预览，不实际转换")
        print("  --pattern <模式>     文件匹配模式 (默认: *.md)")
        print("")
        print("示例:")
        print("  python obsidian-to-blowfish.py content/posts")
        print("  python obsidian-to-blowfish.py content/posts --recursive")
        print("  python obsidian-to-blowfish.py . --preview")
        print("")
        print("转换内容:")
        print("  Categories: -> categories: [JSON数组]")
        print("  tags: -> tags: [JSON数组]")
        return
    
    directory_path = sys.argv[1]
    pattern = "*.md"
    recursive = False
    preview_only = False
    
    # 解析命令行参数
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg in ["--recursive", "-r"]:
            recursive = True
        elif arg in ["--preview", "-p"]:
            preview_only = True
        elif arg == "--pattern" and i + 1 < len(sys.argv):
            pattern = sys.argv[i + 1]
            i += 1
        i += 1
    
    if preview_only:
        # 预览模式
        if not os.path.exists(directory_path):
            print(f"目录不存在: {directory_path}")
            return
        
        if recursive:
            search_pattern = os.path.join(directory_path, "**", pattern)
            files = glob.glob(search_pattern, recursive=True)
        else:
            search_pattern = os.path.join(directory_path, pattern)
            files = glob.glob(search_pattern)
        
        if not files:
            print(f"在目录 {directory_path} 中没有找到匹配 {pattern} 的文件")
            return
        
        print(f"预览模式 - 找到 {len(files)} 个文件")
        print("-" * 50)
        
        converted_count = 0
        for file_path in files:
            if preview_changes(file_path):
                converted_count += 1
        
        print("-" * 50)
        print(f"预览完成！共 {len(files)} 个文件，需要转换 {converted_count} 个文件")
    else:
        batch_convert(directory_path, pattern, recursive)

if __name__ == "__main__":
    main()
