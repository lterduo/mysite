"""django_shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from shopping import views

# 用户登录验证
from shopping.views import AuthView

# 接口注册路由
router = DefaultRouter()
router.register('music', views.MusicViewSet)
router.register('book',views.BookViewSet)
router.register('users',views.SpUserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('api/', include(router.urls)),
    # # 用户登录验证
    path('api/login/', AuthView.as_view()),
    # 学习,student
    path('student/',include('student.urls')),
    # 学习，CBV
    path('cbv/',include('CBV.urls')),
    # FBV
    path('fbv/',include('FBV.urls')),
    # 带参数查询
    url(r'^getBook/(\w+)/(\d+)/',views.BookView.as_view())
    # url(r'^getBook/P?<price>(\d+)/',views.BookView.as_view())
]
