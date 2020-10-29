from django.db import models


class User(models.Model):
    userid = models.CharField(max_length=32, primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    organization = models.CharField(max_length=32, null=True)
    tel = models.CharField(max_length=32, null=True)
    email = models.CharField(max_length=32, null=True)
    addr = models.CharField(max_length=64, null=True)
    is_active = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    role_id = models.IntegerField()

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


class ProjectCategory(models.Model):
    name = models.CharField(max_length=32)
    desc = models.CharField(max_length=64)

    class Meta:
        db_table = 'project_category'
        verbose_name = verbose_name_plural = '课题类别表'


class Project(models.Model):
    name = models.CharField(max_length=64)
    leader = models.CharField(max_length=32)
    organization = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    status = models.CharField(max_length=10)
