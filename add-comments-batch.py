#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量添加评论系统脚本
为所有文章添加 showComments: true 参数
"""

import os
import re
import glob
import sys
from pathlib import Path

def add_comments_to_file(file_path):
    """
    为单个文件添加评论系统配置
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经有showComments参数
        if 'showComments:' in content:
            print(f"已包含评论配置: {file_path}")
            return False
        
        # 匹配front matter部分
        front_matter_pattern = r'^---\n(.*?)\n---'
        match = re.search(front_matter_pattern, content, re.DOTALL)
        
        if not match:
            print(f"未找到front matter: {file_path}")
            return False
        
        front_matter_content = match.group(1)
        
        # 在draft参数后添加showComments
        if 'draft:' in front_matter_content:
            # 在draft行后添加showComments
            new_front_matter = re.sub(
                r'(draft:\s*(?:true|false))',
                r'\1\nshowComments: true',
                front_matter_content
            )
        else:
            # 如果没有draft参数，在最后添加
            new_front_matter = front_matter_content.rstrip() + '\nshowComments: true'
        
        # 替换原内容
        new_content = content.replace(match.group(0), f"---\n{new_front_matter}\n---")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"已添加评论配置: {file_path}")
        return True
        
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")
        return False

def batch_add_comments(directory_path, pattern="*.md", recursive=False):
    """
    批量添加评论系统配置
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
    
    print(f"找到 {len(files)} 个文件，开始添加评论配置...")
    print("-" * 50)
    
    updated_count = 0
    for file_path in files:
        if add_comments_to_file(file_path):
            updated_count += 1
    
    print("-" * 50)
    print(f"处理完成！共处理 {len(files)} 个文件，成功更新 {updated_count} 个文件")

def preview_changes(directory_path, pattern="*.md", recursive=False):
    """
    预览将要添加的评论配置
    """
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
    
    need_update_count = 0
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'showComments:' not in content:
                print(f"需要添加评论配置: {file_path}")
                need_update_count += 1
            else:
                print(f"已有评论配置: {file_path}")
        except Exception as e:
            print(f"预览文件 {file_path} 时出错: {e}")
    
    print("-" * 50)
    print(f"预览完成！共 {len(files)} 个文件，需要更新 {need_update_count} 个文件")

def main():
    if len(sys.argv) < 2:
        print("批量添加评论系统脚本")
        print("使用方法:")
        print("  python add-comments-batch.py <目录路径> [选项]")
        print("")
        print("选项:")
        print("  --recursive, -r     递归搜索子目录")
        print("  --preview, -p       仅预览，不实际修改文件")
        print("  --pattern <模式>     文件匹配模式 (默认: *.md)")
        print("")
        print("示例:")
        print("  python add-comments-batch.py content/posts")
        print("  python add-comments-batch.py content/posts --recursive")
        print("  python add-comments-batch.py . --preview")
        print("")
        print("功能:")
        print("  为所有文章的front matter添加 showComments: true 参数")
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
        preview_changes(directory_path, pattern, recursive)
    else:
        batch_add_comments(directory_path, pattern, recursive)

if __name__ == "__main__":
    main()
