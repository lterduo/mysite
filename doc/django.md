# 版本

~~~
pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ django==2.2

pip install djangorestframework
pip install django-cors-headers
pip install django-filter
pip install pymysql
~~~



# 国内源

~~~
# 清华源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 或：
# 阿里源
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
# 腾讯源
pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple
# 豆瓣源
pip config set global.index-url http://pypi.douban.com/simple/
~~~





# 运行

django-admin startproject mysite
django-admin startapp login
或 python manage.py startapp login
python manage.py runserver 
python manage.py runserver 0.0.0.0:8000 


`'login' 这个 app 加入到 settings.py 中，否则makemigrations 会提示没有没有变化`

# mysql
1.在settings.py中配置
DATABASES = {
 'default': {
  'ENGINE': 'django.db.backends.mysql',　　# 数据库引擎
  'NAME': 'django',　　　　　　　　　　　　　　# 你要存储数据的库名，事先要创建之
  'USER': 'root',　　　　　　　　　　　　　　# 数据库用户名
  'PASSWORD': '112358jqk',　　　　　　　　　# 密码
  'HOST': 'localhost',　　　　　　　　　　　　# 主机
  'PORT': '3306',　　　　　　　　　　　　　　 # 数据库使用的端口
 }
}
    `mysql -uroot -p`
    `create database django charset=utf8;`

2.数据库迁移
pip install pymysql
在项目文件夹下的_init_.py添加如下代码(settings.py同级)
import pymysql
pymysql.install_as_MySQLdb()

3.
python manage.py makemigrations
python manage.py migrate

# settings.py

* ```
  ALLOWED_HOSTS = ['*']
  ```

* 注册app

* ```
  LANGUAGE_CODE = 'zh-hans'
  TIME_ZONE = 'Asia/Shanghai'
  USE_TZ = False
  ```





# 基础

## models
    book = Book.objects.all()
    book = Book.objects.get(pk=2)   primary key
    book.name = 'Jack'
    book.delete()
    book.save()
*****
### 建表
class Grade(models.Model):
    g_name = models.CharField(max_length=32)

class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_grade = models.ForeignKey(Grade,on_delete=models.CASCADE)
    

### 查询
    objects.filter  exclude all
    book = Book.objects.filter(price__gt=50).filter.filter.exclude.exclude.....

* 通过grade.student_set获得班级
    grade = Grade.objects.get(pk=1)
    students = grade.student_set.all()
### insert
1. book = Book.objects.create('...')
2. book = Book('...')
3. book = Book()
   book.name = 'ttt'
4. book.save()

### 方法总结
1. all()
2. filter()
3. exclude()
4. order_by()
5. values() 将查询到的每条数字生成一个字典，返回一个列表
    转json用
返回单个数据
1. get()    ******尽量少用，返回多个时会异常
2. first()
3. last()
查询条数
4. count()
是否存在
5. exists()     count和exists常用登陆判断

### 切片
objects.all()[5:15]
相当于sql中的offset和limit，不是python切片（不能一次把数据读入内存），所以下标不能是负数
分页用

### 查询条件
属性__运算符 = 值   price__gt = 
1. gt
2. lt
3. gte
4. lte
5. in   在某一集合中
6. contains             模糊查询****
7. startswith           模糊查询****
8. endswith             模糊查询****
9. exact                精确查询
10. 前面加i,ignore igt ilt... 忽略
11. 时间类型    objects.all(xxxtime__month=9)   及时存在9月的数据也不会返回，因为时区bug
    修改    settings.py USE_TZ = False
12. pk = 1
13. 跨关系查询
        grades = Grade.objects.filter(student__s_name='jack')
### 聚合函数
使用aggregate()函数返回聚合函数的值
1. Avg
2. Count
3. Max
4. Min
5. Sum
    objects.aggregate(Max('price'))
### F函数
比较两列的值
    objects.filter(boy_number__lt=F('gile_number')) F函数不但可以获取值，还可以根据值做运算
    objects.filter(boy_number__lt=F('gile_number')-15)
    注意F函数要导入，

### Q函数
可以对查询条件封装，支持逻辑运算
    filter(Q(boy_number__lt=5) & Q(girl_number__gt=10))
    &--and  |--or   ~--not

class Grade(models.Model):
    g_name = models.CharField(max_length=32)

class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_grade = models.ForeignKey(Grade,on_delete=models.CASCADE)

### 模型成员
* 显性属性

  * 开发者手动书写的属性

*  隐性属性

  * orm自动生成的

  * 如果手动声明了，系统就不会生成隐性属性了
    * 如objects是一个models.Manager()，如果在模型类Book中定义了
      
      b_m = models.manager()
      
      则使用objects就会报错，必须使用b_m
      
    * 比如做逻辑删除时，模型加一个is_delete=False
      
      每次删除都是修改is_delete=true,而不是真删除
      
      查询时filter(is_delete=False)
      
      每次查都要加这个条件，那么就可以重新Manager了
      
    * 在Manager中重写create(),或者重新定义一个new_create()

### 重写类方法

在不修改表的情况下加默认值等等约束

    在类中重新定义
    @classmethod
    def create(cls,name='test',price=10):
        return cls(name='test',price=10)

## 数据类型
    TextField
    BooleanField



## 数据迁移

* 项目migrations目录的py文件，对应数据库的django_migrations表里的记录
  * 先删除相应的py文件，再删除表中对应的数据，再做迁移



django.db.utils.OperationalError: (1050, "Table '表名' already exists）解决方法

python manage.py migrate myapp --fake





## sql 转 model

~~~
python manage.py inspectdb
~~~

直接生成models，拷贝到models.py

或者删除models.py，直接重定向

~~~
python manage.py inspectdb > app.models.py
~~~

* 注意：manage = False, 不被迁移系统管理，按需修改



## url

* student 下新建 urls.py
      urlpatterns = [
          path('index/', views.index)
      ]
      `alt + enter` 导包，新建
  项目 urls.py
      path('student/',include('student.urls'))
      导包

* url(r'^student/(\d+)/(\d+)/(\d+)/',views.student)

  * url可以用正则。student函数接收/(\d+)/后面的参数，但是是顺序参数

  * url(r'^getdate/P?<year>(\d+)/P?<month>(\d+)/P?<day>(\d+)/',views.student)

    关键字参数

  * 太麻烦，用顺序参数，函数里用y,m接收可好？

    `ctr + p` 参数提示
  
* 根据需要路径后加$

  * student/(\d+)有时匹配到student就结束了，需要在上个student后加$	student/$



## 域名反向解析 namespace

## HttpResponse

* 属性

r = HttpResponse()

r.content = 'heihei'

r.statuc_code = 404

r.content-type 	mime类型

* 方法
* 子类
  * HttpResponseRedirect
    * 缩写 redirect
  * JsonResponse
    * content-type 会自动设成 application/json

## request

* 属性

  * request.method

  * request.POST  GET  ...

    ```
    if request.method == 'POST'
    	request.POST.get('username')
    ```

  * ip = request.META.get('REMOTE_ADDR')

## Cookie

https://www.cnblogs.com/wusir66/p/9838986.html

response.set_cookie(key, value, max_age= ......)

request.COOKIES.get('name of key')

```
try:
	username = 
	if username == 
		return render(...)
except Exception as e:
	pass
return redirect('login')
```

```
#response.set_signed_cookie('username',username,salt='asdasd')    #带签名的cookie(加盐)
```

```
username = request.get_signed_cookie('username',salt='asdasd')     #获取带签名的cookie（盐要相同，不然拿不到）
```

```
response.delete_cookie('username')
```



## session

* session 依赖cookie

  session的存：

  [![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

  ```
  request.session['username'] = username#上面这一句代码完成了以下事情：
  #1、生成随机字符串
  #2、将随机字符串写到用户浏览器cookie
  #3、将随机字符串保存到服务器session#4、在服务器随机字符串对应的字典中设置相关内容
  request.session['password'] = password
  return HttpResponse('登陆成功')
  ```

  [![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

  session的取：

  ```
  username = request.session.get('username')
  #username = request.session['username']      #两种方式都可以取，但是这种如果没取到会报错
  password = request.session.get('password')
  ```

  session的删除：

  ```
  request.session.flush()    #删除session和cookie	推荐
  #del request.session['username']   #删除key为username的session
  return HttpResponse('清除成功')
  ```

   PS：在django中，session默认的过期时间是两周



## token

* 自定义的session(某些浏览器或移动端浏览器不支持session)



## csrf



## 中间件



# 类视图

* 继承自View
* url注册时要用as_view()



# *******



# P129 DRF



## 简略步骤

* 建model

* 写序列化器
* 写viewset
* urls里 router 里注册 viewset
  * 看习惯，可以拆分成根urls和app.urls



## APIVIEW

* render_classes
  * 渲染的类
* parser_classes
  * 解析转换的类
* authentication_classes
  * 认证
* throttle_classes
  * 节流
  * 控制请求频率的
* permission_classes
  * 权限
* content_negotiation_class
* metadata_class
* versioning_class



## ModelViewSet



## 条件查询

~~~
from django_filters import rest_framework

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [rest_framework.DjangoFilterBackend]
    filter_fields = ['name','price']
~~~

~~~
http://127.0.0.1:8000/api/book/?price=88
http://127.0.0.1:8000/api/book/?name=天龙八部&price=88
一个或者多个查询条件
~~~

vue中：

~~~
const data = await this.axios.get(`/api/book/?name=${name}&price=${price}`)
~~~



## 模糊查询

~~~
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend,SearchFilter]
    filter_fields = ['name','price']
    search_fields = ('price',)	#一定要有逗号
    pagination_class = MyPageNumberPagination
~~~

* **search_fields** 里的字段，是做模糊查询的字段，url中的关键字是“search”，如：

* 这时后端的接口就去search_fields里的“price”字段里做模糊查询，如果search_fields里有多个字段，就会在这个多个字段里全部做模糊匹配。

  ~~~
  http://localhost:8000/api/book/?search=2
  ~~~

* **filter_fields** 里的字段，是做精确查询的字段，url中的关键字就是filter_fields里的各个字段，如：

  ~~~
  http://localhost:8000/api/book/?name=天龙八部&price=88
  ~~~

  

## 分页

~~~
from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    # 默认每页显示的数据条数
    page_size = 8
    # 获取URL参数中设置的每页显示数据条数
    page_size_query_param = 'page_size'

    # 获取URL参数中传入的页码key
    page_query_param = 'page'

    # 最大支持的每页显示的数据条数（这个是用来限制page_size的）
    max_page_size = 4
~~~

~~~
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [rest_framework.DjangoFilterBackend]
    filter_fields = ['name','price']
    pagination_class = MyPageNumberPagination
~~~

~~~
http://localhost:8000/api/book/?page=2&size=5
~~~



## 排序

~~~
from rest_framework.filters import OrderingFilter
class FreeCourseListViewSet(ListModelMixin, GenericViewSet):
    queryset = models.Course.objects.filter(is_delete=False, is_show=True).all()
    serializer_class = serializers.CourseModelSerializer
    
    # 配置排序组件,调用[ ]中的类进行排序
    filter_backends = [OrderingFilter]
    # 配置参与排序字段
    ordering_fields = ['price', 'id', 'students']
    # 规则：
    #       ?ordering=price 按价格升序
    #       ?ordering=-price 按价格降序
    #       ?ordering=id 按主键升序
    #       ?ordering=-price,id 按价格降序，价格相同时按主键升序
~~~



***





# django-rest-framework



## 注意 url参数问题

## views、models 拆分成包	**暂时没必要

* refactor--convert to python package
* 注意要在\__init__.py中导入各个业务



https://github.com/twtrubiks/django-rest-framework-tutorial
pip install djangorestframework

 pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ djangorestframework

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
​        fields = ('id', 'song', 'singer', 'last_modify_date', 'created')
​        

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



## django rest_framework 实现用户登录认证

https://www.cnblogs.com/BlueSkyyj/p/11193982.html



# 常见问题



## 从已存在的Mysql数据库表生成model

python .\manage.py inspectdb
检查无误后，手动复制，后者
python manage.py inspectdb > models.py





## 下载文件中文名问题

* Content-Disposition

* 写下载歌词接口的时候遇到了一个问题，`中文.lrc`的文件下载之后的文件名的编码始终有问题，找了很久也没解决 过程暂且不表 最后靠自己解决了问题(靠!)

```
from urllib import parse
    self.set_header('Content-Type', 'application/octet-stream;')
    self.set_header('Content-Disposition', "attachment; filename*=UTF-8''{}".format(parse.quote(file_name)))
```

* 源码见 class DownloadFile(APIView):



## 跨域

* https://www.jianshu.com/p/16ce416555fe

~~~
# 跨域请求时，是否运行携带cookie，默认为False
CORS_ALLOW_CREDENTIALS = True
# 允许所有主机执行跨站点请求，默认为False
# 如果没设置该参数，则必须设置白名单，运行部分白名单的主机才能执行跨站点请求
CORS_ORIGIN_ALLOW_ALL = True
~~~



## 函数在django启动时执行

*  https://blog.csdn.net/qq_36963372/article/details/84847581
* 貌似好多问题



## Django执行定时任务（使用django-apscheduler）

* https://blog.csdn.net/weixin_43748870/article/details/102916168?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control



## 如何在python中调用终端命令

* os.system('python ./api/tests.py')
* os.system('python xxx.exe')



#  websocket  channels

* https://www.cnblogs.com/chuangming/p/9222794.html

* pip install channels

* 报错  Running setup.py install for twisted ... error

  https://www.cnblogs.com/dajie/p/11223775.html

  

* 1、settings.py 同级目录创建routing.py

  ~~~
  from channels.routing import ProtocolTypeRouter
  application = ProtocolTypeRouter({
      # (http->django views is added by default)
  })
  ~~~

* 2、settings.py  将 'channels' 添加到 INSTALLED_APPS 

  ~~~
  INSTALLED_APPS = [
      'channels',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'api'
  ]
  ~~~

  ```
  # Channels
  ASGI_APPLICATION = 'mysite.routing.application'
  ```

* 3、runserver 

  留意从 Starting ASGI/Channels development server at http://127.0.0.1:8000/ 开始的内容。这表明 Channels 开发服务器已接管了 Django 开发服务器。

* 4、api/consumers.py

  ~~~
  from channels.generic.websocket import WebsocketConsumer
  import json
  
  class ChatConsumer(WebsocketConsumer):
      def connect(self):
          self.accept()
  
      def disconnect(self, close_code):
          pass
  
      def receive(self, text_data):
          text_data_json = json.loads(text_data)
          message = text_data_json['message']
  
          self.send(text_data=json.dumps({
              'message': message
          }))
  ~~~

* 5、routing.py 中输入以下代码：

  ~~~
  from django.conf.urls import url
  
  from . import consumers
  
  websocket_urlpatterns = [
      url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
  ]
  ~~~

  