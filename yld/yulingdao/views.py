from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
import json

def auth(request):
    user_id = request.GET['user_id']
    password = request.GET['password']
    client = MongoClient('mongodb://yldAdmin:112358@47.104.242.85:27017')
    db_yld = client.yld
    collection_users = db_yld.users
    user = collection_users.find_one({'user_id': user_id})
    user_info = ''
    if user is None :
        return HttpResponse(user_info)
    if user['pass'] == password :
        user.pop('_id') # _id 为对象格式，需要删除
        user_info = json.dumps(user, ensure_ascii=False) #不转换的话，只把键过去了
    return HttpResponse(user_info)

def get_user(request):
    user_id = request.GET['user_id']
    client = MongoClient('mongodb://yldAdmin:112358@47.104.242.85:27017')
    db_yld = client.yld
    collection_users = db_yld.users
    user = collection_users.find_one({'user_id': user_id})
    user_info = ''
    if user is None :
        return HttpResponse(user_info)
    user.pop('_id') # _id 为对象格式，需要删除
    user_info = json.dumps(user, ensure_ascii=False) #不转换的话，只把键过去了
    return HttpResponse(user_info)

def news(request):
    client = MongoClient('mongodb://yldAdmin:112358@47.104.242.85:27017')
    db_yld = client.yld
    collection_imgs = db_yld.imgs
    info = collection_imgs.find()
    infos = []
    for i in info :
        i.pop('_id')
        infos.append(i)
    print(infos)
    imgs = json.dumps(infos)
    return HttpResponse(imgs)

def questions(request):
    client = MongoClient('mongodb://yldAdmin:112358@47.104.242.85:27017')
    db_yld = client.yld
    collection_questions = db_yld.questions
    result = collection_questions.find()
    questions = []
    for i in result:
        i.pop('_id')
        questions.append(i)
    questions = json.dumps(questions,ensure_ascii=False)
    print(questions)
    return HttpResponse(questions)

def exam(request):
    user_id = request.GET['user_id']
    result = request.GET['result']
    print(result)
    result = result[1:-1].split(',')
    #取出问题比较答案
    client = MongoClient('mongodb://yldAdmin:112358@47.104.242.85:27017')
    db_yld = client.yld
    collection_questions = db_yld.questions
    answers = collection_questions.find()
    i = 0
    j = 0 #答对数量
    while i < len(result):
        print(result[i] + '***************' + answers[i]['answer'])       
        if str(result[i]).strip() == str(answers[i]['answer']).strip() :
            j = j + 1
        i = i + 1
    score = int(j / len(result) * 100)
    #写入用户表
    collection_users = db_yld.users
    condition = {'user_id':user_id}
    user = collection_users.find_one(condition)
    user['score'] = score
    user_update = collection_users.update(condition,{'$set':user})
    print(user_update)
    return HttpResponse(score)