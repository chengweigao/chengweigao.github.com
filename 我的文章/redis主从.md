主Redis：192.168.10.1 6379
从redis：192.168.10.2 6380
一、主从配置
1、将主从redis配置文件redis.conf中的aemonize no 改为 yes
2、修改从redis配置文件redis.conf中的port 6379 改为 6380，添加slaveof 192.168.10.1 6379 
3、启动主从服务

      主redis：      
      [root@localhost redis-2.8.3]# src/redis-server /soft/redis-2.8.3-master/redis-2.8.3/redis.conf
     从redis：
     [root@localhost redis-2.8.3]# src/redis-server /soft/redis-2.8.3-slave/redis-2.8.3/redis.conf
4、测试数据同步

      主redis：
      [root@localhost redis-2.8.3]# src/redis-cli -p 6379
     127.0.0.1:6379> set name abc
     OK
     127.0.0.1:6379> get name
     "abc"
     127.0.0.1:6379>
    从redis：
      [root@localhost redis-2.8.3]# src/redis-cli -p 6380
     127.0.0.1:6380> get name
     "abc"
     127.0.0.1:6380>
5、默认是读写分离的

     在从redis：
     [root@localhost redis-2.8.3]# src/redis-cli -p 6380
     127.0.0.1:6380> set name 123
     (error) READONLY You can't write against a read only slave.
      
 二、主从切换

     1、停止主redis
     [root@localhost redis-2.8.3]# src/redis-cli -n 6379 shutdown
     [root@localhost redis-2.8.3]# src/redis-cli -p 6379
     Could not connect to Redis at 127.0.0.1:6379: Connection refused
     not connected>
     2、将从redis设成主redis
     [root@localhost redis-2.8.3]# src/redis-cli -p 6380 slaveof NO ONE
     OK
    3、测试从redis是否切换从主redis
     [root@localhost redis-2.8.3]# src/redis-cli -p 6380
     127.0.0.1:6380> set name 123
     OK
     127.0.0.1:6380> get name
     "123"
     127.0.0.1:6380>
     4、原来的主redis恢复正常了，要重新切换回去
         1）将现在的主redis的数据进行保存
     [root@localhost redis-2.8.3]# src/redis-cli -p 6380
     127.0.0.1:6380> get name
     "abc"
     127.0.0.1:6380> set name 123
     OK
     127.0.0.1:6380> get name
     "123"
     127.0.0.1:6380> save
     OK
     127.0.0.1:6380> get name
     "123"
     127.0.0.1:6380>  
       2）将现在的主redis根目录下dump.rdb文件拷贝覆盖到原来主redis的根目录
       3）启动原来的主redis
      [root@localhost redis-2.8.3]# src/redis-server /soft/redis-2.8.3-master/redis-2.8.3/redis.conf
       4）在现在的主redis中切换
      [root@localhost redis-2.8.3]# src/redis-cli -p 6380 slaveof 192.168.10.1 6379
      OK
