变量
    常量约定俗成用大写

字符串
    \r  把\r后的拉到当前行首
    \t  一个缩进
    元字符串：串前加r，不进行转义，原型化输出
        strvar = r"C:\flutter\bin\cache\nata"
    字符串格式化
        %d  %2d 占两位，居右    %-2d 占两位居左
            strvar = "hei%dhei" % (3)
        %f  默认保留6位     %.2f 保留2位 
        %s
元组    tuple
    可取值，不可修改，有序
    字符串跟元组相同，可取值，不可修改，有序
集合    set 
    无序，自动去重
字典    dict 

    可哈希数据（不可变）： Number(int float bool complex) str tuple
    不可哈希（可变）： list set dict
    集合的值，字典的键，必须是可哈希的

容器类型数据强制转换
    print(repr("hahaha"))   repr() 不转义字符，原型化输出

15
    注意短路： True or ...  后面的短路不执行了
    逻辑优先级： () > not > and > or
    isinstance(变量，类型)  isinstance(变量,(类型，类型...))

27 
    str.split(';',2)    分隔两次，后面的不再分隔，做一个list
    rsplit()            从右向左
    join    split的反操作

39  *args **kwargs      *args, 得到的参数为列表， **kwargs，得到的参数为字典
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)
test_var_args('yasoob', 'python', 'eggs', 'test')

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))
>>> greet_me(name="yasoob")
name == yasoob