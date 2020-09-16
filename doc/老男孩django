p5
    jinja2
p09
    静态文件

10 通用步骤
    创建project
    配置
        1、模板路径
            template
        2、静态文件路径 js、css、图片 
            static: 一定加逗号
                STATIC_URL = '/static/'
                STATICFILES_DIRS = (
                    os.path.join(BASE_DIR, 'static'),
                )


        3、middleware
            csrfViewMiddleware注释掉
12 模板语言特殊标记
    return render(request, 'login.html', {...})
    return redirect('/index/')

42  数据库操作优化
52  layout.html
        后台管理，左侧div，宽度一般定死
        bootstrap
        font-awesome
55  cookie
64  动态路由
70  连接数据库
        创建数据库
        修改 settings.py database项
        __init__.py 中
            import pymysql
            pymysql.install_as_MySQLdb()    #用pymysql替换MySQLdb
        
        注册app settings.py INSTALLED_APPS
        创表
        python manage.py makemigrations
        python manage.py migrate
        class UserGroup(models.Model):
            title = models.CharField(max_length=32)
        class UserInfo(models.Model):
            nid = models.BigAutoField(primary_key=True)
            user = models.CharFiedl(max_length=64)
            age = models.IntegerField(default=1)
            ug = models.ForeignKey("UserGroup", null=Ture)  #建外键 UserGroup ，但是添加的列名为 ug_id
        再执行另个命令 makemigrations