import pdfkit
import os
'''将html文件生成pdf文件'''

# 不好用


def html_to_pdf(html, to_file):
    try:
        if os.path.exists(to_file):
            os.remove(to_file)

        # 将wkhtmltopdf.exe程序绝对路径传入config对象
        path_wkthmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        # 生成pdf文件，to_file为文件路径
        pdfkit.from_file(html, to_file, configuration=config)
        print('完成')
    except Exception as e:
        print(e)


html_to_pdf('./01.html', './out_2.pdf')
