import pdfkit
import os
'''将html文件生成pdf文件'''

from PyPDF2 import PdfFileReader, PdfFileWriter


def html_to_pdf(fileList, pid):

    # 生成PDF
    for html in fileList:
        html = 'toPdf/' + pid + html
        to_file = html[:-5] + '.pdf'
        try:
            if os.path.exists(to_file):
                os.remove(to_file)

            # 将wkhtmltopdf.exe程序绝对路径传入config对象
            path_wkthmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
            config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
            # 生成pdf文件，to_file为文件路径
            # pdfkit.from_file(html, to_file, configuration=config)
            pdfkit.from_url(html, to_file, configuration=config)
            print(html)
        except Exception as e:
            with open('errlog.txt', 'a+') as f:
                f.writelines(str(datetime.now()) + '  html_to_pdf.py')
                f.writelines(str(e))
                f.close()

    pdf_merge(fileList, pid)
    del_files(fileList, pid)


# 合并
def pdf_merge(fileList, pid):

    # output = PdfFileWriter()
    # outputPages = 0

    pdf_writer = PdfFileWriter()

    for pdf_file in fileList:
        pdf_file = 'toPdf/' + pid + pdf_file[:-5] + '.pdf'

        pdf_reader = PdfFileReader(pdf_file)
        for page in range(pdf_reader.getNumPages()):
            # 将每页添加到writer对象
            pdf_writer.addPage(pdf_reader.getPage(page))

    # 写入合并的pdf
    outPutFile = 'toPdf/pdf_temp/' + pid + '.pdf'
    with open(outPutFile, 'wb') as out:
        pdf_writer.write(out)

    print("PDF文件合并完成！")


# 删除临时文件
def del_files(fileList, pid):

    for f in fileList:
        print(f)
        html = 'toPdf/' + pid + f
        pdf = html[:-5] + '.pdf'
        print(html)
        print(pdf)
        if os.path.exists(html):
            os.remove(html)
        if os.path.exists(pdf):
            os.remove(pdf)
