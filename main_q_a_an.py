import json
from bs4 import BeautifulSoup

import json
import re
from bs4 import BeautifulSoup

def clean_html(html_content):
    """
    将 HTML 标签转换为简洁的 Markdown 格式，并压缩多余换行
    """
    if not html_content:
        return ""
    
    soup = BeautifulSoup(html_content, "html.parser")
    
    # 1. 预处理代码块
    for pre in soup.find_all("pre"):
        code_text = pre.get_text()
        pre.replace_with(f"\n\n```java\n{code_text}\n```\n\n")
    
    # 2. 获取文本 (使用换行符作为分隔)
    text = soup.get_text(separator="\n")
    
    # 3. 核心优化：使用正则表达式清理多余的空白
    # 将 3 个或更多连续换行符替换为 2 个 (即标准 Markdown 段落间距)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # 去除首尾空格
    return text.strip()

def convert_to_md(json_data):
    md_output = "# Spring 认证练习题\n\n"
    results = json_data.get("results", [])
    
    for i, item in enumerate(results, 1):
        prompt = item.get("prompt", {})
        
        # 提取数据
        question = clean_html(prompt.get("question", ""))
        answers = [clean_html(a) for a in prompt.get("answers", [])]
        correct_responses = item.get("correct_response", [])
        explanation = clean_html(prompt.get("explanation", ""))
        section = item.get("section", "未分类")

        # 写入题目
        md_output += f"### {i}. {question}\n\n"
        
        # 写入选项
        md_output += "**选项：**\n"
        for j, ans_text in enumerate(answers):
            letter = chr(65 + j)
            # 选项内部也可能有多余换行，处理一下
            clean_ans = ans_text.replace('\n', ' ') 
            md_output += f"- **{letter}**: {clean_ans}\n"
        
        # 写入答案
        formatted_correct = ", ".join([r.upper() for r in correct_responses])
        md_output += f"\n**正确答案：** `{formatted_correct}`\n\n"

        # 写入解析 (避开 Python 3.10 f-string 反斜杠限制)
        if explanation:
            md_output += "**答案解析：**\n"
            # 将解析内容变为引用格式，同时确保引用符号 > 后面不会有太多空行
            quoted_explanation = explanation.replace("\n", "\n> ")
            md_output += f"> {quoted_explanation}\n\n"
        
        md_output += "---\n\n"
        
    return md_output

# --- 运行部分 (用法同前) ---
# markdown_result = convert_to_md(data)
# --- 运行部分 ---

# 假设你的 JSON 字符串存储在变量 json_str 中
# 如果是从文件读取，请使用：
# with open('data.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)

# 这里仅作演示，请将下面的变量替换为你实际的 JSON 数据
try:
    with open('1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 转换逻辑
    markdown_result = convert_to_md(data) # 这里的 data 对应你的 json 对象
    
    # 写入文件，指定 utf-8 编码防止中文乱码
    with open("Spring_Questions.md", "w", encoding="utf-8") as f:
        f.write(markdown_result)
        
    print("Markdown 文件生成成功：Spring_Questions.md")

except NameError:
    print("提示：请确保你已经定义了包含 JSON 数据的 data 变量。")
except Exception as e:
    print(f"处理过程中出错: {e}")