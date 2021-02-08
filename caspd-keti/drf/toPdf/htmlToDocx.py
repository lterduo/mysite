
from docxtpl import DocxTemplate, Document

from html2docx import html2docx

with open("课题研究计划.html") as fp:
    html = fp.read()
    fp.close()
# 使用 html2docx 将html转换成doc
# html = '''
# '''

buf = html2docx(html, title="My Document")

with open("sub.docx", "wb") as fp:
    fp.write(buf.getvalue())
    fp.close()
