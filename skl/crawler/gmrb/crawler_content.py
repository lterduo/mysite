import datetime
from bs4 import BeautifulSoup
import requests
import re
import json
from duanju import *

def json_save(url,headers): # 爬取正文，生成json并保存
    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'  # 解决乱码问题
    soup = BeautifulSoup(web_data.text, 'lxml')

    s = soup.head.title.text
    if s == '404错误':
        file_temp = open('./err.txt', 'a')
        file_temp.write('没有本期报纸：' + url + '\n')
        file_temp.close()
        return
    # title = soup.h1.string.strip()
    if soup.h1:
        title = soup.h1.text
    
    print('title:', title)
    title_sub = ''
    if soup.h2 :
        title_sub  = soup.h2.text

    s = soup.select('.lai > span')[0].text.strip()
    s = re.sub('作者：','',s)
    author_name = []
    if s is not None:
        for s1 in s.split(' '):
            if s1 != '':
                author_name.append(s1)
    print('作者************',author_name)

    # 2015-01/02
    publish_time = re.findall('\d\d\d\d-\d\d/\d\d',url)[0]
    publish_time = re.sub('-', '年', publish_time)
    publish_time = re.sub('/', '月', publish_time) + '日'
    print('publish_time:',publish_time)

    s = soup.select('#articleContent > p ')
    content = ''
    author_org = ''
    for s1 in s:
        s2 = s1.text.strip()
        if s2[0:4] == '（作者：' or s2[0:5] =='（作者单位' or s2[0:6] =='（作者分别为' :
            author_org = s2[1:-1]
            print('author_org:',author_org)
        else:
            content = content + '\n' + s2
    source_name = '光明日报'
    source = {'name':source_name,"issue": "", "category": "报刊"}

    #判断第一段是否摘要，如果是，从正文摘除
    abstract = ''
    content_temp = content.strip().split('\n')
    # print(content_temp)
    abstract_temp = content_temp[0]
    if abstract_temp[0:4] == '内容提要':
        abstract = abstract_temp
        content = '\n'.join(content_temp[1:])

    sentences = []
    sections = []
    chapters = []
    contents = []
    sens = duanju_wenzhang(content)
    location = []  # 分段位置
    chap = [] #取chapter名称和位置
    i = 0
    while i < len(sens):
        # print("sens: " + str(i) + '  '+ sens[i])
        if sens[i][-1] not in ('。', '！', '？', '…', '”'):
            location.append(i)
        i = i + 1
    if len(location) != 0:
        if location[-1] == len(sens)-1:#防止把最后一句没标点的判断为chapter
            location.pop()
    chaptername = ''
    if len(location) == 0:
        chap.append({"name": chaptername, "loc1": 0, "loc2": len(sens)})
    j = 0
    if len(location) != 0:
        for i in location:
            if i == 0:
                chaptername = sens[0]
                continue
            chap.append({"name": chaptername, "loc1": j, "loc2": i})
            j = i
            chaptername = sens[i]
        chap.append({"name": chaptername, "loc1": j, "loc2": len(sens)})
    for c in chap:
        sentences = []  # 处理每段前先把sentences清空
        loc1 = c["loc1"]
        loc2 = c["loc2"]
        for sen1 in sens[loc1:loc2]:
            sentences.append({"page_num": 1, "is_cross_page": False, 'sentence': sen1})
        if c['name'] != '': #如果有chapter，则第一句应该是chapter而不是sentence
            sentences = sentences[1:]            

        sections = [{'name': '', "sentences": sentences}]
        chapters = [{'name': c["name"], 'section': sections}]
        contents.append({"chapter": chapters})
    author = []
    for i in author_name:
        author.append({'name':i, 'organization':author_org})
    publish_time1 = publish_time[0:4] + '-'+publish_time[5:7] + '-'+publish_time[8:10]
    total_size = len(content) + len(title) + len(abstract)
    data = {'number':'','title':title,'title_en':'','title_sub':title_sub,\
    'author':author,'source':source,"keywords":"","abstract":abstract,"abstract_en":"","references":"",\
    "publish_time":publish_time1,"base_category":"重要报刊",'base_sub_category':source_name, \
    "subject_category": {"first_class": "","second_class": "","third_class": ""},\
    'contents':contents,"total_page_size": 1,"total_size": total_size,"url": url}
    import os
    pubtime = publish_time[0:4] + publish_time[5:7] + publish_time[8:10]

    print(pubtime,'    ',publish_time)

    s = re.findall('gmrb_\d\d\d\d\d\d\d\d_\d-\d\d', url)
    if s :
        s = s[0]
    else:
        s = re.findall('gmrb_\d\d\d\d\d\d\d\d_\d\d-\d\d', url)[0]
#      http://epaper.gmw.cn/gmrb/html/2018-01/11/nw.D110000gmrb_20180111_10-05.htm
#      http://epaper.gmw.cn/gmrb/html/2018-01/10/nw.D110000gmrb_20180110_2-11.htm
    print(s)

    import codecs  # 中文问题
    # filename = './json/' + s + '.json'
    data['number'] = s   
    filename = './json/' + s + '.json' #文件名跟number相同
    with codecs.open(filename, 'w', 'utf-8') as f:
        json.dump(data, f, sort_keys=False , indent=4, separators=(',', ': '), ensure_ascii=False)

# headers = {
#     'User-Agent': 'Windows Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
# }
# json_save('http://epaper.gmw.cn/gmrb/html/2015-01/02/nw.D110000gmrb_20150102_1-06.htm?div=-1',headers)
