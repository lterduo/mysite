from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views

from django.conf.urls import url, include

# from api.views import AuthView

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'role', views.RoleViewSet)
router.register(r'projectCategory', views.ProjectCategoryViewSet)
router.register(r'projectInfo', views.ProjectInfoViewSet)
router.register(r'projectStatus', views.ProjectStatusViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello/', views.hello),
    url(r'^api/login/$', views.AuthView.as_view()),
    url(r'^api/', include(router.urls)),
]
