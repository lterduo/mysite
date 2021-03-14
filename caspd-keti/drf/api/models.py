from django.db import models
from django_jsonfield_backport.models import JSONField


class User(models.Model):
    userid = models.CharField(max_length=32, primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    organization = models.CharField(max_length=32, null=True)
    tel = models.CharField(max_length=32, null=True)
    email = models.CharField(max_length=32, null=True)
    addr = models.CharField(max_length=64, null=True)
    is_active = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10, default='未审核', help_text='注册状态，未审核、审核未通过、审核通过')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    role_id = models.IntegerField()
    gender = models.CharField(max_length=4, null=True)
    national = models.CharField(max_length=8, null=True)
    birth = models.CharField(max_length=16, null=True)
    duty = models.CharField(max_length=16, null=True, help_text='职务')
    title_level = models.CharField(max_length=16, null=True, help_text='职称级别')
    title = models.CharField(max_length=16, null=True, help_text='职称')
    major = models.CharField(max_length=16, null=True, help_text='研究专长')
    education = models.CharField(max_length=16, null=True, help_text='最后学历')
    degree = models.CharField(max_length=16, null=True, help_text='最后学位')
    province = models.CharField(max_length=16, null=True)
    zipcode = models.CharField(max_length=6, null=True)

    bank = JSONField(default={"bank": " ", "account": " "}, help_text='银行账号')

    class Meta:
        db_table = 'user'
        verbose_name = verbose_name_plural = '用户信息表'


class UserToken(models.Model):
    username = models.OneToOneField(to='User', on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=60)

    class Meta:
        db_table = 'user_token'
        verbose_name = verbose_name_plural = '用户token表'


class Role(models.Model):
    role_id = models.IntegerField()
    role_name = models.CharField(max_length=16)
    menus = JSONField(null=True, help_text='角色权限包含的菜单')

    class Meta:
        db_table = 'role'
        verbose_name = verbose_name_plural = '角色表'


# class Applicant(models.Model):
#     name = models.CharField(max_length=32)
#     organization = models.CharField(max_length=32)
#     tel = models.CharField(max_length=32)
#     email = models.CharField(max_length=32)
#     addr = models.CharField(max_length=64)
#     create_time = models.DateTimeField(auto_now_add=True)
#     update_time = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=False)

#     class Meta:
#         db_table = 'applicant'
#         verbose_name = verbose_name_plural = '申报人信息表'


# 暂时用user
# 专家信息表
class Assessor(models.Model):
    userid = models.CharField(max_length=32,  help_text='对应user表')
    name = models.CharField(max_length=32)
    major = models.CharField(max_length=16, null=True, help_text='研究方向')
    title = models.CharField(max_length=16, null=True, help_text='职称')

    class Meta:
        db_table = 'assessor'
        verbose_name = verbose_name_plural = '专家信息表'


# 专家方向表
class AssessorMajor(models.Model):
    name = models.CharField(max_length=16, null=True, help_text='研究方向')

    class Meta:
        db_table = 'assessor_major'
        verbose_name = verbose_name_plural = '专家研究方向表'


# 课题类型
class ProjectCategory(models.Model):
    name = models.CharField(max_length=32)
    desc = models.CharField(max_length=64, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'project_category'
        verbose_name = verbose_name_plural = '课题类别表'


# 课题类型子类
class ProjectCategorySon(models.Model):
    father_name = models.CharField(max_length=32, help_text='类别名，对应父类')
    name = models.CharField(max_length=32, help_text='子类名')
    desc = models.CharField(max_length=64, null=True)
    direction = JSONField(null=True, help_text='课题方向列表')

    class Meta:
        db_table = 'project_category_son'
        verbose_name = verbose_name_plural = '课题类别子类表'


# 课题状态
class ProjectStatus(models.Model):
    s_id = models.IntegerField()
    status = models.CharField(max_length=10)

    class Meta:
        db_table = 'project_status'
        verbose_name = verbose_name_plural = '课题状态表'


# 课题详细信息
class ProjectInfo(models.Model):
    pid = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=64, null=True)
    category = models.IntegerField(
        null=True, help_text='课题子类,对应project_category_son中id')
    category_direction = models.CharField(
        max_length=64, null=True, help_text='课题子类方向')
    leader = models.CharField(max_length=32, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    audit_time = models.DateTimeField(auto_now=True)
    status = models.IntegerField()
    result_type = models.CharField(max_length=16, null=True)
    total_words = models.CharField(max_length=8, null=True)
    complete_time = models.CharField(max_length=16, null=True)
    content = models.TextField(null=True)

    class Meta:
        db_table = 'project_info'
        verbose_name = verbose_name_plural = '课题信息表'


# 废弃，改用user
class ProjectLeader(models.Model):
    pid = models.CharField(max_length=64, null=True)
    userid = models.CharField(max_length=32, null=True)
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=2, null=True)
    national = models.CharField(max_length=2, null=True)
    birth = models.CharField(max_length=16, null=True)
    duty = models.CharField(max_length=16, null=True)
    title = models.CharField(max_length=16, null=True)
    major = models.CharField(max_length=16, null=True)
    education = models.CharField(max_length=16, null=True)
    degree = models.CharField(max_length=16, null=True)
    province = models.CharField(max_length=16, null=True)
    organization = models.CharField(max_length=32, null=True)
    tel = models.CharField(max_length=16, null=True)
    email = models.CharField(max_length=32, null=True)
    addr = models.CharField(max_length=64, null=True)
    zipcode = models.CharField(max_length=6, null=True)

    class Meta:
        db_table = 'project_leader'
        verbose_name = verbose_name_plural = '课题主持人表'


# 课题参加者
class ProjectMember(models.Model):
    pid = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=32, null=True)
    organization = models.CharField(max_length=32, null=True)
    education = models.CharField(max_length=16, null=True)
    major = models.CharField(max_length=16, null=True)
    duty = models.CharField(max_length=16, null=True)
    division = models.CharField(max_length=16, null=True)

    class Meta:
        db_table = 'project_member'
        verbose_name = verbose_name_plural = '课题参加者表'


# 附件
class FileList(models.Model):
    pid = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=64, null=True)
    path = models.CharField(max_length=256, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'file_list'
        verbose_name = verbose_name_plural = '申报书附件'


# 审核信息
class AuditInfo(models.Model):
    pid = models.CharField(max_length=64, null=True)
    auditor = models.CharField(max_length=64, null=True)
    info = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'audit_info'
        verbose_name = verbose_name_plural = '审核信息表'


# 课题分配表
class ProjectDistribute(models.Model):
    pid = models.CharField(max_length=64, null=True)
    pname = models.CharField(max_length=64, null=True)  # 项目名称
    assessor = models.CharField(max_length=32, null=True)  # 专家userid
    aname = models.CharField(max_length=32, null=True)  # 专家姓名
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'project_distribute'
        verbose_name = verbose_name_plural = '课题分配表'


# 课题评审结果表
class ProjectAssess(models.Model):
    pid = models.CharField(max_length=64, null=True)
    pname = models.CharField(max_length=64, null=True)  # 项目名称
    assessor_result = JSONField(null=True)  # 专家userid
    status = models.IntegerField(null=True)

    class Meta:
        db_table = 'project_assess'
        verbose_name = verbose_name_plural = '课题评审表'
