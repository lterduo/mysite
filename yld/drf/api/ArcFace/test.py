import socket  # 导入模块
# SOCK_STREAM---TCP协议方式
# AF_INET----我的是ipv4地址
# 1,创建socket对象：指定传输协议
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 2，建立连接发送连接请求 ip地址和端口号
# s.connect(('47.95.229.159', 38238))
# s.send("hei liuqi !".encode())  # 只能发送字节流需要用encode转码字符串成字节，不然无法发送文
import sys

bstr = b'0xAA' + b'0x01' + b'0x01' + b'0x01' + \
    b'0x00' + b'0x00' + b'0x00' + b'0xAD' + b'0x55'
s = '0xAA0x010x010x010x000x000x000xAD0x55'
print(bstr)
print(sys.getsizeof(bstr))
