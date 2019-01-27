import requests
import re
from bs4 import BeautifulSoup
import json
headers = {
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
urls = ['https://www.pexels.com/?page={}'.format(str(i)) for i in range(1, 3)]
photos = []
for url in urls:
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    imgs = soup.select('article.photo-item > a > img')
    for img in imgs:
        if img.get('data-big-src') != None:
            temp = img.get('data-big-src')
            print('***************'+temp)
            # if re.findall('.*jpeg', temp):
            #     temp = re.findall('.*jpeg', temp)[0]
            photos.append({"img":temp})

with open('./python/photo.json', 'w') as f:
    json.dump(photos, f, sort_keys=False , indent=4, separators=(',', ': '), ensure_ascii=False)
# if photo_name:
#     fp = open(path + photo_name[0], 'wb')
#     fp.write(data.content)
#     fp.close()

# url = 'http://www.imagebam.com/gallery/7oyt77oqulbsotmggokeykvqato91k59'
# get_info(url)
# url_in = 'http://www.imagebam.com/image/2723a81102983184'
# web_data = requests.get(url_in, headers=headers)
# soup = BeautifulSoup(web_data.text, 'lxml')
# big_jpg = soup.select('.image')
# print(soup)