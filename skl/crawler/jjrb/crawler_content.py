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

    title = soup.select('td[class="font01"]')
    if title:
        title = title[0].string.strip()
    print('title:',title)
    title_sub = ''
    
    s = soup.select('td[class="font02"]')
    author_name = []
    for i in s:
        if i.text:
            s1 = re.sub('□','',i.text).strip()
            author_name.append(s1)
    print('作者************',author_name)

    publish_time = re.findall('\d\d\d\d-\d\d/\d\d',url)[0]
    publish_time = re.sub('/', '-', publish_time)
    print('publish_time:',publish_time)

    s = soup.select('#ozoom p ')
    content = ''
    author_org = ''
    for s1 in s:
        s2 = s1.text.strip()
        if s2[0:4] == '（作者：' or s2[0:4] == '（作者系' or s2[0:5] =='（作者单位' or s2[0:6] =='（作者分别为' :
            author_org = s2[1:-1]
            print('author_org:',author_org)
        else:
            content = content + '\n' + s2

    source_name = '经济日报'
    source = {'name':source_name,"issue": "", "category": "报刊"}

    #判断第一段是否摘要，如果是，从正文摘除
    abstract = ''
    content_temp = content.strip().split('\n')
    print(content_temp)
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
        print("sens: " + str(i) + '  '+ sens[i])
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
    
    total_size = len(content) + len(title) + len(abstract)
    data = {'number':'','title':title,'title_en':'','title_sub':title_sub,\
    'author':author,'source':source,"keywords":"","abstract":abstract,"abstract_en":"","references":"",\
    "publish_time":publish_time,"base_category":"重要报刊",'base_sub_category':source_name, \
    "subject_category": {"first_class": "","second_class": "","third_class": ""},\
    'contents':contents,"total_page_size": 1,"total_size": total_size,"url": url}
    import os

    s = re.findall('\d\d\d\d-\d\d/\d\d/content_\d\d\d\d\d\d', url)[0] 
    s = re.sub('/', '-', s)
    s = 'jjrb_' + s
    print(s)

    import codecs  # 中文问题

    data['number'] = s   
    filename = './json/' + s + '.json' #文件名跟number相同
    with codecs.open(filename, 'w', 'utf-8') as f:
        json.dump(data, f, sort_keys=False , indent=4, separators=(',', ': '), ensure_ascii=False)

# headers = {
#     'User-Agent': 'Windows Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
# }
# json_save('http://paper.ce.cn/jjrb/html/2019-02/20/content_384335.htm',headers)
