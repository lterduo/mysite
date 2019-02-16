import requests
import re
from bs4 import BeautifulSoup
import json
from pymongo import MongoClient

# headers = {
#     'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
# }
# urls = ['https://www.pexels.com/?page={}'.format(str(i)) for i in range(1, 10)]
# photos = []
# for url in urls:
#     wb_data = requests.get(url, headers=headers)
#     soup = BeautifulSoup(wb_data.text, 'lxml')
#     imgs = soup.select('article.photo-item > a > img')
#     for img in imgs:
#         if img.get('data-big-src') != None:
#             temp = img.get('data-big-src')
#             print('***************'+temp)
#             photos.append({"img":temp})

# mongoDB
client = MongoClient('mongodb://yldAdmin:112358@47.104.242.85:27017')
db_yld = client.yld
collection_imgs = db_yld.imgs
# imgs = {'img':'1'}
# imgs_insert = collection_imgs.insert_one(imgs)
# imgs_remove = collection_imgs.remove()
# imgs_update = collection_imgs.update(
#     {'img':'test'},
#     {'$set':
#         {'age':18}}
# )
# for i in photos:
#     imgs_find_one = collection_imgs.find_one(i)
#     if imgs_find_one :
#         continue
#     imgs_insert = collection_imgs.insert_one(i)

# with open('./python/photo.json', 'w') as f:
#     json.dump(photos, f, sort_keys=False , indent=4, separators=(',', ': '), ensure_ascii=False)

# collection_users = db_yld.users
# user = collection_users.find_one({'user_id': 'cdz'})
# user.pop('_id')
# print(user)
# user_info = json.dumps(user)
# print(user_info)

# collection_exam = db_yld.exam
# q1 = {"number": "1", "question": "1 + 1 = ?",
#       "answers": ["2", "3", "4"], "answer": "2"}
# q2 = {"number": "2", "question": "1 + 2 = ?",
#       "answers": ["2", "3", "4"], "answer": "3"}
# q3 = {"number": "3", "question": "2 + 2 = ?",
#       "answers": ["2", "3", "4"], "answer": "4"}
# collection_exam.insert_many([q1,q2,q3])

s = '[{number: 1, answer: 3}, {number: 2, answer: 3}, {number: 3, answer: 3}, {number: 4, answer: 世界第一傻}]'
s1 = s[1:-1]
s1 = json.loads(s1)
print(s1)
