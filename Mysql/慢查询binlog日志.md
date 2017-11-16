    mysql 开启二进制日志

    编辑/etc/my.cnf 数据库配置项
	log-bin=mysql-bin
    重启mysql  登陆mysql执行
	mysql> show variables like '%log_bin%';
	+---------------------------------+-------+
	| Variable_name                   | Value |
	+---------------------------------+-------+
	| log_bin                         | ON    |
	| log_bin_trust_function_creators | OFF   |
	| sql_log_bin                     | ON    |
	+---------------------------------+-------+
    去到 /var/lib/mysql   数据库文件目录 binlog已存在
	将日志导出到a.log慢慢查阅处理
	./mysqlbinlog --start-datetime="开始时间" --stop-datetime="结束时间" mysql-bin.000001 > a.log
	恢复
	mysqlbinlog e:/log/logbin.000001 | mysql -u root -p 
	指定恢复
	mysqlbinlog --start-datetime="2010-01-07 11:25:56" --stop-datetime="2010-01-07 13:23:50" mysql-bin.000001 | mysql -u root -p 
    查看是否开启慢查询日志
	mysql> show variables like 'slow%';
    +---------------------+-----------------------------+
	| Variable_name       | Value                       |
	+---------------------+-----------------------------+
	| slow_launch_time    | 2                           |
	| slow_query_log      | OFF                          |
	| slow_query_log_file | /var/lib/mysql/www-slow.log |
	+---------------------+-----------------------------+
	没有开启
	开启
    set slow_query_log='yes'
	设置查询超时标准 1秒
	set long_query_time=1;




