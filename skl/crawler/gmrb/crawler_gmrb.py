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
    # 用临时文件测试  第06版：学习贯彻习近平新时代中国特色社会主义思想特刊  会解析成NavigableString类型  应该是bs4的bug
    # 没有bug，应该用find_next_sibling()方法，而不是.netx_sibling属性，就可以取到bs类型啦
    # with codecs.open('temp.html','r','utf-8') as f:
    #     html = f.read()
    #     f.close()
    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'  # 解决乱码问题
    soup = BeautifulSoup(web_data.text, 'lxml')
    # soup = BeautifulSoup(html,'lxml')
    banmian = soup.find_all(id='pageLink')

    # 选择理论版块，提取url
    for i in banmian:
        if '理论' in i.text and "新闻" not in i.text\
            or '红船初心特刊' in i.text or '学习贯彻习近平新时代中国特色社会主义思想特刊' in i.text :
            print('banmian:    ' + i.text)
            url_temp = i.get('href')
            url_temp = url[0:-6] + url_temp[-6:]
            print('版面URL：   ', url_temp)
            if i.find_next_sibling():
                pdf = i.find_next_sibling().get('href')
            else:
                file_temp = open('./err.txt', 'a')
                file_temp.write('没有pdf：' + url_temp + '\n')
                file_temp.close()
                continue
            pdf = 'http://epaper.gmw.cn/gmrb/' + re.findall('images.*', pdf)[0]
            print('pdf:   ', pdf)
            # http://epaper.gmw.cn/gmrb/html/2018-01/04/nbs.D110000gmrb_11.htm
            #                  ../../../images/2019-02/18/16/zhikuGM16B20190218B.pdf
            # http://epaper.gmw.cn/gmrb/images/2019-02/18/16/zhikuGM16B20190218B.pdf
            # time.sleep(1)
            get_info(url_temp, headers, pdf)

def get_info(url, headers, pdf):
    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'  # 解决乱码问题
    soup = BeautifulSoup(web_data.text, 'lxml')
    url_content = soup.select('#titleList > ul > li > a ')
    for i in url_content:
        #  http://epaper.gmw.cn/gmrb/html/2019-02/21/nbs.D110000gmrb_01.htm
        #  http://epaper.gmw.cn/gmrb/html/2019-02/18/nw.D110000gmrb_20190218_1-01.htm
        #                                            nw.D110000gmrb_20190218_1-01.htm
        url_content_temp = i.get('href')
        url_content_temp = re.findall('.*\d\d/\d\d/', url)[0] + url_content_temp
        print('url_content:             ' + url_content_temp)
        # time.sleep(1)
        pdf_save(pdf, headers, url_content_temp)
        # time.sleep(1)
        json_save(url_content_temp, headers)


# 按时间获取url
daystart = datetime.datetime.strptime("2011-11-13", "%Y-%m-%d").date()
daystop = datetime.datetime.strptime("2011-12-31", '%Y-%m-%d').date()
urls = []
while daystart <= daystop:
    day = daystart.strftime("%Y-%m/%d")
    s = 'http://epaper.gmw.cn/gmrb/html/'+day+'/nbs.D110000gmrb_01.htm'
    urls.append(s)
    daystart = daystart + datetime.timedelta(days=1)
print(urls)
headers = {
    'User-Agent': 'Windows Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
}
for url in urls:
    get_info_main(url, headers)
    # time.sleep(1)
#  cd d:\mysite\skl\crawler\gmrb\
#  python crawler_gmrb.py
