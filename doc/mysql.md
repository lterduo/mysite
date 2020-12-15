# 安装配置
https://www.zhihu.com/tardis/sogou/art/44977117



1. “环境变量”的”系统变量“内，新建一个  MYSQL_HOME  变量，输入 MySQL 解压缩后文件夹的目录

2. 在“系统变量内”(系统变量，不是用户变量)找到其中的 “Path” 变量，双击打开，再最后加上

  %MYSQL_HOME%\bin

3. 新建 my.ini

  ~~~
  用新建txt的方式创建 my.ini 有时不能启动服务
  echo > my.ini 正常
  ~~~

  ~~~
  [mysql]  
  # 设置 mysql 客户端默认字符集  
  default-character-set=utf8 
   
  [mysqld]  
  #设置 3306 端口  
  port = 3306  
  
  # 设置 mysql 的安装目录  
  basedir=D:\mysql-5.7.31-winx64
  
  # 设置 mysql 数据库的数据的存放目录  
  datadir=D:\mysql-5.7.31-winx64\data 
  
  # 允许最大连接数  
  max_connections=200  
  
  # 服务端使用的字符集默认为 8 比特编码的 latin1 字符集  
  character-set-server=utf8  
  
  # 创建新表时将使用的默认存储引擎  
  default-storage-engine=INNODB
  ~~~

  

**以下命令最好用cmd执行，powershell不会提示错误**



4. 添加服务

  mysqld -install		// mysqld -remove

5. 初始化

  mysqld --initialize-insecure --user=mysql

6. 启动服务
    net start mysql

7. 登录
    mysql -u root -p //默认为 root，mysql -u <用户名> -p <密码>

8. 设置密码
    ALTER USER 'root'@'localhost' IDENTIFIED BY '112358jqk'; 

9. 操作数据库

   create database Shopping charset=utf8

10. 退出和停止
     不使用的时候最好停止 MySQL 服务~
       quit  // 退出
       net stop mysql // 停止服务

# 工具
https://www.heidisql.com/download.php

# vscode mysql
安装【vscode-database】插件
安装完成后按：【CTRL+SHILF+P】快捷键后点击【SQL:Connect to MySQL/PostgreSQL Server】选项。



