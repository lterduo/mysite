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





https://blog.csdn.net/weixin_46704975/article/details/108409696?utm_medium=distribute.pc_relevant.none-task-blog-title-2&spm=1001.2101.3001.4242

# 一、安装的环境说明

Windows10 MySQL-8.0.21 zip
 (这个最新的版本并没有x64 msi版的安装，所以只能用zip版来进行安装）

# 二、出现服务器无法响应控制的几个原因

## 1.缺失运行库

 在CSDN查找MySQL安装步骤的文章时，很多文章并没有写明安装前需要安装运行库，所以像我这样子的新手菜鸟要注意安装MySQL前千万千万要注意检查自己电脑是否有运行库，没有的话一定要记得下载。 

解决方法：下载安装 Microsoft Visual C++ 2015 运行库就行。

## 2.mysql.ini配置文件问题

### 2.1配置文件没有用ANSI编码保存，而是用UTF-8编码保存

 像我当时是用VS Code来编写的这个文件的，所以编码格式默认保存为UTF-8。而MySQL读取时一定会解析失败。用其他开发环境编写这个文件的小伙伴们一定要注意这一点。 

解决方法：双击点开此文件，再点另存为，就会跳出ANSI编码保存格式。

### 2.2配置文件中basedir与datadir中的文件路径的‘/’改为‘//’

 关于这个，有些人不用改也可以顺利运行MySQL。 

## 3.其他原因及其解决方法

### 3.1在cmd窗口启动MySQL没有用管理员身份启动，权限不够。

 解决方法：用管理员身份启动cmd窗口即可。 

### 3.2其他方法

 解决方法在这里引用了老王的博客的博主的方法，附上链接:  [link](https://blog.csdn.net/wzbwzh/article/details/90450936?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~first_rank_v2~rank_v25-3-90450936.nonecase&utm_term=MySQL). 

管理员cmd窗口 进入mysql bin 目录

> 执行：sc delete mysql
>
> 执行：mysqld --install
>
> 执行： net start mysql

## 4.如果以上方法都不能解决问题

终极解决办法：开启两个cmd窗口运行MySQL。
 这里引用了风风biu博主的方法，附上链接: [link](https://blog.csdn.net/qq_41645678/article/details/106543925).







# 工具
https://www.heidisql.com/download.php

# vscode mysql
安装【vscode-database】插件
安装完成后按：【CTRL+SHILF+P】快捷键后点击【SQL:Connect to MySQL/PostgreSQL Server】选项。



