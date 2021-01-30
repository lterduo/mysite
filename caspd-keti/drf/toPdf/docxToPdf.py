import os
from win32com import client


def doc2pdf(doc_name, pdf_name):
    """
    :word文件转pdf
    :param doc_name word文件名称
    :param pdf_name 转换后pdf文件名称
    """
    try:
        word = client.DispatchEx("Word.Application")
        if os.path.exists(pdf_name):
            os.remove(pdf_name)
        worddoc = word.Documents.Open(doc_name, ReadOnly=1)
        print(worddoc)
        worddoc.SaveAs(pdf_name, FileFormat=17)
        worddoc.Close()
        return pdf_name
    except Exception as e:
        print(e)


# 路径必须转义！！！
doc2pdf('D:\\git\\mysite\\caspd-keti\\drf\\toPdf\\sub.docx',
        'D:\\git\\mysite\\caspd-keti\\drf\\toPdf\\output.pdf')
