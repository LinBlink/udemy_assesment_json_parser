import html2text
import re
from mdutils.mdutils import MdUtils


# convert explanation part to markdown 
def html_convert_to_md( html_content ):
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

with open("output.md", "w", encoding="utf-8") as f:
  f.write( result )

print("😊DONE")