import datetime
from bs4 import BeautifulSoup
import requests
import re
from crawler_content import *

def get_info_main(url,headers):
    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'  # 解决乱码问题
    soup = BeautifulSoup(web_data.text, 'lxml')
    # soup = BeautifulSoup(html,'lxml')
    banmian = soup.find_all(id='pageLink')

    # 选择理论版块，提取url
    for i in banmian:
        if '理论' in i.text :
            print('banmian:    ' + i.text)
            url_temp = i.get('href')
            url_temp = url[0:-6] + url_temp[-6:]
            print('理论版url：  ' + url_temp)
            get_info(url_temp, headers)


#保存pdf； 调用json_save爬取下层网址并保存json
def get_info(url,headers):
    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'  # 解决乱码问题
    soup = BeautifulSoup(web_data.text, 'lxml')

    #获取具体地址，爬取内容并保存json
    urls7 = soup.select('.news > ul > li > a ')
    for s in urls7:
        print(s.get('href'))
        '''
        http://paper.people.com.cn/rmrb/html/2018-08/02/nbs.D110000renmrb_07.htm
        http://paper.people.com.cn/rmrb/html/2018-08/02/nw.D110000renmrb_20180802_1-07.htm
                                                        nw.D110000renmrb_20180802_1-07.htm'''
        s = re.findall('.*\d\d/\d\d/', url)[0] + s.get('href')
        print(s)
        json_save(s,headers)

#按时间获取url
daystart = datetime.datetime.strptime("2020-07-01", "%Y-%m-%d").date()
daystop = datetime.datetime.strptime("2020-07-02",'%Y-%m-%d').date()
urls = []
while daystart <= daystop:
    day = daystart.strftime("%Y-%m/%d")
    s = 'http://paper.people.com.cn/rmrb/html/'+day+'/nbs.D110000renmrb_01.htm'
    urls.append(s)
    daystart = daystart + datetime.timedelta(days=1)

headers = {
    'User-Agent': 'Windows Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
}
for url in urls:
    get_info_main(url,headers)
    