import requests
import re

path = './pdf/'
def pdf_save(url,headers,filename): #filename��crawler_content��url����Ҫ����
    data = requests.get(url, headers=headers)
    #file_name = re.findall('rmrb\d*.pdf', url)
    filename = re.findall('renmrb_\d\d\d\d\d\d\d\d_\d', filename)[0] #renmrb_20180815_1
    filename = '10' + filename[7:-2] + '0' + filename[-1]  #名称跟json中的number一致
    filename =path + filename + '.pdf'
#     print('filename :        '+filename)
    if filename:
        fp = open(filename, 'wb')
        fp.write(data.content)
        fp.close()

# url = 'http://paper.people.com.cn/rmrb/page/2018-08/18/07/rmrb2018081807.pdf'
# headers = {
#     'User-Agent': 'Windows Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
# }
# pdf_save(url,headers)
