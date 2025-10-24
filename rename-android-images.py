#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Android图片文件重命名脚本
将assets/images/android中的图片文件名修改为对应笔记front matter中的featureimage字段
"""

import os
import re
import glob
import shutil
from pathlib import Path

def get_featureimage_mapping():
    """
    获取所有Android文章的featureimage映射
    返回: {文章编号: featureimage文件名}
    """
    android_dir = "content/posts/android"
    mapping = {}
    
    # 获取所有markdown文件
    md_files = glob.glob(os.path.join(android_dir, "*.md"))
    
    for file_path in md_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取文章编号和featureimage
            filename = os.path.basename(file_path)
            # 匹配文件名开头的数字
            match = re.match(r'^(\d+)', filename)
            if match:
                article_num = match.group(1)
                
                # 提取featureimage字段
                featureimage_match = re.search(r'featureimage:\s*images/android/(\d+\.jpg)', content)
                if featureimage_match:
                    expected_filename = featureimage_match.group(1)
                    mapping[article_num] = expected_filename
                    print(f"文章 {article_num}: {filename} -> {expected_filename}")
        
        except Exception as e:
            print(f"处理文件 {file_path} 时出错: {e}")
    
    return mapping

def rename_images():
    """
    重命名图片文件
    """
    images_dir = "assets/images/android"
    
    if not os.path.exists(images_dir):
        print(f"图片目录不存在: {images_dir}")
        return
    
    # 获取featureimage映射
    mapping = get_featureimage_mapping()
    
    if not mapping:
        print("没有找到featureimage映射")
        return
    
    print(f"\n找到 {len(mapping)} 个映射关系")
    print("=" * 50)
    
    # 获取当前所有图片文件
    current_images = {}
    for file_path in glob.glob(os.path.join(images_dir, "*.jpg")):
        filename = os.path.basename(file_path)
        # 尝试从文件名提取编号
        match = re.match(r'^(\d+)', filename)
        if match:
            article_num = match.group(1)
            current_images[article_num] = filename
        else:
            # 如果没有数字开头，尝试从文件名推断
            print(f"警告: 无法从文件名提取编号: {filename}")
    
    print(f"当前图片文件: {list(current_images.keys())}")
    print(f"期望的映射: {list(mapping.keys())}")
    
    # 执行重命名
    renamed_count = 0
    
    for article_num, expected_filename in mapping.items():
        if article_num in current_images:
            current_filename = current_images[article_num]
            
            if current_filename != expected_filename:
                old_path = os.path.join(images_dir, current_filename)
                new_path = os.path.join(images_dir, expected_filename)
                
                try:
                    # 检查目标文件是否已存在
                    if os.path.exists(new_path):
                        print(f"警告: 目标文件已存在 {expected_filename}")
                        continue
                    
                    # 重命名文件
                    shutil.move(old_path, new_path)
                    print(f"成功重命名: {current_filename} -> {expected_filename}")
                    renamed_count += 1
                    
                except Exception as e:
                    print(f"重命名失败 {current_filename}: {e}")
            else:
                print(f"无需重命名: {current_filename}")
        else:
            print(f"未找到文章 {article_num} 对应的图片文件")
    
    print("=" * 50)
    print(f"重命名完成！成功重命名 {renamed_count} 个文件")

def preview_rename():
    """
    预览重命名操作
    """
    images_dir = "assets/images/android"
    
    if not os.path.exists(images_dir):
        print(f"图片目录不存在: {images_dir}")
        return
    
    # 获取featureimage映射
    mapping = get_featureimage_mapping()
    
    if not mapping:
        print("没有找到featureimage映射")
        return
    
    print(f"\n预览重命名操作:")
    print("=" * 50)
    
    # 获取当前所有图片文件
    current_images = {}
    for file_path in glob.glob(os.path.join(images_dir, "*.jpg")):
        filename = os.path.basename(file_path)
        # 尝试从文件名提取编号
        match = re.match(r'^(\d+)', filename)
        if match:
            article_num = match.group(1)
            current_images[article_num] = filename
    
    for article_num, expected_filename in mapping.items():
        if article_num in current_images:
            current_filename = current_images[article_num]
            
            if current_filename != expected_filename:
                print(f"重命名: {current_filename} -> {expected_filename}")
            else:
                print(f"无需重命名: {current_filename}")
        else:
            print(f"警告: 文章 {article_num} 缺少对应的图片文件")

def main():
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--preview":
        preview_rename()
    else:
        print("Android图片文件重命名脚本")
        print("使用方法:")
        print("  python rename-android-images.py          # 执行重命名")
        print("  python rename-android-images.py --preview # 预览重命名")
        print("")
        
        confirm = input("确认执行重命名操作？(y/N): ")
        if confirm.lower() == 'y':
            rename_images()
        else:
            print("操作已取消")

if __name__ == "__main__":
    main()
