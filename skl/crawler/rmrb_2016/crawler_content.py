import os
from bs4 import BeautifulSoup
import requests
import re
import json
from duanju import *

def json_save(path, file, number): 
    print(path,file,number)
    html = open(path + file, "r", encoding="gb18030")
    web_data = html.read()
    html.close()

    soup = BeautifulSoup(web_data, 'lxml')
    filename = re.findall('\d\d\d\d.\d\d.\d\d',file)[0].replace('.', '') #  2015.09.18     20150918
    if number < 10:
        filename = "10" + filename + "0" + str(number) # 102015091801
    else:
        filename = "10" + filename + str(number) 

    #重写html
    f = open('./json/' + filename + '.html', 'w', encoding='gb18030')
    f.write(web_data)
    f.close()

    #作者
    author_name = re.findall("第9版(.*)】",file)[0] #人民日报 2015.07.15 第7版杨光斌】.htm
    author_name = author_name.replace(' 作者：','')
    author_name = author_name.split(";")
    print(author_name)
    #内容、作者单位
    s = soup.select('.div_detail-neirong > p ')
    content = ''
    author_org = ''
    for s1 in s:
        s2 = s1.text.strip()
        if s2[0:4] == '（作者为' or s2[0:5] =='（作者单位' or s2[0:6] =='（作者分别为' :
            author_org = s2[1:-1]
            print('author_org:',author_org)
        else:
            content = content + '\n' + s2

    source_name = '人民日报'
    source = {'name':source_name,"issue": "", "category": "报刊"}
    #标题
    s = soup.select('.div_biaoti')
    print('title:    ', s)
    if s is not None:
        title = s[0].text.strip()
    if s is None:
        title = ''
    print('title:',title)
    #副标题
    s = soup.select('.div_biaoti2')
    # print(s)
    title_sub = []
    for s1 in s :
        if s1.string is not None:
            title_sub.append(s1.string.strip())
    print("title_sub:  ", title_sub)

    publish_time = re.findall('\d\d\d\d.\d\d.\d\d',file)[0]
    print('publish_time:',publish_time)

    #判断第一段是否摘要，如果是，从正文摘除
    abstract = ''
    content_temp = content.strip().split('\n')
    # print(content_temp)
    abstract_temp = content_temp[0]
    if abstract_temp[0:4] == '内容提要':
        abstract = abstract_temp
        content = '\n'.join(content_temp[1:])
    #判断第一段是否是作者
    print('author_name[0]: ', author_name[0])
    # print(abstract_temp)
    # print(abstract_temp.replace(' ','')) #很神奇，空格去不完全
    s = abstract_temp
    s = ''.join(s.split())
    # print(s)
    if author_name[0] in s:
        content = '\n'.join(content_temp[1:])

    # 处理内容
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
        if sens[i][-1] not in ('。', '！', '？', '…', '”',):
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
    'contents':contents,"total_page_size": 1,"total_size": total_size,"url": ""}

    import codecs  # 中文问题
    data['number'] = filename
    filename = './json/' + filename + '.json' #文件名跟number相同

    with codecs.open(filename, 'w', 'utf-8') as f:
        json.dump(data, f, sort_keys=False , indent=4, separators=(',', ': '), ensure_ascii=False)


# json_save('/人民日报/2016/', '【人民日报 2016.01.05 第7版巩海滨】.html', 1)