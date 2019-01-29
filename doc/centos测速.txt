测试写速度：
time dd if=/dev/zero bs=1024 count=1000000 of=/测试目录/1Gb.file
记录了1000000+0 的读入
记录了1000000+0 的写出
1024000000字节(1.0 GB)已复制，88.7857 秒，11.5 MB/秒

real    1m28.790s
user    0m0.299s
sys     0m2.256s

本地速度：
time dd if=/dev/zero bs=1024 count=1000000 of=/1Gb.file

记录了1000000+0 的读入
记录了1000000+0 的写出
1024000000字节(1.0 GB)已复制，2.29978 秒，445 MB/秒
测试itarget读取速度：

[root@node2 nfs-inspur]# fdisk -l

[root@node2 nfs-inspur]#
[root@node2 nfs-inspur]# hdparm -tT /dev/sdc

/dev/sdc:
 Timing cached reads:   15296 MB in  1.99 seconds = 7673.76 MB/sec
 Timing buffered disk reads:  34 MB in  3.03 seconds =  11.21 MB/sec
[root@node2 nfs-inspur]# hdparm -tT /dev/sda

/dev/sda:
 Timing cached reads:   17040 MB in  1.99 seconds = 8551.34 MB/sec
 Timing buffered disk reads: 544 MB in  3.00 seconds = 181.19 MB/sec

测主机网速
yum -y install iperf3*
服务端iperf3 -s 
客户端 
iperf3 -c 10.96.45.162 -u -i 1 -t X 
iperf3 -c 10.96.45.162 -w 4k -i 1 -t 60 #4K 
iperf3 -c 10.96.45.162 -w 4k -i 1 -t 60 -P 10 
-c：客户端模式，后接服务器ip 
-p：后接服务端监听的端口 
-i：设置带宽报告的时间间隔，单位为秒 
-t：设置测试的时长，单位为秒 
-w：设置tcp窗口大小，一般可以不用设置，默认即可
iperf3 -c 172.17.100.55 -i 1

直接查看网卡速度
ethtool enp6s0