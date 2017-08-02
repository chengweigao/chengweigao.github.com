CentOS6.5系统下安装Apache2.4+PHP5.6+Mysql5.5 (LAMP)
一直都认为国内最好的PHP框架为ThinkPHP，但有朋友说在做DB更新的时候，会出现偶然性几率的丢失掉 Where 条件，等于说做有条件的更新的时候，有可能就突然变成了全部更新， 。唯有转投当前最热门之一的 YII 框架 。

Down下基础框架后，跑一下，发现没效果，查看一下教程文档才发现原来需要最低 PHP5.4 的版本支持，但系统上用的是php5.3 的版本，看来要升级了。
吐槽一下，不知道为什么，php都更新了那么多个版本了，但是CentOS默认 yum 安装的还是PHP5.3 的版本，根本找不到直接升级PHP的方法，唯有手工编译升级了。

首先说下思路，因为一开始系统上已经跑了一套完成的 PHP 环境，那时候都是快速自动安装的，如果是跑一些5.3以下版本的话，很简单，几个指令，10分钟搞定了。
但现在要升级，彻底一点的话，唯有推倒重来了。所以步骤有：
1. 卸载掉当前的 Apache、php、MySQL；
2. 清除残留的一些配置文件；
3. 一步步安装 Apache 、mysql、php，当然在过程当中需要注意每个软件的依赖控件不可少。

下面是整体的步骤，从卸载后开始（同理适合刚刚安装好的全新系统）：

1. 准备工作，工欲善其事必先利其器，各个软件的安装包是必须的，有：

apr-1.5.1.tar.bz2
apr-util-1.5.4.tar.bz2
pcre-8.36.tar.bz2
httpd-2.4.10.tar.bz2

mysql-5.5.21.tar.gz

php-5.6.4.tar.bz2

具体的版本和下载地址相信大家都可以搜索下载好啦。

2. 安装Apache2.4

apr-1.5.1.tar.bz2
apr-util-1.5.4.tar.bz2
pcre-8.36.tar.bz2
这些是Apache依赖的一些安装包，解压，安装。


    cd apr-1.5.1
    ./configure --prefix=/usr/local/apr
    make && make install
    
    cd apr-util-1.5.4
    ./configure --prefix=/usr/local/apr-util --with-apr=/usr/local/apr
    make && make install
    
    cd pcre-8.36
    ./configure
    make && make install
    
    都完成后正式安装Apache
    cd httpd-2.4.10
    ./configure --prefix=/usr/local/apache2 --with-apr=/usr/local/apr --with-apr-util=/usr/local/apr-util --with-pcre=/usr/local/pcre --enable-so --enable-rewrite
    make && make install
    
    cp /usr/local/apache2/bin/apachectl /etc/rc.d/init.d/httpd
    servicehttpd start
测试是否安装成功

出现“It works”就说明Apache已经正常安装。


2. 安装Mysql
需要先安装好cmake

         yum -y install cmake make
       	cd mysql-5.5.21`
    	cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql -DMYSQL_DATADIR=/usr/local/mysql/data -DSYSCONFIGDIR=/usr/local/mysql/etc -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_ARCHIVE_STORAGE_ENGINE=1 -DWITH_BLACKHOLE_STORAGE_ENGINE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DMYSQL_UNIX_ADDR=/tmp/mysqld.sock -DMYSQL_TCP_PORT=3306 -DENABLED_LOCAL_INFILE=1 -DEXTRA_CHARSETS=all -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DMYSQL_USER=mysql
    
		make&& make install

配置mysql 5.5.21
    cp /usr/loacl/mysql/support-files/my-huge.cnfetc/my.cnf
    vi /etc/my.cnf
修改my.cnf配置，把innodb相关选项前面的#去掉，大概在115-130行之间。


    以下命令为mysql启动及自启动配置
    cp /usr/loacl/mysql/support-files/mysql.server /etc/init.d/mysqld
	/usr/local/mysql/scripts/mysql_install_db --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data &
    chkconfig --add mysqld
    chkconfig --level 345 mysqld on
     
    service mysqld start 
一般只要把my.cnf设置好这里就不会报错

剩下mysql的账号密码数据库等更改创建就还是老规矩了

3. 安装PHP5.6

>     cd php-5.6.4
>     	
>     ./configure --prefix=/usr/local/php
>      --with-apxs2=/usr/local/apache2/bin/apxs 
>     --with-libxml-dir=/usr/include/libxml2 
>     --with-config-file-path=/usr/local/apache2/conf 
>     --with-mysql=/usr/local/mysql 
>     --with-mysqli=/usr/local/mysql/bin/mysql_config 
>     --with-gd 
>     --enable-gd-native-ttf
>      --with-zlib --with-mcrypt
>      --with-pdo-mysql=/usr/local/mysql
>      --enable-shmop 
>     --enable-soap
>      --enable-sockets 
>     --enable-wddx 
>     --enable-zip 
>     --with-xmlrpc 
>     --enable-fpm 
>     --enable-mbstring 
>     --with-zlib-dir 
>     --with-bz2 
>     --with-curl 
>     --enable-exif 
>     --enable-ftp 
>     --with-jpeg-dir=/usr/lib 
>     --with-png-dir=/usr/lib 
>     --with-freetype-dir=/usr/lib/

有时候，CentOS会在编译过程中报错 mcrypt.h not found. Please reinstall libmcrypt
这个很好解决，百度一下就出来了，传送门
解决后

        make&& make install
    
    
    apache配置文件httpd.conf相关修改以支持PHP
    vim /usr/local/apache/conf/httpd.conf
    1. 添加php支持。
    AddType application/x-httpd-php .php .phtml
    AddType application/x-httpd-php-source .phps
    2. 添加默认索引页面index.php，再找到“DirectoryIndex”，在index.html后面加上“ index.php”
    DirectoryIndex index.html index.php
    3. 不显示目录结构，找到“Options Indexes FollowSymLinks”，修改为
    Options FollowSymLinks
    4. 开启Apache支持伪静态，找到“AllowOverride None”，修改为
    AllowOverride All
    保存httpd.conf配置，然后再执行以下两行命令
     chown -R nobody. /usr/local/apache/htdocs/
    chmod -R 777 /usr/local/apache/htdocs/
     service httpd restart
    

到这里基本 PHP环境搞定，测试一下.
 

尝试一下 YII2 是否可以正常运行

 
Bingo~~~ 收工。
