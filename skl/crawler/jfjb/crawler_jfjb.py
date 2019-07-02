import datetime
from bs4 import BeautifulSoup
import requests
import re
from pdf_save import pdf_save
from crawler_content import *
import codecs

# 进主页面，判断是符合要求的版面，再取出版块url调用get_info

def get_info_main(url, headers):
    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'  # 解决乱码问题
    soup = BeautifulSoup(web_data.text, 'lxml')
    # soup = BeautifulSoup(html,'lxml')
    # banmian = soup.find_all(id='pageLink')
    banmian = soup.select('div[id="nav-section-viewport"] a')

    # 选择理论版块，提取url     有一个隐藏的div，a标签id=pageLink，需要过滤掉
    for i in banmian:
        if '思想战线' in i.text or '学习与研究' in i.text :
            print('banmian:    ' + i.text)
            url_temp = i.get('href')
            url_temp = url[0:-10] + url_temp
            print('版面URL：   ', url_temp)
            get_info(url_temp, headers, '')

def get_info(url, headers, pdf):
    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'  # 解决乱码问题
    soup = BeautifulSoup(web_data.text, 'lxml')
    url_content = soup.select('div[id="newslist-box"] li a ')
    for i in url_content:
        
        #  http://www.81.cn/jfjbmap/content/2019-03/08/node_12.htm
        #  http://www.81.cn/jfjbmap/content/2019-03/01/content_228400.htm
        #                                              content_228910.htm
        url_content_temp = i.get('href')
        print(url_content_temp)
        url_content_temp = re.findall('.*\d\d/\d\d/', url)[0] + url_content_temp
        print('url_content:             ' + url_content_temp)

        pdf = soup.select('a[id="APP-Pdf"]')
        # http://www.81.cn/jfjbmap/content/1/2019-03/08/11/2019030811_pdf.pdf
        #                            ../../1/2019-03/08/11/2019030811_pdf.pdf
        pdf = pdf[0].get('href')
        pdf = 'http://www.81.cn/jfjbmap/content/' + pdf[6:]
        print('pdf: ', pdf)
        pdf_save(pdf, headers, url_content_temp)
        json_save(url_content_temp, headers)


# 按时间获取url
daystart = datetime.datetime.strptime("2019-01-01", "%Y-%m-%d").date()
daystop = datetime.datetime.strptime("2019-06-30", '%Y-%m-%d').date()
urls = []
while daystart <= daystop:
    day = daystart.strftime("%Y-%m/%d")
    # http://www.81.cn/jfjbmap/content/2019-03/08/node_2.htm
    # http://www.81.cn/jfjbmap/content/2015-01/08/node_2.htm
    s = 'http://www.81.cn/jfjbmap/content/'+day+'/node_2.htm'
    urls.append(s)
    daystart = daystart + datetime.timedelta(days=1)
print(urls)
headers = {
    'User-Agent': 'Windows Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
}
for url in urls:
    get_info_main(url, headers)
