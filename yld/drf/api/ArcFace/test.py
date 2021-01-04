import socket  # 导入模块
# SOCK_STREAM---TCP协议方式
# AF_INET----我的是ipv4地址
# 1,创建socket对象：指定传输协议
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 2，建立连接发送连接请求 ip地址和端口号
# s.connect(('47.95.229.159', 38238))
# s.send("hei liuqi !".encode())  # 只能发送字节流需要用encode转码字符串成字节，不然无法发送文
import os
from datetime import datetime

dir_name = '../../static/customer_face_features/'

for root, dirs, files in os.walk(dir_name):
    for filename in files:
        print(filename)
        s_time = filename
        s_time = s_time.replace(' ', '_')
        print(s_time)
        # s_time = s_time[:-4]
        try:
            os.rename('../../static/customer_face_features/' + filename,
                      '../../static/customer_face_features/' + s_time)
        except Exception as e:
            with open('errlog.txt', 'a+') as f:
                f.writelines(str(datetime.now()) + '  filename_to_datetime.py')
                # f.write(str(datetime.now()) + '  filename_to_datetime.py')
                f.writelines(str(e))
                f.close()
