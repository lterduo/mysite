from docxtpl import DocxTemplate

tpl = DocxTemplate('./template.docx')

context = {
    'title': 'aaa'
}

tpl.render(context)
tpl.save('./template.docx')
