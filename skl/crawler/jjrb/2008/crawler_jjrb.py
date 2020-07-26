import datetime
from bs4 import BeautifulSoup
import requests
import re

from crawler_content import *
import codecs

# 进主页面，判断是符合要求的版面，再取出版块url调用get_info

def get_info_main(url, headers):
    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'  # 解决乱码问题
    soup = BeautifulSoup(web_data.text, 'lxml')
    # soup = BeautifulSoup(html,'lxml')
    # banmian = soup.find_all(id='pageLink')
    banmian = soup.select('td[class="default"] > a[id="pageLink"]')

    # 选择理论版块，提取url     有一个隐藏的div，a标签id=pageLink，需要过滤掉
    for i in banmian:
        if '理论' in i.text :
            print('banmian:    ' + i.text)
            url_temp = i.get('href')
            url_temp = url[0:-10] + url_temp
            print('版面URL：   ', url_temp)
            
            pdf = ''
            get_info(url_temp, headers, pdf)


def get_info(url, headers, pdf):
    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'  # 解决乱码问题
    soup = BeautifulSoup(web_data.text, 'lxml')
    url_content = soup.select('#btdh a ')
    for i in url_content:
        if i.text.strip() == "本版编辑":
            continue
        #  http://paper.ce.cn/jjrb/html/2019-02/20/content_384331.htm
        #  http://epaper.gmw.cn/gmrb/html/2019-02/18/nw.D110000gmrb_20190218_1-01.htm
        #                                            nw.D110000gmrb_20190218_1-01.htm
        print('url_content_front', url)
        url_content_temp = i.get('href')
        print(url_content_temp)
        # url_content_temp = url[0:-11] + url_content_temp\
        url_content_temp = re.findall('.*\d\d/\d\d/', url)[0] + url_content_temp
        print('url_content:             ' + url_content_temp)

        json_save(url_content_temp, headers)


# 按时间获取url
daystart = datetime.datetime.strptime("2012-12-28", "%Y-%m-%d").date()
daystop = datetime.datetime.strptime("2012-12-31", '%Y-%m-%d').date()
urls = []
while daystart <= daystop:
    day = daystart.strftime("%Y-%m/%d")
    s = 'http://paper.ce.cn/jjrb/html/'+day+'/node_2.htm'
    urls.append(s)
    daystart = daystart + datetime.timedelta(days=1)
print(urls)
headers = {
    'User-Agent': 'Windows Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
}
for url in urls:
    get_info_main(url, headers)
