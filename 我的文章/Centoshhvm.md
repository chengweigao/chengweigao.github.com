> Centos + HHVM 生产环境安装!
>  分享 ⋅ Denniskevin ⋅ 于 2年前 ⋅ 最后回复由 yzdel200 于 2年前 ⋅ 6726 阅读
> 一、配置防火墙，开启80端口、3306端口
> 
> CentOS 7.0默认使用的是firewall作为防火墙，这里改为iptables防火墙。
> 
> 1、关闭firewall：
> 
> systemctl stop firewalld.service #停止firewall
> 
> systemctl disable firewalld.service #禁止firewall开机启动
> 
> 2、安装iptables防火墙
> 
> yum install iptables-services #安装
> 
> vi /etc/sysconfig/iptables #编辑防火墙配置文件
> 
> # Firewall configuration written by system-config-firewall
> 
> # Manual customization of this file is not recommended.
> 
> *filter
> 
> :INPUT ACCEPT [0:0]
> 
> :FORWARD ACCEPT [0:0]
> 
> :OUTPUT ACCEPT [0:0]
> 
> -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
> 
> -A INPUT -p icmp -j ACCEPT
> 
> -A INPUT -i lo -j ACCEPT
> 
> -A INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT
> 
> -A INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT
> 
> -A INPUT -m state --state NEW -m tcp -p tcp --dport 3306 -j ACCEPT
> 
> -A INPUT -j REJECT --reject-with icmp-host-prohibited
> 
> -A FORWARD -j REJECT --reject-with icmp-host-prohibited
> 
> COMMIT
> 
> :wq! #保存退出
> 
> systemctl restart iptables.service #最后重启防火墙使配置生效
> 
> systemctl enable iptables.service #设置防火墙开机启动
> 
> 二、关闭SELINUX
> 
> vi /etc/selinux/config
> 
> #SELINUX=enforcing #注释掉
> 
> #SELINUXTYPE=targeted #注释掉
> 
> SELINUX=disabled #增加
> 
> :wq! #保存退出
> 
> setenforce 0 #使配置立即生效
> 
> 三 、系统约定
> 
> 软件源代码包存放位置：/usr/local/src
> 
> 源码包编译安装位置：/usr/local/lnmp+hhvm
> 
>  点赞
>  
> 回复数量: 25
> •	 
> zhuzhichao MOD Lalala Demacian !
> #1 ⋅ 2年前
> 赞！
> •	 
> Denniskevin
> #2 ⋅ 2年前
> 
> 安装包!
> 
> 1、下载nginx（目前稳定版）
> 
> http://nginx.org/download/nginx-1.6.2.tar.gz
> 
> 2、下载MySQL
> 
> http://cdn.mysql.com/archives/mysql-5.6/mysql-5.6.21.tar.gz
> 
> 3、下载php
> 
> http://cn2.php.net/distributions/php-5.6.4.tar.gz
> 
> 4、下载pcre （支持nginx伪静态）
> 
> ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.35.tar.gz
> 
> 5、下载openssl（nginx扩展）
> 
> http://www.openssl.org/source/openssl-1.0.1h.tar.gz
> 
> 6、下载zlib（nginx扩展）
> 
> http://zlib.net/zlib-1.2.8.tar.gz
> 
> 7、下载cmake（MySQL编译工具）
> 
> http://www.cmake.org/files/v2.8/cmake-2.8.11.2.tar.gz
> 
> 8、下载libmcrypt（php扩展）
> 
> http://nchc.dl.sourceforge.net/project/mcrypt/Libmcrypt/2.5.8/libmcrypt-2.5.8.tar.gz
> 
> 9、下载yasm（php扩展）
> 
> http://www.tortall.net/projects/yasm/releases/yasm-1.2.0.tar.gz
> 
> 10、t1lib（php扩展）
> 
> ftp://sunsite.unc.edu/pub/Linux/libs/graphics/t1lib-5.1.2.tar.gz
> 
> 11、下载gd库安装包
> 
> https://bitbucket.org/libgd/gd-libgd/downloads/libgd-2.1.0.tar.gz
> 
> 12、libvpx（gd库需要）
> 
> https://webm.googlecode.com/files/libvpx-v1.3.0.tar.bz2
> 
> 13、tiff（gd库需要）
> 
> http://download.osgeo.org/libtiff/tiff-4.0.3.tar.gz
> 
> 14、libpng（gd库需要）
> 
> ftp://ftp.simplesystems.org/pub/png/src/libpng16/libpng-1.6.12.tar.gz
> 
> 15、freetype（gd库需要）
> 
> http://ring.u-toyama.ac.jp/archives/graphics/freetype/freetype2/freetype-2.5.3.tar.gz
> 
> 16、jpegsrc（gd库需要）
> 
> http://www.ijg.org/files/jpegsrc.v9a.tar.gz
> •	 
> Denniskevin
> #3 ⋅ 2年前
> 安装配置系统依赖
> 
> yum install -y apr* autoconf automake bison bzip2 bzip2* cloog-ppl compat* cpp curl curl-devel fontconfig fontconfig-devel 
> freetype freetype* freetype-devel gcc gcc-c++ gtk+-devel gd gettext gettext-devel glibc kernel kernel-headers keyutils 
> keyutils-libs-devel krb5-devel libcom_err-devel libpng libpng-devel libjpeg* libsepol-devel libselinux-devel libstdc++-devel 
> libtool* libgomp libxml2 libxml2-devel libXpm* libtiff libtiff* make mpfr ncurses* ntp openssl openssl-devel patch pcre-devel
>  perl php-common php-gd policycoreutils telnet t1lib t1lib* nasm nasm* wget zlib-devel
> 
> •	 
> ganto
> #4 ⋅ 2年前
> 赞
> •	 
> Denniskevin
> #5 ⋅ 2年前
> 
> 安装
> 
> 1、安装cmake
> 
> cd /usr/local/src
> 
> tar zxvf cmake-2.8.11.2.tar.gz
> 
> cd cmake-2.8.11.2
> 
> ./configure
> 
> make
> 
> make install
> 
> 安装MySQL
> 
> groupadd mysql #添加mysql组
> 
> useradd -g mysql mysql -s /bin/false #创建用户mysql并加入到mysql组，不允许mysql用户直接登录系统
> 
> mkdir -p /data/mysql #创建MySQL数据库存放目录
> 
> chown -R mysql:mysql /data/mysql #设置MySQL数据库存放目录权限
> 
> mkdir -p /usr/local/mysql #创建MySQL安装目录
> 
> cd /usr/local/src #进入软件包存放目录
> 
> tar zxvf mysql-5.6.19.tar.gz #解压
> 
> cd mysql-5.6.19 #进入目录
> 
> cmake . -DCMAKE_INSTALL_PREFIX=/usr/local/mysql -DMYSQL_DATADIR=/data/mysql -DSYSCONFDIR=/etc #配置
> 
> make #编译
> 
> make install #安装
> 
> rm -rf /etc/my.cnf #删除系统默认的配置文件（如果默认没有就不用删除）
> 
> cd /usr/local/mysql #进入MySQL安装目录
> 
> ./scripts/mysql_install_db --user=mysql --basedir=/usr/local/mysql --datadir=/data/mysql #生成mysql系统数据库
> 
> ln -s /usr/local/mysql/my.cnf /etc/my.cnf #添加到/etc目录的软连接
> 
> cp ./support-files/mysql.server /etc/rc.d/init.d/mysqld #把Mysql加入系统启动
> 
> chmod 755 /etc/init.d/mysqld #增加执行权限
> 
> chkconfig mysqld on #加入开机启动
> 
> vi /etc/rc.d/init.d/mysqld #编辑
> 
> basedir=/usr/local/mysql #MySQL程序安装路径
> 
> datadir=/data/mysql #MySQl数据库存放目录
> 
> :wq! #保存退出
> 
> •	 
> Denniskevin
> #6 ⋅ 2年前
> 
> 启动数据库!
> 
> service mysqld start #启动
> 
> vi /etc/profile #把mysql服务加入系统环境变量：在最后添加下面这一行
> 
> export PATH=$PATH:/usr/local/mysql/bin
> 
> :wq! #保存退出
> 
> source /etc/profile  #使配置立刻生效
> 
> 下面这两行把myslq的库文件链接到系统默认的位置，这样你在编译类似PHP等软件时可以不用指定mysql的库文件地址。
> 
> ln -s /usr/local/mysql/lib/mysql /usr/lib/mysql
> 
> ln -s /usr/local/mysql/include/mysql /usr/include/mysql
> 
> mkdir /var/lib/mysql #创建目录
> 
> ln -s /tmp/mysql.sock /var/lib/mysql/mysql.sock #添加软链接
> 
> mysql_secure_installation #设置Mysql密码，根据提示按Y 回车输入2次密码
> •	 
> Denniskevin
> #7 ⋅ 2年前
> 安装Nginx
> 
> 安装pcre
> 
> cd /usr/local/src
> 
> mkdir /usr/local/pcre
> 
> tar zxvf pcre-8.35.tar.gz
> 
> cd pcre-8.35
> 
> ./configure --prefix=/usr/local/pcre
> 
> make
> 
> make install
> 
> 安装openssl
> 
> cd /usr/local/src
> 
> mkdir /usr/local/openssl
> 
> tar zxvf openssl-1.0.1h.tar.gz
> 
> cd openssl-1.0.1h
> 
> ./config --prefix=/usr/local/openssl
> 
> make
> 
> make install
> 
> vi /etc/profile
> 
> export PATH=$PATH:/usr/local/openssl/bin
> 
> :wq!
> 
> source /etc/profile
> 安装zlib
> 
> cd /usr/local/src
> 
> mkdir /usr/local/zlib
> 
> tar zxvf zlib-1.2.8.tar.gz
> 
> cd zlib-1.2.8
> 
> ./configure --prefix=/usr/local/zlib
> 
> make
> 
> make install
> 
> 安装Nginx
> 
> groupadd www
> 
> useradd -g www www -s /bin/false
> 
> cd /usr/local/src
> 
> tar zxvf nginx-1.6.2.tar.gz
> 
> cd nginx-1.2.0
> 
> ./configure --prefix=/usr/local/nginx --without-http_memcached_module --user=www --group=www --with-http_stub_status_module --with-http_ssl_module --with-http_gzip_static_module --with-openssl=/usr/local/src/openssl-1.0.1h --with-zlib=/usr/local/src/zlib-1.2.8 --with-pcre=/usr/local/src/pcre-8.35
> 
> 注意：--with-openssl=/usr/local/src/openssl-1.0.1h --with-zlib=/usr/local/src/zlib-1.2.8 --with-pcre=/usr/local/src/pcre-8.35指向的是源码包解压的路径，而不是安装的路径，否则会报错
> •	 
> Denniskevin
> #8 ⋅ 2年前
> 
> make
> 
> make install
> 
> /usr/local/nginx/sbin/nginx #启动Nginx
> 
> 设置nginx开机启动
> 
> vi /etc/rc.d/init.d/nginx  #编辑启动文件添加下面内容
> 
> vi /etc/rc.d/init.d/nginx  #编辑启动文件添加下面内容
> 
> #!/bin/sh
> 
> #
> 
> # nginx - this script starts and stops the nginx daemon
> 
> #
> 
> # chkconfig: - 85 15
> 
> # description: Nginx is an HTTP(S) server, HTTP(S) reverse \
> 
> # proxy and IMAP/POP3 proxy server
> 
> # processname: nginx
> 
> # config: /etc/nginx/nginx.conf
> 
> # config: /usr/local/nginx/conf/nginx.conf
> 
> # pidfile: /usr/local/nginx/logs/nginx.pid
> 
> # Source function library.
> 
> . /etc/rc.d/init.d/functions
> 
> # Source networking configuration.
> 
> . /etc/sysconfig/network
> 
> # Check that networking is up.
> 
> [ "$NETWORKING" = "no" ] && exit 0
> 
> nginx="/usr/local/nginx/sbin/nginx"
> 
> prog=$(basename $nginx)
> 
> NGINX_CONF_FILE="/usr/local/nginx/conf/nginx.conf"
> 
> [ -f /etc/sysconfig/nginx ] && . /etc/sysconfig/nginx
> 
> lockfile=/var/lock/subsys/nginx
> 
> make_dirs() {
> 
> # make required directories
> 
> user=`$nginx -V 2>&1 | grep "configure arguments:" | sed 's/[^*]*--user=\([^ ]*\).*/\1/g' -`
> 
> if [ -z "`grep $user /etc/passwd`" ]; then
> 
> useradd -M -s /bin/nologin $user
> 
> fi
> 
> options=`$nginx -V 2>&1 | grep 'configure arguments:'`
> 
> for opt in $options; do
> 
> if [ `echo $opt | grep '.*-temp-path'` ]; then
> 
> value=`echo $opt | cut -d "=" -f 2`
> 
> if [ ! -d "$value" ]; then
> 
> # echo "creating" $value
> 
> mkdir -p $value && chown -R $user $value
> 
> fi
> 
> fi
> 
> done
> 
> }
> 
> start() {
> 
> [ -x $nginx ] || exit 5
> 
> [ -f $NGINX_CONF_FILE ] || exit 6
> 
> make_dirs
> 
> echo -n $"Starting $prog: "
> 
> daemon $nginx -c $NGINX_CONF_FILE
> 
> retval=$?
> 
> echo
> 
> [ $retval -eq 0 ] && touch $lockfile
> 
> return $retval
> 
> }
> 
> stop() {
> 
> echo -n $"Stopping $prog: "
> 
> killproc $prog -QUIT
> 
> retval=$?
> 
> echo
> 
> [ $retval -eq 0 ] && rm -f $lockfile
> 
> return $retval
> 
> }
> 
> restart() {
> 
> #configtest || return $?
> 
> stop
> 
> sleep 1
> 
> start
> 
> }
> 
> reload() {
> 
> #configtest || return $?
> 
> echo -n $"Reloading $prog: "
> 
> killproc $nginx -HUP
> 
> RETVAL=$?
> 
> echo
> 
> }
> 
> force_reload() {
> 
> restart
> 
> }
> 
> configtest() {
> 
> $nginx -t -c $NGINX_CONF_FILE
> 
> }
> 
> rh_status() {
> 
> status $prog
> 
> }
> 
> rh_status_q() {
> 
> rh_status >/dev/null 2>&1
> 
> }
> 
> case "$1" in
> 
> start)
> 
> rh_status_q && exit 0
> 
> $1
> 
> ;;
> 
> stop)
> 
> rh_status_q || exit 0
> 
> $1
> 
> ;;
> 
> restart|configtest)
> 
> $1
> 
> ;;
> 
> reload)
> 
> rh_status_q || exit 7
> 
> $1
> 
> ;;
> 
> force-reload)
> 
> force_reload
> 
> ;;
> 
> status)
> 
> rh_status
> 
> ;;
> 
> condrestart|try-restart)
> 
> rh_status_q || exit 0
> 
> ;;
> 
> *)
> 
> echo $"Usage: $0 {start|stop|status|restart|condrestart|try-restart|reload|force-reload|configtest}"
> 
> exit 2
> 
> esac
> 
> :wq! #保存退出
> 
> chmod 775 /etc/rc.d/init.d/nginx #赋予文件执行权限
> 
> chkconfig nginx on #设置开机启动
> 
> /etc/rc.d/init.d/nginx restart #重启
> •	 
> Denniskevin
> #9 ⋅ 2年前
> 安装PHP
> 
> 、安装php
> 
> 1、安装yasm
> 
> cd /usr/local/src
> 
> tar zxvf yasm-1.2.0.tar.gz
> 
> cd yasm-1.2.0
> 
> ./configure
> 
> make
> 
> make install
> 
> 安装libmcrypt
> 
> cd /usr/local/src
> 
> tar zxvf libmcrypt-2.5.8.tar.gz
> 
> cd libmcrypt-2.5.8
> 
> ./configure
> 
> make
> 
> make install
> 
> 安装libvpx
> 
> cd /usr/local/src
> 
> tar xvf libvpx-v1.3.0.tar.bz2
> 
> cd libvpx-v1.3.0
> 
> ./configure --prefix=/usr/local/libvpx --enable-shared --enable-vp9
> 
> make
> 
> make install
> 
> 安装tiff
> 
> cd /usr/local/src
> 
> tar zxvf tiff-4.0.3.tar.gz
> 
> cd tiff-4.0.3
> 
> ./configure --prefix=/usr/local/tiff --enable-shared
> 
> make
> 
> make install
> 
> 安装libpng
> 
> cd /usr/local/src
> 
> tar zxvf libpng-1.6.12.tar.gz
> 
> cd libpng-1.6.12
> 
> ./configure --prefix=/usr/local/libpng --enable-shared
> 
> make
> 
> make install
> 
> 安装freetype
> 
> cd /usr/local/src
> 
> tar zxvf freetype-2.5.3.tar.gz
> 
> cd freetype-2.5.3
> 
> ./configure --prefix=/usr/local/freetype --enable-shared
> 
> make #编译
> 
> make install #安装
> 
> 、安装jpeg
> 
> cd /usr/local/src
> 
> tar zxvf jpegsrc.v9a.tar.gz
> 
> cd jpeg-9a
> 
> ./configure --prefix=/usr/local/jpeg --enable-shared
> 
> make #编译
> 
> make install #安装
> 
> 安装libgd
> 
> cd /usr/local/src
> 
> tar zxvf libgd-2.1.0.tar.gz #解压
> 
> cd libgd-2.1.0 #进入目录
> 
> ./configure --prefix=/usr/local/libgd --enable-shared --with-jpeg=/usr/local/jpeg --with-png=/usr/local/libpng --with-freetype=/usr/local/freetype --with-fontconfig=/usr/local/freetype --with-xpm=/usr/ --with-tiff=/usr/local/tiff --with-vpx=/usr/local/libvpx #配置
> 
> make #编译
> 
> make install #安装
> 
> 安装t1lib
> 
> cd /usr/local/src
> 
> tar zxvf t1lib-5.1.2.tar.gz
> 
> cd t1lib-5.1.2
> 
> ./configure --prefix=/usr/local/t1lib --enable-shared
> 
> make without_doc
> 
> make install
> 
> 安装php
> 
> 注意：如果系统是64位，请执行以下两条命令，否则安装php会出错（32位系统不需要执行）
> 
> \cp -frp /usr/lib64/libltdl.so*  /usr/lib/
> 
> \cp -frp /usr/lib64/libXpm.so* /usr/lib/
> 
> cd /usr/local/src
> 
> tar -zvxf php-5.6.4.tar.gz
> 
> cd php-5.6.4
> 
> export LD_LIBRARY_PATH=/usr/local/libgd/lib
> 
> ./configure --prefix=/usr/local/php --with-config-file-path=/usr/local/php/etc --with-mysql=/usr/local/mysql --with-mysqli=/usr/local/mysql/bin/mysql_config --with-mysql-sock=/tmp/mysql.sock --with-pdo-mysql=/usr/local/mysql --with-gd --with-png-dir=/usr/local/libpng --with-jpeg-dir=/usr/local/jpeg --with-freetype-dir=/usr/local/freetype --with-xpm-dir=/usr/ --with-vpx-dir=/usr/local/libvpx/ --with-zlib-dir=/usr/local/zlib --with-t1lib=/usr/local/t1lib --with-iconv --enable-libxml --enable-xml --enable-bcmath --enable-shmop --enable-sysvsem --enable-inline-optimization --enable-opcache --enable-mbregex --enable-fpm --enable-mbstring --enable-ftp --enable-gd-native-ttf --with-openssl --enable-pcntl --enable-sockets --with-xmlrpc --enable-zip --enable-soap --without-pear --with-gettext --enable-session --with-mcrypt --with-curl --enable-ctype   #配置
> 
> make  #编译
> 
> make install   #安装
> 
> cp php.ini-production /usr/local/php/etc/php.ini  #复制php配置文件到安装目录
> 
> rm -rf /etc/php.ini  #删除系统自带配置文件
> 
> ln -s /usr/local/php/etc/php.ini /etc/php.ini   #添加软链接到 /etc目录
> 
> cp /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf  #拷贝模板文件为php-fpm配置文件
> 
> ln -s /usr/local/php/etc/php-fpm.conf /etc/php-fpm.conf  #添加软连接到 /etc目录
> 
> vi /usr/local/php/etc/php-fpm.conf #编辑
> 
> user = www #设置php-fpm运行账号为www
> 
> group = www #设置php-fpm运行组为www
> 
> pid = run/php-fpm.pid #取消前面的分号
> 
> :wq! #保存退出
> •	 
> Denniskevin
> #10 ⋅ 2年前
> 设置 php-fpm开机启动
> 
> cp /usr/local/src/php-5.6.4/sapi/fpm/init.d.php-fpm /etc/rc.d/init.d/php-fpm #拷贝php-fpm到启动目录
> 
> chmod +x /etc/rc.d/init.d/php-fpm #添加执行权限
> 
> chkconfig php-fpm on #设置开机启动
> 
> vi /usr/local/php/etc/php.ini #编辑配置文件
> 
> 找到：disable_functions =
> 
> 修改为：disable_functions = passthru,exec,system,chroot,scandir,chgrp,chown,shell_exec,proc_open,proc_get_status,ini_alter,ini_alter,ini_restore,dl,openlog,syslog,readlink,symlink,popepassthru,stream_socket_server,escapeshellcmd,dll,popen,disk_free_space,checkdnsrr,checkdnsrr,getservbyname,getservbyport,disk_total_space,posix_ctermid,posix_get_last_error,posix_getcwd, posix_getegid,posix_geteuid,posix_getgid, posix_getgrgid,posix_getgrnam,posix_getgroups,posix_getlogin,posix_getpgid,posix_getpgrp,posix_getpid, posix_getppid,posix_getpwnam,posix_getpwuid, posix_getrlimit, posix_getsid,posix_getuid,posix_isatty, posix_kill,posix_mkfifo,posix_setegid,posix_seteuid,posix_setgid, posix_setpgid,posix_setsid,posix_setuid,posix_strerror,posix_times,posix_ttyname,posix_uname
> 
> #列出PHP可以禁用的函数，如果某些程序需要用到这个函数，可以删除，取消禁用。
> 
> 找到：;date.timezone =
> 
> 修改为：date.timezone = PRC #设置时区
> 
> 找到：expose_php = On
> 
> 修改为：expose_php = Off #禁止显示php版本的信息
> 
> 找到：short_open_tag = Off
> 
> 修改为：short_open_tag = ON #支持php短标签
> 
> 找到opcache.enable=0
> 
> 修改为opcache.enable=1 #php支持opcode缓存
> 
> 找到：opcache.enable_cli=1 #php支持opcode缓存
> 
> 修改为：opcache.enable_cli=0
> 
> 在最后一行添加：zend_extension=opcache.so #开启opcode缓存功能
> 
> :wq! #保存退出
> 
> 配置nginx支持php
> 
> vi /usr/local/nginx/conf/nginx.conf
> 
> 修改/usr/local/nginx/conf/nginx.conf 配置文件,需做如下修改
> •	 
> Denniskevin
> #11 ⋅ 2年前
> 配置nginx支持php
> 
> vi /usr/local/nginx/conf/nginx.conf
> 
> 修改/usr/local/nginx/conf/nginx.conf 配置文件,需做如下修改
> 
> user www www; #首行user去掉注释,修改Nginx运行组为www www；必须与/usr/local/php/etc/php-fpm.conf中的user,group配置相同，否则php运行出错
> 
> index index.html index.htm index.php; #添加index.php
> 
> # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
> 
> #
> 
> location ~ \.php$ {
> 
> root html;
> 
> fastcgi_pass 127.0.0.1:9000;
> 
> fastcgi_index index.php;
> 
> fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
> 
> include fastcgi_params;
> 
> }
> 
> #取消FastCGI server部分location的注释,注意fastcgi_param行的参数,改为$document_root$fastcgi_script_name,或者使用绝对路径
> 
> /etc/init.d/nginx restart #重启nginx
> 
> service php-fpm start #启动php-fpm
> 
> 测试篇
> 
> cd /usr/local/nginx/html/ #进入nginx默认网站根目录
> 
> rm -rf /usr/local/nginx/html/* #删除默认测试页
> 
> vi index.php #新建index.php文件
> 
> <?php
> 
> phpinfo();
> 
> ?>
> 
> :wq! #保存退出
> 
> chown www.www /usr/local/nginx/html/ -R #设置目录所有者
> 
> chmod 700 /usr/local/nginx/html/ -R #设置目录权限
> •	 
> Denniskevin
> #12 ⋅ 2年前
> 安装HHVM
> 
> 参考facebook/hhvm
> 
> https://github.com/facebook/hhvm/wiki/Building-and-installing-hhvm-on-CentOS-7.x
> 
> hhvm
> 
> rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
> 
> -y install git mariadb-devel curl-devel expat-devel libpng-devel psmisc binutils-devel \
> boost-devel libmcrypt-devel libmemcached-devel jemalloc-devel libevent-devel sqlite-devel \
> libxslt-devel libicu-devel tbb-devel libzip-devel bzip2-devel openldap-devel readline-devel \
> elfutils-libelf-devel libdwarf-devel libcap-devel libyaml-devel libedit-devel lz4-devel \
> libvpx-devel unixODBC-devel libgmp-devel libpng-devel ImageMagick-devel curl-devel expat-devel
> 
> •	 
> Denniskevin
> #13 ⋅ 2年前
> cd /usr/local/src
> wget https://google-glog.googlecode.com/files/glog-0.3.3.tar.gz
> tar xvzf glog-0.3.3.tar.gz
> cd glog-0.3.3
> ./configure
> make && make install
> cd ..
> 
> wget http://www.geocities.jp/kosako3/oniguruma/archive/onig-5.9.5.tar.gz
> tar xvzf onig-5.9.5.tar.gz
> cd onig-5.9.5
> ./configure
> make && make install
> cd ..
> 
> git clone https://github.com/facebook/hhvm -b master  hhvm  --recursive
> cd hhvm
> ./configure
> 
> rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
> 
> yum -y remove ImageMagick
> yum -y install ImageMagick-last* --enablerepo=remi
> cmake -D LIBMAGICKWAND_INCLUDE_DIRS="/usr/include/ImageMagick-6" \
> -D LIBODBC_INCLUDE_DIRS="/usr/lib64" -D LIBODBC_LIBRARIES="/usr/lib64" \
> -D LIBVPX_INCLUDE_DIRS="/usr/lib64" -D LIBXSLT_INCLUDE_DIR="/usr/lib64" \
> -D LIBXSLT_LIBRARIES="/usr/lib64/libxslt.so"  -D LIBMAGICKWAND_LIBRARIES="/usr/lib64/libMagickWand-6.Q16.so" \
> -D LIBMAGICKCORE_LIBRARIES="/usr/lib64/libMagickCore-6.Q16.so" .
> 
> make
> make install
> 
> 查看HHVM
> 
> hhvm --version
> [root@localhost ~]# hhvm --version
> HipHop VM 3.5.0-dev (rel)
> Compiler: heads/master-0-g0098244a6f5f2e4056687c08860c13350dfda882
> Repo schema: fe7404f1687eeddaa1ca5ae7c51d47737fbff594
> 
> •	 
> Denniskevin
> #14 ⋅ 2年前
> 配置hhvm
> mkdir /etc/hhvm /var/run/hhvm /var/log/hhvm
> chown -R www.www /var/run/hhvm /var/log/hhvm
> 
> vi /usr/local/nginx/conf/nginx.conf
> 
> location ~ .*\.(php|php5)?$  {
> fastcgi_pass   unix:/var/run/hhvm/sock;
> fastcgi_index  index.php;
> fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;
> includefastcgi_params;
> }
> 
> 启动
> service nginx reload
> 
> •	 
> Denniskevin
> #15 ⋅ 2年前
> hhvm配置
> 
> vi /etc/hhvm/config.hdf
> ResourceLimit { CoreFileSize = 0 # in bytes MaxSocket = 10000 # must be not 0, otherwise HHVM will not start SocketDefaultTimeout = 5 # in seconds MaxRSS = 0 MaxRSSPollingCycle = 0 # in seconds, how often to check max memory DropCacheCycle = 0 # in seconds, how often to drop disk cache }
> Log { Level = Info AlwaysLogUnhandledExceptions = true RuntimeErrorReportingLevel = 8191 UseLogFile = true UseSyslog = false File = /var/log/hhvm/error.log Access { * { File = /var/log/hhvm/access.log Format = %h %l %u % t \"%r\" %>s %b } } }
> MySQL { ReadOnly = false ConnectTimeout = 1000 # in ms ReadTimeout = 1000 # in ms SlowQueryThreshold = 1000 # in ms, log slow queries as errors KillOnTimeout = false }
> Mail { SendmailPath = /usr/sbin/sendmail -t -i ForceExtraParameters = }
> •	 
> shench
> 
> #16 ⋅ 2年前
> 这个要顶！
> •	 
> Denniskevin
> #17 ⋅ 2年前
> vi /etc/hhvm/server.ini
> 
> ; php options
> pid = /var/run/hhvm/pid
> 
> ; hhvm specific
> ;hhvm.server.port = 9001
> hhvm.server.file_socket = /var/run/hhvm/sock
> hhvm.server.type = fastcgi
> hhvm.server.default_document = index.php
> hhvm.log.use_log_file = true
> hhvm.log.file = /var/log/hhvm/error.log
> hhvm.repo.central.path = /var/run/hhvm/hhvm.hhbc
> 
> vi /etc/hhvm/php.ini指定mysql.sock路径（hhvm默认路径sock路径是/var/lib/mysql/mysql.sock）
> 
> hhvm.mysql.socket = /tmp/mysql.sock
> expose_php = 0 ;关闭头信息X-Powered-By (和hhvm.server.expose_hphp = false作用一样)
> memory_limit = 400M
> post_max_size = 50M 
> 
> •	 
> Denniskevin
> #18 ⋅ 2年前
> 设置开机自启动
> vi /etc/systemd/system/hhvm.service
> 
> [Unit]
> Description=HHVM HipHop Virtual Machine (FCGI)
> 
> [Service]
> ExecStart=/usr/local/bin/hhvm --mode daemon --user www --config /etc/hhvm/server.ini \
> --config /etc/hhvm/php.ini --config /etc/hhvm/config.hdf
> 
> [Install]
> WantedBy=multi-user.target
> 
> •	 
> Denniskevin
> #19 ⋅ 2年前
> HHVM 服务信息
> 
> systemctl enable hhvm #开机自启动
> systemctl start hhvm #启动hhvm
> systemctl status hhvm #查看hhvm状态
> 
> •	 
> Denniskevin
> #20 ⋅ 2年前
> wget http://www.geocities.jp/kosako3/oniguruma/archive/onig-5.9.5.tar.gz
> 
> wget http://www.geocities.jp/kosako3/oniguruma/archive/onig-5.9.5.tar.gz
> 
> 下载这两个要那什么 大家都懂哈!
> 
> 