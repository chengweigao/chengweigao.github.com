**centos7下yum升级被PackageKit锁定**

新安装centos7后，第一次升级出现下面的错误：

`Another app is currently holding the 
yum lock; waiting for it to exit...另一个应用程序是：PackageKit内存：163 M RSS （1.5 GB VSZ）已启动： Wed Jun 21 07:58:02 2017 - 06:42之前状态  ：睡眠中，进程ID：14023`
PackageKit是一个离线更新服务，基本没啥用途，应该永久禁用。
centos7下，

打开： /etc/yum/pluginconf.d/langpacks.conf 


将第一行：enable=1改为enable=0


ok，

在执行sudo yum update,就不会被锁定了。
