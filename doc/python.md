MongoDb:
pip install pymongo

crawler:
pip install requests
pip install beautifulsoup4
pip install lxml

django:
	??????:settings.py	TEMPLATES	'DIRS': [os.path.join(BASE_DIR, 'templates')](????project????templates?)

socket:
	django-channels	??WebSocket??

channels:
	pip install channels
	settings.py:
		将channels加入到INSTALLED_APPS中
		ASGI_APPLICATION = 'mysite.routing.application'
	
	

	1、views.py 中为房间视图创建视图函数
	
	2、urls.py 中创建房间视图的路由
	
	3、在 chat/consumers.py 中写入以下代码：
		# chat/consumers.py
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
				
	4、在 chat/routing.py 中输入以下代码：
		# chat/routing.py
		from django.conf.urls import url
		from . import consumers
		websocket_urlpatterns = [
			url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
		]
		
	5、在 mysite/routing.py 中, 导入 AuthMiddlewareStack、URLRouter 和 chat.routing ;并在 ProtocolTypeRouter 列表中插入一个 "websocket" 键, 格式如下:
		# mysite/routing.py
		from channels.auth import AuthMiddlewareStack
		from channels.routing import ProtocolTypeRouter, URLRouter
		import chat.routing
	
		application = ProtocolTypeRouter({
			# (http->django views is added by default)
			'websocket': AuthMiddlewareStack(
				URLRouter(
					chat.routing.websocket_urlpatterns
				)
			),
		})
	
	客户端请求用ws
		ws://192.168.1.100:8000/customer



## 文件操作

~~~
"r"   以读方式打开，只能读文件 ， 如果文件不存在，会发生异常      

"w" 以写方式打开，只能写文件， 如果文件不存在，创建该文件
 如果文件已存在，先清空，再打开文件

"rb"   以二进制读方式打开，只能读文件 ， 如果文件不存在，会发生异常      

"wb" 以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件
如果文件已存在，先清空，再打开文件

"rt"   以文本读方式打开，只能读文件 ， 如果文件不存在，会发生异常      

"wt" 以文本写方式打开，只能写文件， 如果文件不存在，创建该文件
如果文件已存在，先清空，再打开文件

"rb+"   以二进制读方式打开，可以读、写文件 ， 如果文件不存在，会发生异常      

"wb+" 以二进制写方式打开，可以读、写文件， 如果文件不存在，创建该文件
如果文件已存在，先清空，再打开文件
~~~



## 后端主动向前段推送消息的几种方式

https://blog.csdn.net/justyou_and_me/article/details/88218199