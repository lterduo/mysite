import requests
import re

path = './pdf/'


def pdf_save(url, headers, filename):
    data = requests.get(url, headers=headers)
    filename1 = re.findall('gmrb_\d\d\d\d\d\d\d\d_\d-\d\d', filename)
    if filename1:
        filename1 = filename1[0]
    else:
        filename1 = re.findall('gmrb_\d\d\d\d\d\d\d\d_\d\d-\d\d', filename)[0]
#      http://epaper.gmw.cn/gmrb/html/2018-01/11/nw.D110000gmrb_20180111_10-05.htm
#      http://epaper.gmw.cn/gmrb/html/2018-01/10/nw.D110000gmrb_20180110_2-11.htm
    filename = path + filename1 + '.pdf'
    if filename:
        fp = open(filename, 'wb')
        fp.write(data.content)
        fp.close()

# url = 'http://paper.people.com.cn/rmrb/page/2018-08/18/07/rmrb2018081807.pdf'
# headers = {
#     'User-Agent': 'Windows Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
# }
# pdf_save(url,headers)
