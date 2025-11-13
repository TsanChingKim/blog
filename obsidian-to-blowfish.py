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

CALLOUT_TYPE_MAP = {
    "note": "note",
    "info": "info",
    "todo": "note",
    "tip": "tip",
    "hint": "tip",
    "important": "info",
    "abstract": "note",
    "summary": "note",
    "tldr": "note",
    "success": "success",
    "check": "success",
    "done": "success",
    "question": "info",
    "help": "info",
    "faq": "info",
    "warning": "warning",
    "caution": "warning",
    "attention": "warning",
    "failure": "danger",
    "fail": "danger",
    "missing": "danger",
    "danger": "danger",
    "error": "danger",
    "bug": "danger",
    "example": "note",
    "quote": "",
}

def convert_mermaid_syntax(content):
    """
    将Obsidian的Mermaid语法转换为Blowfish的Mermaid简码语法
    Obsidian: ```mermaid ... ```
    Blowfish: {{< mermaid >}} ... {{< /mermaid >}}
    """
    # 匹配Obsidian的mermaid代码块
    mermaid_pattern = r'```mermaid\s*\n(.*?)\n```'
    
    def replace_mermaid(match):
        mermaid_content = match.group(1)
        # 转换为Blowfish的mermaid简码
        return '{{< mermaid >}}\n' + mermaid_content + '\n{{< /mermaid >}}'
    
    # 执行替换
    new_content = re.sub(mermaid_pattern, replace_mermaid, content, flags=re.DOTALL)
    
    return new_content


def convert_callouts(content):
    """
    将Obsidian的Callout语法转换为Blowfish的alert短代码
    """
    lines = content.splitlines()
    converted_lines = []
    total_lines = len(lines)
    i = 0

    def strip_callout_prefix(text):
        return re.sub(r'^\s{0,3}>\s?', '', text)

    while i < total_lines:
        line = lines[i]
        match = re.match(
            r'^\s{0,3}>\s*\[!(?P<type>[^\]\s]+)\]\s*(?P<modifier>[+-])?\s*(?P<title>.*)$',
            line,
            flags=re.IGNORECASE,
        )

        if match:
            callout_type = match.group("type").strip()
            title = match.group("title").strip()
            style_key = CALLOUT_TYPE_MAP.get(callout_type.lower(), callout_type.lower())

            callout_body = []
            if title:
                callout_body.append(title)

            i += 1
            while i < total_lines:
                next_line = lines[i]
                if re.match(r'^\s{0,3}>\s?', next_line):
                    callout_body.append(strip_callout_prefix(next_line))
                    i += 1
                else:
                    break

            while callout_body and callout_body[-1].strip() == "":
                callout_body.pop()

            params = []
            if style_key:
                params.append(f'"{style_key}"')

            effective_title = title if title else callout_type.capitalize()
            if effective_title:
                params.append(f'title="{effective_title}"')

            opening = "{{< alert"
            if params:
                opening += " " + " ".join(params)
            opening += " >}}"

            converted_lines.append(opening)
            converted_lines.extend(callout_body)
            converted_lines.append("{{< /alert >}}")
            converted_lines.append("")
        else:
            converted_lines.append(line)
            i += 1

    result = "\n".join(converted_lines)
    if content.endswith("\n") and not result.endswith("\n"):
        result += "\n"
    return result


def convert_latex_to_katex(content):
    """
    将Obsidian的LaTeX语法转换为Blowfish的KaTeX语法
    Obsidian行内公式: $...$ -> KaTeX行内公式: \(...\)
    Obsidian块级公式: $$...$$ -> KaTeX块级公式: $$...$$ (保持不变)
    如果检测到数学公式，确保文章包含 {{< katex >}} 短代码
    """
    # 检测是否包含数学公式（排除已经转换过的和代码块中的）
    # 检查是否有未转换的行内公式 $...$ (不是 $$...$$ 的一部分)
    has_inline_math = bool(re.search(r'(?<!\$)\$(?!\$)[^$\n]+\$(?!\$)', content))
    # 检查是否有块级公式 $$...$$
    has_block_math = bool(re.search(r'\$\$[\s\S]*?\$\$', content))
    has_math = has_inline_math or has_block_math
    
    if not has_math:
        return content
    
    # 需要排除代码块中的内容
    def process_non_code_blocks(text):
        """处理非代码块部分的数学公式"""
        parts = []
        last_end = 0
        
        # 找到所有代码块的位置（包括行内代码和代码块）
        code_block_pattern = r'```[\s\S]*?```|`[^`\n]+`'
        code_blocks = list(re.finditer(code_block_pattern, text))
        
        for code_match in code_blocks:
            # 处理代码块之前的内容
            before_code = text[last_end:code_match.start()]
            # 转换行内公式: $...$ -> \(...\)
            # 排除块级公式中的 $，以及已经转换过的 \(...\)
            def replace_inline_math(match):
                math_content = match.group(1)
                # 跳过已经转换过的公式
                if math_content.strip().startswith('\\(') or math_content.strip().startswith('\\['):
                    return match.group(0)
                # 转换为KaTeX行内公式格式
                return r'\(' + math_content + r'\)'
            
            # 匹配行内公式，排除块级公式
            # 使用负向前瞻和回顾来排除 $$...$$ 中的 $
            inline_math_pattern = r'(?<!\$)\$(?!\$)([^$\n]+?)\$(?!\$)'
            before_code = re.sub(inline_math_pattern, replace_inline_math, before_code)
            parts.append(before_code)
            
            # 保持代码块不变
            parts.append(code_match.group(0))
            last_end = code_match.end()
        
        # 处理最后一部分
        remaining = text[last_end:]
        def replace_inline_math(match):
            math_content = match.group(1)
            if math_content.strip().startswith('\\(') or math_content.strip().startswith('\\['):
                return match.group(0)
            return r'\(' + math_content + r'\)'
        inline_math_pattern = r'(?<!\$)\$(?!\$)([^$\n]+?)\$(?!\$)'
        remaining = re.sub(inline_math_pattern, replace_inline_math, remaining)
        parts.append(remaining)
        
        return ''.join(parts)
    
    new_content = process_non_code_blocks(content)
    
    # 检查是否已包含 katex 短代码
    has_katex_shortcode = bool(re.search(r'\{\{<\s*katex\s*>', new_content, re.IGNORECASE))
    
    # 如果没有 katex 短代码，在 front matter 后添加
    if not has_katex_shortcode:
        # 查找 front matter 结束位置
        front_matter_match = re.search(r'^---\n[\s\S]*?\n---\n?', new_content, re.MULTILINE)
        if front_matter_match:
            # 在 front matter 后添加 katex 短代码
            insert_pos = front_matter_match.end()
            # 检查是否已经有 <!--more--> 标记（在接下来的200个字符内查找）
            more_tag_match = re.search(r'<!--more-->', new_content[insert_pos:insert_pos+200])
            if more_tag_match:
                # 在 <!--more--> 后添加
                insert_pos = insert_pos + more_tag_match.end()
                new_content = (new_content[:insert_pos] + 
                             '\n\n{{< katex >}}\n\n' + 
                             new_content[insert_pos:])
            else:
                # 直接在 front matter 后添加
                new_content = (new_content[:insert_pos] + 
                             '\n{{< katex >}}\n\n' + 
                             new_content[insert_pos:])
    
    return new_content

def convert_yaml_lists_to_json(content):
    """
    将YAML列表格式转换为JSON数组格式
    处理 Categories 和 tags 字段
    """
    # 仅在 Front Matter（--- ... ---）内进行转换，避免将正文中的 "-" 或分隔线误判为列表项
    front_matter_match = re.search(r'^---\n([\s\S]*?)\n---', content, flags=re.MULTILINE)
    if not front_matter_match:
        return content

    front_matter = front_matter_match.group(1)

    # 匹配 Categories 字段（不区分大小写），要求 "- " 后至少有一个空格，防止将 "---" 误判
    categories_pattern = r'(?im)^(categories:)\s*\n((?:\s*-\s+[^\n]+\n?)+)'

    def replace_categories(match):
        key = match.group(1)
        categories_block = match.group(2)
        items = re.findall(r'-\s+([^\n]+)', categories_block)
        json_items = [f'"{item.strip()}"' for item in items]
        json_str = '[' + ','.join(json_items) + ']'
        return f'{key} {json_str}\n'

    # 匹配 tags 字段（不区分大小写），同样要求 "- " 后至少一个空格
    tags_list_pattern = r'(?im)^(tags:)\s*\n((?:\s*-\s+[^\n]+\n?)+)'

    def replace_tags_list(match):
        key = match.group(1)
        tags_block = match.group(2)
        items = re.findall(r'-\s+([^\n]+)', tags_block)
        json_items = [f'"{item.strip()}"' for item in items]
        json_str = '[' + ','.join(json_items) + ']'
        return f'{key} {json_str}\n'

    # 处理 Front Matter 内的转换
    converted = re.sub(categories_pattern, replace_categories, front_matter)
    converted = re.sub(tags_list_pattern, replace_tags_list, converted)

    # 若存在独立的 "tags:" 但其下没有列表，统一为空数组
    converted = re.sub(r'(?im)^(tags:)\s*(\n(?!(\s*-\s+)))', r'\1 []\n', converted)

    # 将转换后的 Front Matter 写回原文
    start, end = front_matter_match.span(1)
    new_content = content[:start] + converted + content[end:]

    return new_content

def process_file(file_path):
    """
    处理单个文件
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        content = original_content
        modified = False

        # 先转换Mermaid语法
        new_content = convert_mermaid_syntax(content)
        if new_content != content:
            modified = True
            content = new_content

        # 转换Callout为 alert 简码
        new_content = convert_callouts(content)
        if new_content != content:
            modified = True
            content = new_content

        # 转换LaTeX到KaTeX
        new_content = convert_latex_to_katex(content)
        if new_content != content:
            modified = True
            content = new_content
        
        # 再转换YAML列表格式
        new_content = convert_yaml_lists_to_json(content)
        if new_content != content:
            modified = True
            content = new_content

        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
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
        
        # 先转换Mermaid语法
        mermaid_converted = convert_mermaid_syntax(original_content)

        # 转换Callout为 alert
        callout_converted = convert_callouts(mermaid_converted)
        
        # 转换LaTeX到KaTeX
        latex_converted = convert_latex_to_katex(callout_converted)
        
        # 再转换YAML列表格式
        converted_content = convert_yaml_lists_to_json(latex_converted)
        
        if converted_content != original_content:
            print(f"\n文件: {file_path}")
            print("变化预览:")
            print("-" * 40)
            
            # 检查Mermaid转换
            if mermaid_converted != original_content:
                print("Mermaid语法转换:")
                mermaid_matches = re.findall(r'```mermaid\s*\n(.*?)\n```', original_content, re.DOTALL)
                for i, match in enumerate(mermaid_matches):
                    print(f"  发现Mermaid代码块 {i+1}:")
                    print(f"    原: ```mermaid\n{match[:100]}...```")
                    print(f"    新: {{< mermaid >}}\n{match[:100]}...{{< /mermaid >}}")
                print()
            
            # 检查Callout转换
            if callout_converted != mermaid_converted:
                print("Callout 转换:")
                callout_matches = re.findall(
                    r'^\s{0,3}>\s*\[!(?P<type>[^\]\s]+)\].*$',
                    original_content,
                    flags=re.MULTILINE,
                )
                for idx, c_type in enumerate(callout_matches, start=1):
                    print(f"  发现Callout {idx}: {c_type}")
                print()
            
            # 检查LaTeX转换
            if latex_converted != callout_converted:
                print("LaTeX到KaTeX转换:")
                # 查找行内公式
                inline_matches = re.findall(r'(?<!\$)\$(?!\$)[^$\n]+\$(?!\$)', original_content)
                if inline_matches:
                    print(f"  发现行内公式 {len(inline_matches)} 个:")
                    for i, match in enumerate(inline_matches[:5]):  # 只显示前5个
                        print(f"    {i+1}: ${match} -> \\({match}\\)")
                    if len(inline_matches) > 5:
                        print(f"    ... 还有 {len(inline_matches) - 5} 个")
                
                # 查找块级公式
                block_matches = re.findall(r'\$\$[\s\S]*?\$\$', original_content)
                if block_matches:
                    print(f"  发现块级公式 {len(block_matches)} 个 (保持不变)")
                
                # 检查是否添加了 katex 短代码
                if re.search(r'\{\{<\s*katex\s*>', latex_converted, re.IGNORECASE):
                    if not re.search(r'\{\{<\s*katex\s*>', original_content, re.IGNORECASE):
                        print("  已添加 {{< katex >}} 短代码")
                print()
            
            # 检查YAML转换
            if converted_content != latex_converted:
                print("YAML列表转换:")
                # 显示变化的部分
                original_lines = callout_converted.split('\n')
                converted_lines = converted_content.split('\n')
                
                for i, (orig, conv) in enumerate(zip(original_lines, converted_lines)):
                    if orig != conv:
                        print(f"  第{i+1}行:")
                        print(f"    原: {orig}")
                        print(f"    新: {conv}")
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
        print("  Mermaid语法: ```mermaid ... ``` -> {{< mermaid >}} ... {{< /mermaid >}}")
        print("  Callout: > [!TYPE] ... -> {{< alert \"type\" title=\"...\" >}} ... {{< /alert >}}")
        print("  LaTeX公式: $...$ -> \\(...\\) (行内), $$...$$ -> $$...$$ (块级)")
        print("  自动添加 {{< katex >}} 短代码（如果文章包含数学公式）")
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
