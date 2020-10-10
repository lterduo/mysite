from django.conf.urls import url
from django.urls import path

from student import views
from .views import TestCBV
urlpatterns = [
    path('index', views.index),
    path('getgrade',views.getgrade),
    path('getstudent',views.getStudents),
    url(r'student/(\d+)/',views.student),
    url(r'^getdate/(\d+)/(\d+)',views.get_date),
    url(r'^testcbv/(\d+)',TestCBV.TestCBV.as_view())
]
