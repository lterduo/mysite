from django.urls import path

from FBV import views

urlpatterns = [
    path('hello',views.hello)
]