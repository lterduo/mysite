# 安装配置
https://www.zhihu.com/tardis/sogou/art/44977117

1. 启动服务
net start mysql
2. 登录
mysql -u root -p //默认为 root，mysql -u <用户名> -p <密码>
3. 设置密码
<!-- ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password'; -->
4. 操作数据库

   create database Shopping charset=utf8

5. 退出和停止
  不使用的时候最好停止 MySQL 服务~
  quit  // 退出
  net stop mysql // 停止服务

# 工具
https://www.heidisql.com/download.php

# vscode mysql
安装【vscode-database】插件
安装完成后按：【CTRL+SHILF+P】快捷键后点击【SQL:Connect to MySQL/PostgreSQL Server】选项。