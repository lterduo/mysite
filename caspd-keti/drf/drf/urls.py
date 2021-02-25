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
router.register(r'projectCategorySon', views.ProjectCategorySonViewSet)
router.register(r'projectInfo', views.ProjectInfoViewSet)
router.register(r'projectStatus', views.ProjectStatusViewSet)
router.register(r'projectLeader', views.ProjectLeaderViewSet)
router.register(r'projectMember', views.ProjectMemberViewSet)
router.register(r'fileList', views.FileListViewSet)
router.register(r'auditInfo', views.AuditInfoViewSet)
router.register(r'projectDistribute', views.ProjectDistributeViewSet)
router.register(r'projectAssess', views.ProjectAssessViewSet)
router.register(r'assessor', views.AssessorViewSet)
router.register(r'assessorMajor', views.AssessorMajorViewSet)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello/', views.hello),
    url(r'^api/login/$', views.AuthView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^api/genPdf/', views.GenPdf.as_view()),
    url(r'^api/uploadFile/', views.UploadFile.as_view()),
    url(r'^api/deleteFile/', views.DeleteFile.as_view()),
    url(r'^api/downloadFile/', views.DownloadFile.as_view()),
]
