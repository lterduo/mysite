from docxtpl import DocxTemplate, Document

doc = DocxTemplate('./template.docx')

# 将文档当做子项
sub = doc.new_subdoc()
sub.subdocx = Document('./sub.docx')

leader = {
    'name': '冯颖',
    'organization': '残联',
    'gender': '女'
}

context = {
    'title': 'aaa',
    'leader': leader,
    'sub': sub
}

# doc.render(context)
doc.render(context)
doc.save('./output.docx')
