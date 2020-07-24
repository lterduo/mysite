import datetime
from bs4 import BeautifulSoup
import requests
import re
from pdf_save import pdf_save
from crawler_content import *
import codecs

import time

# 进主页面，判断是符合要求的版面，再取出版块url调用get_info


def get_info_main(url, headers):
    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'  # 解决乱码问题
    soup = BeautifulSoup(web_data.text, 'lxml')
    banmian = soup.select('div[class="hidenPage"] a ')

    # 选择理论版块，提取url
    for i in banmian:
        if '理论周刊' in i.text :
            print('banmian:    ' + i.text)
            url_temp = i.get('href')
            # http://bjrb.bjd.com.cn/html/2019-01/07/node_105.htm
            url_temp = re.findall('.*\d\d\d\d-\d\d/\d\d/', url)[0] + url_temp
            print('版面URL：   ', url_temp)
            get_info(url_temp, headers, '')

def get_info(url, headers, pdf):
    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'  # 解决乱码问题
    soup = BeautifulSoup(web_data.text, 'lxml')
    url_content = soup.select('.main-list > ul > li a ')
    for i in url_content:
        #  http://bjrb.bjd.com.cn/html/2019-01/07/node_1.htm
        #  http://bjrb.bjd.com.cn/html/2019-01/07/content_571500.htm
        url_content_temp = i.get('href')
        url_content_temp = re.findall('.*\d\d/\d\d/', url)[0] + url_content_temp
        print('url_content:             ' + url_content_temp)

        pdf = soup.select('#downpdfLink > a')[0]
        pdf = pdf.get('href')
        pdf = 'http://bjrb.bjd.com.cn/' + re.findall('images.*', pdf)[0]
        # http://bjrb.bjd.com.cn/html/2019-01/07/node_1.htm
        # http://bjrb.bjd.com.cn/images/2019-01/07/13/13.pdf
        # ../../../images/2019-01/07/13/13.pdf
        # time.sleep(1)
        pdf_save(pdf, headers, url_content_temp)
        # time.sleep(1)
        json_save(url_content_temp, headers)


# 按时间获取url
daystart = datetime.datetime.strptime("2019-07-01", "%Y-%m-%d").date()
daystop = datetime.datetime.strptime("2020-06-30", '%Y-%m-%d').date()
urls = []
while daystart <= daystop:
    day = daystart.strftime("%Y-%m/%d")
    # http://bjrb.bjd.com.cn/html/2019-01/07/node_1.htm
    s = 'http://bjrb.bjd.com.cn/html/'+day+'/node_1.htm'
    urls.append(s)
    daystart = daystart + datetime.timedelta(days=1)
# print(urls)
headers = {
    'User-Agent': 'Windows Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
}
for url in urls:
    get_info_main(url, headers)
#     # time.sleep(1)
# cd D:\mysite\skl\crawler\bjrb

#  python .\crawler_bjrb.py

