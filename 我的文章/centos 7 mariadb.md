使用的是linode的centos7系统，安装MySQL发现已经默认的是mariadb。

但是不管是使用linode官网说明还是百度搜索到的的根本安装方法无法安装成功。

总是提示这一句：

`ERROR 2002 (HY000): Can't connect to local mysql server through socket '/var/lib/mysql/mysql.sock' (2)`



最后通过google 搜索 install mariadb on centos 7得到了安装的关键一步。

现在安装成功，特此备注一下整个安装过程：

`[php] view plain copy
mysql:[root@localhost ~]# yum -y install mariadb*`  