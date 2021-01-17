from docxtpl import DocxTemplate, Document

from html2docx import html2docx

# with open("my.html") as fp:
#     html = fp.read()

# 使用 html2docx 将html转换成doc
html = '''
<h1>大沙发电视</h1><h1>heading</h1><p><em>斜体</em></p><p><strong>加粗</strong></p><p><strong class=\"ql-size-huge\">加大</strong></p>
'''
html = '<html>' + html + '</html>'
buf = html2docx(html, title="My Document")

with open("1.docx", "wb") as fp:
    fp.write(buf.getvalue())
    fp.close()


doc = DocxTemplate('./template.docx')

# 将文档当做子项
sub = doc.new_subdoc()
sub.subdocx = Document('./content.docx')

sub = '我是富文本'

context = {
    'title': 'aaa',
    'leader': {
        'name': '冯颖',
        'organization': '残联',
        'gender': '女'
    },
    'sub': sub
}

doc.render(context)
doc.save('./output.docx')
