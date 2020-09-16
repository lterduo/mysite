# 运行
django-admin startproject mysite
django-admin startapp login
或 python manage.py startapp login
python manage.py runserver 
python manage.py runserver 0.0.0.0:8000 

TemplateDoesNotExist的解决方法：settings.py 修改templates的dirs
'DIRS': [os.path.join(BASE_DIR, 'templates')],
`'login' 这个 app 加入到 settings.py 中，否则makemigrations 会提示没有没有变化`

# mysql
1.在settings.py中配置
DATABASES = {
 'default': {
  'ENGINE': 'django.db.backends.mysql',　　# 数据库引擎
  'NAME': 'django',　　　　　　　　　　　　　　# 你要存储数据的库名，事先要创建之
  'USER': 'django',　　　　　　　　　　　　　　# 数据库用户名
  'PASSWORD': 'django@123',　　　　　　　　　# 密码
  'HOST': 'localhost',　　　　　　　　　　　　# 主机
  'PORT': '3306',　　　　　　　　　　　　　　 # 数据库使用的端口
 }
}
    `mysql -uroot`
    `create database charset=utf8;`

2.数据库迁移
pip install pymysql。
在项目文件夹下的_init_.py添加如下代码(settings.py同级)
import pymysql
pymysql.install_as_MySQLdb()

3.
python manage.py makemigrations
python manage.py migrate

# django-rest-framework
https://github.com/twtrubiks/django-rest-framework-tutorial
pip install djangorestframework

INSTALLED_APPS = (
    ...
    'rest_framework',
    `'musics'`
)

## models中
class Music(models.Model):
    song = models.TextField()
    singer = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

makemigrations  migrate

##  musics 新增 serializers.py
from rest_framework import serializers
from musics.models import Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        # fields = '__all__'
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created')
        
## views.py 
from musics.models import Music
from musics.serializers import MusicSerializer
from rest_framework import viewsets

class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

## urls.py
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from musics import views

router = DefaultRouter()
router.register(r'music', views.MusicViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]