Mysql     yum安装
先去网https://dev.mysql.com/downloads/repo/yum/
下载对应系统的rpm包
https://repo.mysql.com//mysql57-community-release-el6-9.noarch.rpm




rpm –ivh   mysql57-community-release-el6-9.noarch.rpm
然后后就可以开心的yum 安装了


如果不知道当前使用的配置文件的路径，可以尝试下面的操作：
# which mysqld
/usr/local/mysql/bin/mysqld
# /usr/local/mysql/bin/mysqld --verbose --help |grep -A 1 'Default options'
2016-06-02 16:49:39 0 [Note] /usr/local/mysql/bin/mysqld (mysqld 5.6.25-log) starting as process 8253 ...
2016-06-02 16:49:41 8253 [Note] Plugin 'FEDERATED' is disabled.
Default options are read from the following files in the given order: 默认的选项是按照给定的顺序读取从以下文件:
/etc/mysql/my.cnf /etc/my.cnf ~/.my.cnf 
