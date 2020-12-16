ssh-keygen -t rsa -C "lterduo@qq.com"
新增ssh key, 内容为C:\Users\Administrator\.ssh\id_rsa.pub
ssh -T git@github.com  #查看绑定是否成功
git config --global user.name "lterduo"
git config --global user.email "lterduo@qq.com"

git init
git clone https://github.com/lterduo/test.git
git clone https://github.com/lterduo/test.git mypro
git clone git://github.com/lterduo/test.git

git remote add origin git@github.com:lterduo/Django.git

git remote add origin https://github.com/lterduo/skl.git
git push -u origin master

git init
git add .
git commit  -m 'version 1.0.0'
git remote add origin https://github.com//lterduo/test.git
git push -u origin master

git add README
git commit -m 'first commit'
git push origin master

git pull

先删除已关联的名为origin的远程库：

git remote rm origin
然后，先关联GitHub的远程库：

git remote add github git@github.com:michaelliao/learngit.git
注意，远程库的名称叫github，不叫origin了。

接着，再关联码云的远程库：

git remote add gitee git@gitee.com:liaoxuefeng/learngit.git
同样注意，远程库的名称叫gitee，不叫origin。

现在，我们用git remote -v查看远程库信息，可以看到两个远程库：

git remote -v
gitee    git@gitee.com:liaoxuefeng/learngit.git (fetch)
gitee    git@gitee.com:liaoxuefeng/learngit.git (push)
github    git@github.com:michaelliao/learngit.git (fetch)
github    git@github.com:michaelliao/learngit.git (push)
如果要推送到GitHub，使用命令：

git push github master
如果要推送到码云，使用命令：

git push gitee master
这样一来，我们的本地库就可以同时与多个远程库互相同步：

github项目提交失败 master -> master (non-fast-forward)
官方介绍：
https://help.github.com/articles/dealing-with-non-fast-forward-errors
我的解决方法是：
参考：
http://stackoverflow.com/questions/9661059/git-pull-rebase-upstream-git-push-origin-rejects-non-fast-forward
先执行git pull
然后再执行 git push --force origin master 替换原先的git push -u origin master







# 加速

https://blog.csdn.net/weixin_44821644/article/details/107574297

### 二，gitclone.com

这是我用过最爽最实用功能最全面的一个方式了。gitclone.com是一个提供下载缓存的代码下载网站，使用方法十分简单，只需要**在仓库地址前面加上 gitclone.com**，就可以使速度提升几倍。

例如要克隆github上仓库地址`https://github.com/killer-p/ctool.git`
 只需将地址改为`https://gitclone.com/github.com/killer-p/ctool.git`，在命令行中执行`git clone https://gitclone.com/github.com/killer-p/ctool.git`，速度直接起飞！芜湖！**