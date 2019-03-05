import requests
import re

path = './pdf/'
def pdf_save(url,headers,filename): 
    data = requests.get(url, headers=headers)
    filename = re.findall('\d\d\d\d-\d\d/\d\d/content_\d\d\d\d\d\d', filename)[0]
    filename = 'jjrb_' + re.sub('/', '-', filename)
    filename = path + filename + '.pdf'
    if filename:
        fp = open(filename, 'wb')
        fp.write(data.content)
        fp.close()

# url = ' http://paper.ce.cn/jjrb/page/1/2019-02/20/12/2019022012_pdf.pdf'
# headers = {
#     'User-Agent': 'Windows Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
# }
# pdf_save(url,headers)
