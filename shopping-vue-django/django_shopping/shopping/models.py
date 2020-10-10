from django.db import models

# Create your models here.


class Music(models.Model):
    song = models.TextField()
    singer = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"

class Book(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    class Meta:
        db_table = "book"


# 用户登录
class User(models.Model):
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)

    class Meta:
        db_table = 'user'
        verbose_name = verbose_name_plural = '用户信息表'

class userToken(models.Model):
    username = models.OneToOneField(to='User',on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=60)

    class Meta:
        db_table =  'user_token'
        verbose_name = verbose_name_plural = '用户token表'

# 用户管理
class SpUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=128)
    qq_open_id = models.CharField(max_length=32, blank=True, null=True)
    password = models.CharField(max_length=64)
    user_email = models.CharField(max_length=64)
    user_email_code = models.CharField(max_length=13, blank=True, null=True)
    is_active = models.IntegerField()
    user_sex = models.CharField(max_length=2)
    user_qq = models.CharField(max_length=32)
    user_tel = models.CharField(max_length=32)
    user_xueli = models.CharField(max_length=2)
    user_hobby = models.CharField(max_length=32)
    user_introduce = models.TextField(blank=True, null=True)
    create_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sp_user'