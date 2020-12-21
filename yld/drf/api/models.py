from django.db import models

class Customer(models.Model):    
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=2, null=True)
    tel = models.CharField(max_length=32, null=True)
    org = models.CharField(max_length=32, null=True)
    birth = models.CharField(max_length=16, null=True)
    addr = models.CharField(max_length=64, null=True)
    img = models.CharField(max_length=256, null=True)
    favour = models.TextField(null=True)
    relation = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'customer'
        verbose_name = verbose_name_plural = '客户信息表'


class CustomerImg(models.Model):
    pass


# class User(models.Model):
#     userid = models.CharField(max_length=32, primary_key=True)
#     username = models.CharField(max_length=32)
#     password = models.CharField(max_length=32)
#     organization = models.CharField(max_length=32, null=True)
#     tel = models.CharField(max_length=32, null=True)
#     email = models.CharField(max_length=32, null=True)
#     addr = models.CharField(max_length=64, null=True)
#     is_active = models.BooleanField(default=False)
#     create_time = models.DateTimeField(auto_now_add=True)
#     update_time = models.DateTimeField(auto_now=True)
#     role_id = models.IntegerField()

#     gender = models.CharField(max_length=2, null=True)
#     national = models.CharField(max_length=2, null=True)
#     birth = models.CharField(max_length=16, null=True)
#     duty = models.CharField(max_length=16, null=True)
#     title = models.CharField(max_length=16, null=True)
#     major = models.CharField(max_length=16, null=True)
#     education = models.CharField(max_length=16, null=True)
#     degree = models.CharField(max_length=16, null=True)
#     province = models.CharField(max_length=16, null=True)
#     zipcode = models.CharField(max_length=6, null=True)

#     class Meta:
#         db_table = 'user'
#         verbose_name = verbose_name_plural = '用户信息表'


# class UserToken(models.Model):
#     username = models.OneToOneField(to='User', on_delete=models.DO_NOTHING)
#     token = models.CharField(max_length=60)

#     class Meta:
#         db_table = 'user_token'
#         verbose_name = verbose_name_plural = '用户token表'


# class Role(models.Model):
#     role_id = models.IntegerField()
#     role_name = models.CharField(max_length=16)

#     class Meta:
#         db_table = 'role'
#         verbose_name = verbose_name_plural = '角色表'


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


# class ProjectCategory(models.Model):
#     name = models.CharField(max_length=32)
#     desc = models.CharField(max_length=64)

#     class Meta:
#         db_table = 'project_category'
#         verbose_name = verbose_name_plural = '课题类别表'


# class ProjectStatus(models.Model):
#     s_id = models.IntegerField()
#     status = models.CharField(max_length=10)

#     class Meta:
#         db_table = 'project_status'
#         verbose_name = verbose_name_plural = '课题状态表'


# class ProjectInfo(models.Model):
#     pid = models.CharField(max_length=64, null=True)
#     name = models.CharField(max_length=64, null=True)
#     category = models.CharField(max_length=32, null=True)
#     leader = models.CharField(max_length=32, null=True)
#     create_time = models.DateTimeField(auto_now_add=True)
#     update_time = models.DateTimeField(auto_now=True)
#     audit_time = models.DateTimeField(auto_now=True)
#     status = models.IntegerField()
#     result_type = models.CharField(max_length=16, null=True)
#     total_words = models.CharField(max_length=8, null=True)
#     complete_time = models.CharField(max_length=16, null=True)
#     content = models.TextField(null=True)

#     class Meta:
#         db_table = 'project_info'
#         verbose_name = verbose_name_plural = '课题信息表'


# # 废弃，改用user
# class ProjectLeader(models.Model):
#     pid = models.CharField(max_length=64, null=True)
#     userid = models.CharField(max_length=32, null=True)
#     name = models.CharField(max_length=32)
#     gender = models.CharField(max_length=2, null=True)
#     national = models.CharField(max_length=2, null=True)
#     birth = models.CharField(max_length=16, null=True)
#     duty = models.CharField(max_length=16, null=True)
#     title = models.CharField(max_length=16, null=True)
#     major = models.CharField(max_length=16, null=True)
#     education = models.CharField(max_length=16, null=True)
#     degree = models.CharField(max_length=16, null=True)
#     province = models.CharField(max_length=16, null=True)
#     organization = models.CharField(max_length=32, null=True)
#     tel = models.CharField(max_length=16, null=True)
#     email = models.CharField(max_length=32, null=True)
#     addr = models.CharField(max_length=64, null=True)
#     zipcode = models.CharField(max_length=6, null=True)

#     class Meta:
#         db_table = 'project_leader'
#         verbose_name = verbose_name_plural = '课题主持人表'


# class ProjectMember(models.Model):
#     pid = models.CharField(max_length=64, null=True)
#     name = models.CharField(max_length=32, null=True)
#     organization = models.CharField(max_length=32, null=True)
#     education = models.CharField(max_length=16, null=True)
#     major = models.CharField(max_length=16, null=True)
#     duty = models.CharField(max_length=16, null=True)
#     division = models.CharField(max_length=16, null=True)

#     class Meta:
#         db_table = 'project_member'
#         verbose_name = verbose_name_plural = '课题参加者表'


# # 附件
# class FileList(models.Model):
#     pid = models.CharField(max_length=64, null=True)
#     name = models.CharField(max_length=64, null=True)
#     path = models.CharField(max_length=256, null=True)
#     create_time = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'file_list'
#         verbose_name = verbose_name_plural = '申报书附件'


# # 审核信息
# class AuditInfo(models.Model):
#     pid = models.CharField(max_length=64, null=True)
#     auditor = models.CharField(max_length=64, null=True)
#     info = models.TextField(null=True)
#     create_time = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'audit_info'
#         verbose_name = verbose_name_plural = '审核信息表'


# # 课题分配表
# class ProjectDistribute(models.Model):
#     pid = models.CharField(primary_key=True, max_length=64)
#     pname = models.CharField(max_length=64, null=True)  # 项目名称
#     category = models.CharField(max_length=32, null=True)
#     assessor = models.CharField(max_length=32, null=True)  # 专家userid
#     aname = models.CharField(max_length=32, null=True)  # 专家姓名
#     is_active = models.BooleanField(default=True)
#     create_time = models.DateTimeField(auto_now_add=True)
#     update_time = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'project_distribute'
#         verbose_name = verbose_name_plural = '课题分配表'
