from django.test import TestCase

# Create your tests here.
print('************************')
msg = "输入q退出:"
while True:

    choose = input(msg)
    if choose == 'q':
        break
    key1 = input('请输入你要添加的表属性: ')
    value1 = input('请输入你要添加表属性的类型: ')
    if key1 == '' or value1 == '':
        print('输入不能为空,输入错误,请重新输入!')
    if value1.upper() not in typeList:
        print('输入数据类型错误,请重新输入!')
        print('数据类有如下: ', typeList)
