import requests
import re

path = './pdf/'


def pdf_save(url, headers, filename):
    data = requests.get(url, headers=headers)
    #      http://bjrb.bjd.com.cn/html/2019-01/07/content_571504.htm
    filename1 = re.findall('\d\d\d\d-\d\d/\d\d.*', filename)
    if filename1:
        filename1 = filename1[0]
        filename1 = re.sub('/', '-', filename1)
        filename1 = re.sub('.htm', '', filename1)
        # print('filename: ', filename1)
#     else:
#         filename1 = re.findall('\d\d\d\d\d\d\d\d_\d\d-\d\d', filename)[0]

    filename = path + 'bjrb_' + filename1 + '.pdf'
    if filename:
        fp = open(filename, 'wb')
        fp.write(data.content)
        fp.close()

# url = 'http://paper.people.com.cn/rmrb/page/2018-08/18/07/rmrb2018081807.pdf'
# headers = {
#     'User-Agent': 'Windows Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
# }
# pdf_save(url,headers)
