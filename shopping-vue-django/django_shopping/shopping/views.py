from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View

from shopping.models import Music
from shopping.models import Book
from shopping.serializers import MusicSerializer
from shopping.serializers import BookSerializer
from shopping.models import SpUser
from shopping.serializers import SpUserSerializer

# 用户登录
import time
from shopping import models
from django.http import JsonResponse
from rest_framework.views import APIView

from rest_framework import viewsets


from django_filters import rest_framework
from rest_framework.filters import SearchFilter

# 分页
from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 8
    page_query_param = "page"
    page_size_query_param = "size"
    max_page_size = 4
    last_page_strings = ('last',)


# music   book    测试用
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [rest_framework.DjangoFilterBackend,SearchFilter]
    filter_fields = ['name','price']
    search_fields = ('price',)
    pagination_class = MyPageNumberPagination

class BookView(View):
    def get(self,request,name,price):
        p = price
        n = name
        data = {'name':name,'price': p}
        return JsonResponse(data)


# vue用户管理
class SpUserViewSet(viewsets.ModelViewSet):
    queryset = SpUser.objects.all()
    serializer_class = SpUserSerializer
# 用户登录
class AuthView(APIView):

    def post(self,request,*args,**kwargs):

        ret = {'code':100,'msg':None,'token':None}
        try:
            # 参数是datadict 形式
            usr = request.data.get('username')
            pas = request.data.get('password')

            # usr = request._request.POST.get('username')
            # pas = request._request.POST.get('password')

            # usr = request.POST.get('username')
            # pas = request.POST.get('password')

            print(usr)
            # obj = models.User.objects.filter(username='yang', password='123456').first()
            obj = models.User.objects.filter(username=usr,password=pas).first()
            print('obj*********************',obj)
            print(type(obj))
            # print(obj.username)
            # print(obj.password)
            if not obj:
                ret['code'] = 101
                ret['msg'] = '用户名或者密码错误'
                return JsonResponse(ret)
                # 里为了简单，应该是进行加密，再加上其他参数
            token = str(time.time()) + usr
            print(token)
            models.userToken.objects.update_or_create(username=obj, defaults={'token': token})
            ret['msg'] = '登录成功'
            ret['token'] = token
        except Exception as e:
            ret['code'] = 102
            ret['msg'] = '请求异常'
        return JsonResponse(ret)

def test(request):
    res = SpUser.objects.all()[0]
    print('*****************')
    print(repr(res))
    return HttpResponse('hei')