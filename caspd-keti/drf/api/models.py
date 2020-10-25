from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)

    class Meta:
        db_table = 'user'
        verbose_name = verbose_name_plural = '用户信息表'

class UserToken(models.Model):
    username = models.OneToOneField(to='User',on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=60)

    class Meta:
        db_table =  'user_token'
        verbose_name = verbose_name_plural = '用户token表'
