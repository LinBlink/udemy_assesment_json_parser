import html2text
import re
from mdutils.mdutils import MdUtils
import json
from bs4 import BeautifulSoup

# TODO
def question_convert_to_md( html_content ):
  soup = BeautifulSoup( html_content, "html.parser" )

# convert explanation part to markdown
def explanation_convert_to_md( html_content ):
  # html_content = html_content.replace("<strong>","").replace("</strong>","")
  try:
    html_content = bytes(
      html_content,
      "utf-8"
    ).decode(
      "unicode_escape"
    )
  except:
    pass

  h = html2text.HTML2Text()
  h.ignore_links = False
  h.bypass_tables = False
  h.mark_code = False
  h.ignore_emphasis = True
  h.single_line_break = True
  h.body_width = 0

  markdown = h.handle(html_content)
  markdown = re.sub(r'^\s*$\n?', '', markdown, flags=re.MULTILINE).strip()
  return markdown

mdFile = MdUtils(
  file_name='Spring认证官方970道真题 PART 1'
)

mdFile.new_header(
  title='Spring认证官方970道真题 PART 1',
  level=1
)

with open('1.json', 'r', encoding='utf-8') as file:
  data = json.load(file)

#  count number of questions

number_of_qs = int( data['count'] )

selection_str = ["(A)", "(B)", "(C)", "(D)"]

h = html2text.HTML2Text()

h.body_width = 0

for i in range(number_of_qs) :
  mdFile.new_header(  title= "Question #" + str(i+1) , level=2 )
  mdFile.new_paragraph( text="Question: " + h.handle( data['results'][i]['prompt']['question']).strip() , bold_italics_code='b'  )
  for j in range(4):
    mdFile.new_paragraph( text= selection_str[j] + " " + h.handle( data['results'][i]['prompt']['answers'][j] ).strip() )
  mdFile.new_paragraph( text="Answer: " + h.handle( data['results'][i]['correct_response'][0]).strip().capitalize() , bold_italics_code='b'  )
  mdFile.new_paragraph( "Explanation", bold_italics_code='b')
  mdFile.new_paragraph( explanation_convert_to_md(
    data['results'][i]['prompt']['explanation']
  )  )
  mdFile.new_line()


# mdFile.new_paragraph(
#   html_convert_to_md(
#     data['results'][0]['prompt']['explanation']
#   )
# )

mdFile.create_md_file()

print("😊DONE")