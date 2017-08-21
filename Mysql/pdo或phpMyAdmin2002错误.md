php  pdo  mysql错误
=======

#2002 - No such file or directory & mdash; 
是因为php没有指定对应的mysql.sock

> Mysql有两种连接方式： 
> （1），TCP/IP 
> （2），socket 
> 对mysql.sock来说，其作用是程序与mysqlserver处于同一台机器，发起本地连接时可用。 
> 例如你无须定义连接host的具体IP地址，只要为空或localhost就可以。 
> 在此种情况下，即使你改变mysql的外部port也是一样可能正常连接。 
> 因为你在my.ini中或my.cnf中改变端口后，mysql.sock是随每一次 mysql server启动生成的。已经根据你在更改完my.cnf后重启mysql时重新生成了一次，信息已跟着变更。 
> 那么对于外部连接，必须是要变更port才能连接的。 
> linux下安装mysql连接的时候经常回提示说找不到mysql.sock文件，解决办法很简单： 
> 如果是新安装的mysql，提示找不到文件，就搜索下，指定正确的位置。 
> 如果mysql.sock文件误删的话，就需要重启mysql服务，如果重启成功的话会在datadir目录下面生成mysql.sock 到时候指定即可。
 
首先查看mysql.sock在那个位置

       
    >  find / -name mysql.sock
    
找到对应的位置后到php.ini填写上对应的 ${path}是你的.sock路径

     mysql.default_socket = /${path}/mysql.sock
