import re
import os

path = "/报刊数据/人民日报/json2011"

dirs = os.listdir(path)
html = []
json = []

for file in dirs :
    if file[-4:] == 'html':
        html.append(file.replace('.html',''))
    if file[-4:] == 'json':
        json.append(file.replace('.json',''))

a = [x for x in html if x in json]
b = [y for y in (html + json) if y not in a]
print(b)