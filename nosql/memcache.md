Memcache     php扩展安装 加个Memcache缓存。
一开始yum安装，因为PHP版本比较高。
而默认的二进制版memcache是由低版本编译的，所以就造成 Class ‘Memcache’not found的错误。
依赖Gcc c++
> sudo yum install gcc-c++

安装依赖Libevent事件触发管理器。
>  wget https://github.com/downloads/libevent/libevent/libevent-2.0.21-stable.tar.gz
>  
> tar vxf libevent-2.0.21-stable.tar.gz
> 
> cd libevent-2.0.21-stable
> 
> ./configure -prefix=/usr/local/libevent    # ./configure
> 
> make && make install
> 
> yum install libevent-devel


安装memcache

>  
>  wget https://github.com/websupport-sk/pecl-memcache/archive/php7.zip 
>  
>  unzip php7.zip 
>  
>  cd  pecl-memcache-php7
>  
>  phpize
>  
>  ./configure --with-php-config=/usr/local/php/bin/php-config
>  
>  make && make install

在php.ini的最下面添加
> [memcache]
> 
> extension_dir = "/usr/local/php70/lib/php/extensions/no-debug-non-zts-20151012/"
> 
> extension = "memcache.so"

安装memcached 3.0.3扩展
需要依赖libmemcached
    
       wget https://launchpadlibrarian.net/165454254/libmemcached-1.0.18.tar.gz	
       tar -zxvf libmemcached-1.0.18.tar.gz 
       cd libmemcached-1.0.18/
       ./configure --prefix=/usr/local/libmemcached  
       make 
       make & make install
    
    
       wget http://pecl.php.net/get/memcached-3.0.3.tgz
       cd memcached-3.0.3/
       ./configure 
       ./configure  --with-libmemcached-dir=/usr/local/libmemcached
       make insatll
       make install
在php.ini的最下面添加
> [memcached]
> 
> extension_dir = "/usr/local/php70/lib/php/extensions/no-debug-non-zts-20151012/"

> extension = "memcached.so"





编译安装Memcached
> wget http://memcached.org/files/memcached-1.4.25.tar.gz
> 
> tar vxf memcached-1.4.25.tar.gz
> 
> cd memcached-1.4.25
> 
> ./configure -with-libevent=/usr/local/libevent   # ./configure
> 
> make && make install

启动Memcache
>  /usr/local/bin/memcached -d -m 128 -l 127.0.0.1 -p 11211 -u root   # (128为内存, 11211为端口,root为用户组)

验证启动：
ps aux|grep memcached


重启php-fpm ，重新加载nginx
> pkill php-fpm
> 
>/usr/local/php/sbin/php-fpm 
>
>/usr/local/src/nginx/sbin/nginx -s reload

浏览器访问test.php,文件内容，检测是否整合php

	<?php
    $mem = new memcache;
    $mem->connect('localhost', 11211);
    $mem->set('key', 'cbam_liangshu!');
    $val = $mem->get('key');
    echo $val;
    ?>

安装完成，此时可以通过telnet 连接memcache服务器并 通过stats命令查看Memcache的工作状态。
> telnet localhost 11211

刷新缓存
> flush_all
