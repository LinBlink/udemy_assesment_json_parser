import html2text
import re
from mdutils.mdutils import MdUtils
import json
from bs4 import BeautifulSoup
from markdownify import markdownify as mdf

def generateMd( num: int , withAnswer: bool = False, withExp : bool = False ):


  with open(f'{num}.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

  number_of_qs = int( data['count'] )

  mdFile = MdUtils(
    file_name= f"""Spring认证官方970道真题 第{num}部分 共计{number_of_qs}题{"答案" if withAnswer else ""} {"解析" if withExp else ""}"""
  )

  mdFile.new_header(
    title=  f"""Spring认证官方970道真题 第{num}部分 共计{number_of_qs}题{"w答案" if withAnswer else ""} {"解析" if withExp else ""}""",
    level=1
  )

  #  count number of questions


  selection_str = ["(A)", "(B)", "(C)", "(D)","(E)","(F)","(G)","(H)"]

  h = html2text.HTML2Text()

  h.body_width = 0

  for i in range(number_of_qs) :
    mdFile.new_header(  title= "Question #" + str(i+1) , level=2 )

    mdFile.new_header( title="Question", level=3 )

    question_md = mdf( data['results'][i]['prompt']['question']).strip()

    question_md = re.sub(r'\s*```\s*java', r'\n```java\n',question_md)
    question_md = re.sub(r'\s*```\s*json', r'\n```json\n',question_md)
    mdFile.new_paragraph( text="Question: " + question_md )
    
    # ANALYZE ANSWER PART
    for j in range( len(data['results'][i]['prompt']['answers']) ):
      mdFile.new_paragraph( text= "**" + selection_str[j] + "**" + " " + h.handle( data['results'][i]['prompt']['answers'][j] ).strip() )

    if withAnswer:
      mdFile.new_header( title="Answer", level=3 )
      mdFile.new_paragraph( h.handle( data['results'][i]['correct_response'][0]).strip().capitalize() )


    
    try:
      mdFile.new_header( title="Explanation", level=3 )
      explanation_md = mdf(
        data['results'][i]['prompt']['explanation']
      )
      explanation_md = re.sub(r'\s*```\s*java', r'\n```java\n', explanation_md)
      explanation_md = re.sub(r'\s*```\s*json', r'\n```json\n',explanation_md)
      mdFile.new_paragraph( explanation_md  )
    except:
      pass
    
    mdFile.new_line()


  # mdFile.new_paragraph(
  #   html_convert_to_md(
  #     data['results'][0]['prompt']['explanation']
  #   )
  # )

  mdFile.create_md_file()

for i in range(6):
  generateMd(i+1)
  generateMd(i+1 , withAnswer= True)
  generateMd(i+1, withAnswer=True , withExp= True)

print("😊DONE")