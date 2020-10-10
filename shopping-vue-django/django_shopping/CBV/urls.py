from django.urls import path

from CBV import views

urlpatterns = [
    path('book/',views.BookView.as_view())
]