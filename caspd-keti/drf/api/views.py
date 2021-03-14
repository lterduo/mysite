from datetime import datetime
from urllib import parse
import json
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# 用户登陆
import time
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import viewsets
# 分页
from rest_framework.pagination import PageNumberPagination
# 模糊查询
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# 排序
from rest_framework.filters import OrderingFilter

from api import models
from api import serializers

# 转换pdf
from toPdf import toHtml
from toPdf import htmlToPdf

# 测试


def hello(request):
    for i in range(20):
        u = models.ProjectCategory()
        u.name = '课题类别' + str(i)
        u.desc = '类别描述巴拉巴拉' + str(i)
        # u.userid = 'lisi' + str(i)
        # u.username = '李四' + str(i)
        # u.password = '1234'
        # u.organization = '中国残联'
        # u.email = 'zhangsan@qq.com'
        # u.addr = '中国残联101室'
        # u.tel = '1300000000' + str(i)
        # u.role_id = 2
        u.save()
    return HttpResponse('hello')


# 分页器
class MyPageNumberPagination(PageNumberPagination):
    # 默认每页显示的数据条数
    page_size = 10000
    # 获取URL参数中设置的每页显示数据条数
    page_size_query_param = 'page_size'
    # 获取URL参数中传入的页码key
    page_query_param = 'page'
    # 最大支持的每页显示的数据条数（这个是用来限制page_size的）
    max_page_size = 10000


# 用户管理
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    pagination_class = MyPageNumberPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['userid', 'username',
                     'username', 'tel', 'role_id', 'major']
    search_fields = ('userid', 'username', 'organization',
                     'tel', 'email', 'addr')
    # 配置参与排序字段
    ordering_fields = ['role_id', 'username', 'is_active', 'tel']
    # print('*************************888888888888888888888')


# 角色管理
class RoleViewSet(viewsets.ModelViewSet):
    queryset = models.Role.objects.all()
    serializer_class = serializers.RoleSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['role_id']
    ordering_fields = ['role_id']


# 课题分类
class ProjectCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectCategory.objects.all().order_by('-is_active', '-id')
    serializer_class = serializers.ProjectCategorySerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['name', 'desc', 'is_active']
    search_fields = ('name', 'desc')
    ordering_fields = []


# 课题分类子类
class ProjectCategorySonViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectCategorySon.objects.all()
    serializer_class = serializers.ProjectCategorySonSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['father_name', 'name', 'desc', 'id']
    search_fields = ('father_name', 'name', 'desc')
    ordering_fields = ['father_name', 'name', 'desc']


# 课题状态
class ProjectStatusViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectStatus.objects.all()
    serializer_class = serializers.ProjectStatusSerializer


# 课题信息
class ProjectInfoViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectInfo.objects.all()
    serializer_class = serializers.ProjectInfoSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['name', 'leader', 'status',
                     'category', 'pid', 'category_direction']
    search_fields = ('name', 'leader', 'status',
                     'create_time', 'category', 'pid')
    ordering_fields = ['create_time', 'name', 'leader', 'status', 'category']


# 项目主持人信息
class ProjectLeaderViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectLeader.objects.all()
    serializer_class = serializers.ProjectLeaderSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['pid', 'userid', 'name', 'organization']
    search_fields = ('pid', 'userid', 'name', 'organization')


# 项目参加者信息
class ProjectMemberViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectMember.objects.all()
    serializer_class = serializers.ProjectMemberSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['pid',  'name', 'organization']
    search_fields = ('pid', 'name', 'organization')

# 申报人
# class ApplicantViewSet(viewsets.ModelViewSet):
#     queryset = Applicant.objects.all()
#     serializer_class = ApplicantSerializer
#     pagination_class = MyPageNumberPagination

#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filter_fields = ['name', 'tel']
#     search_fields = ('name', 'organization', 'tel', 'email', 'addr')


# 附件列表
class FileListViewSet(viewsets.ModelViewSet):
    queryset = models.FileList.objects.all()
    serializer_class = serializers.FileListSerializer
    pagination_class = MyPageNumberPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['pid', 'path', 'name', 'create_time']
    search_fields = ('pid', 'path', 'name', 'create_time')


# 审核信息
class AuditInfoViewSet(viewsets.ModelViewSet):
    queryset = models.AuditInfo.objects.all()
    serializer_class = serializers.AuditInfoSerializer
    pagination_class = MyPageNumberPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['pid', 'auditor', 'info', 'create_time']
    search_fields = ('pid', 'auditor', 'info', 'create_time')


# 课题分配
class ProjectDistributeViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectDistribute.objects.all()
    serializer_class = serializers.ProjectDistributeSerializer
    pagination_class = MyPageNumberPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['pid', 'pname', 'assessor', 'aname']
    search_fields = ('pid', 'pname', 'assessor', 'aname')
    ordering_fields = ['pname']


# 课题评审
class ProjectAssessViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectAssess.objects.all()
    serializer_class = serializers.ProjectAssessSerializer
    pagination_class = MyPageNumberPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['pid', 'pname', 'status']
    search_fields = ('pid', 'pname', 'status')
    ordering_fields = ['pname']


# 专家信息表
class AssessorViewSet(viewsets.ModelViewSet):
    queryset = models.Assessor.objects.all()
    serializer_class = serializers.AssessorSerializer
    pagination_class = MyPageNumberPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['userid', 'name', 'major', 'title']
    search_fields = ('userid', 'name', 'major', 'title')
    ordering_fields = ['name']


# 专家研究方向
class AssessorMajorViewSet(viewsets.ModelViewSet):
    queryset = models.AssessorMajor.objects.all()
    serializer_class = serializers.AssessorMajorSerializer
    pagination_class = MyPageNumberPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['name']
    search_fields = ('name')
    ordering_fields = ['name']


# 生成pdf
class GenPdf(APIView):
    def post(self, request):
        content = request.body
        content = json.loads(content.decode('utf8'))
        # print('genPdf*****************************', content)

        # 获取信息
        project = content['project']
        leader = content['leader']
        member = content['member']
        pid = project['pid']
        # print('genPdf*****************************', type(project))

        # 查询信息
        # project = models.ProjectInfo.objects.filter(pid=pid).first().__dict__

        project['create_time'] = datetime.now().strftime('%Y.%m.%d')
        if len(member) < 6:
            for i in range(6-len(member)):
                member.append({'name': ' '})

        # 模板列表
        fileList = ['附件1申报书01封面.html', '附件1申报书02承诺.html',
                    '附件1申报书03课题组基本情况.html', '附件1申报书04课题研究计划.html', '附件1申报书05项目主持人情况及课题研究基础.html']
        # 生成html
        toHtml.generate_html(fileList, pid, project, leader, member)
        htmlToPdf.html_to_pdf(fileList, pid)

        return JsonResponse({'pid': pid})


# 上传文件
class UploadFile(APIView):
    def post(self, request):
        file_obj = request.FILES.get("file")    # 获取文件要用request.FILES
        data = request.POST.get("data")       # 从POST请求中获取其他数据， 提前在formData中定义的

        data = json.loads(data)

        pid = data.get('pid')
        file_path = './uploadfiles/' + pid + '/'

        # 创建路径
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        file_path = file_path + file_obj.name
        # 保存
        with open(file_path, 'wb') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
        # 写FileList表
        file_list = models.FileList.objects.filter(path=file_path).first()
        if not file_list:
            file_list = models.FileList()
            file_list.pid = pid
            file_list.name = file_obj.name
            file_list.path = file_path
            file_list.save()

        message = {'status': 200}
        return JsonResponse(message)


# 删除文件
class DeleteFile(APIView):
    def post(self, request):
        path = request.body
        print('*********', path)
        path = json.loads(path)
        path = path['path']
        if path:
            os.remove(path)
        message = {'status': 200}
        return JsonResponse(message)


# 下载文件
class DownloadFile(APIView):
    def post(self, request):
        data = json.loads(request.body)
        response = {}
        file_name = data.get("name")
        file_path = data.get('path')
        print(file_name, '***', file_path)
        if not file_name:
            response["meta"] = {"code": 400}
            response["error"] = {"error_msg": "parameter error, no file_path"}
            return HttpResponse(json.dumps(response))

        with open(file_path, "rb") as f:
            res = HttpResponse(f)
            res["Content-Type"] = "application/octet-stream"  # 注意格式
            # 处理中文名
            res["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(
                parse.quote(file_name))
        return res


# 用户登陆
class AuthView(APIView):

    def post(self, request, *args, **kwargs):

        ret = {'code': 1000, 'msg': None}
        try:
            # 参数是datadict 形式
            usr = request.data.get('userid')
            pas = request.data.get('password')

            print(usr)
            # obj = models.User.objects.filter(username='yang', password='123456').first()
            obj = models.User.objects.filter(
                userid=usr, password=pas).first()

            if not obj:
                ret['code'] = '1001'
                ret['msg'] = '用户名或者密码错误'
                return JsonResponse(ret)
                # 后续进行加密，再加上其他参数
            token = str(time.time()) + usr
            print(token)
            models.UserToken.objects.update_or_create(
                username=obj, defaults={'token': token})
            ret['msg'] = '登录成功'
            ret['token'] = token
            ret['userid'] = obj.userid
            ret['username'] = obj.username
            ret['is_active'] = obj.is_active
            ret['role_id'] = obj.role_id

        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'

        return JsonResponse(ret)
