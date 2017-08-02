1.当我们备份数据时，从其它库拷过来的.sql脚本，这个sql脚本是全部备份的。

这时如果两个数据库版本不一样，就会出现不能登录等问题，这时我们唯有初始化。其关键问题在全备时mysql库发生变化，造成密码等错误。

-----解决方法：

      如果安装是二进制版本的：

   # rm -rf 数据库data文件夹

  #  cd mysql/bin

 # mysqld --initialize --user=mysql      --mysql5.7版本初始化

# bin/mysql_install_db --user=mysql       --5.6到5.7版本 

这时页面最下方会出现初始化后的密码，然后我们登录数据库输入刚才记录的密码。

mysql>alter user 'root'@'localhost' identified by '新密码';

方法1： 用SET PASSWORD命令 
首先登录MySQL。 
格式：mysql> set password for 用户名@localhost = password('新密码'); 
例子：mysql> set password for root@localhost = password('123'); 

方法2：用mysqladmin 
格式：mysqladmin -u用户名 -p旧密码 password 新密码 
例子：mysqladmin -uroot -p123456 password 123 

方法3：用UPDATE直接编辑user表 
首先登录MySQL。 
mysql> use mysql; 
mysql> update user set password=password('123') where user='root' and host='localhost'; 
mysql> flush privileges; 

方法4：在忘记root密码的时候，可以这样 
以windows为例： 
1. 关闭正在运行的MySQL服务。 
2. 打开DOS窗口，转到mysql\bin目录。 
3. 输入mysqld --skip-grant-tables 回车。--skip-grant-tables 的意思是启动MySQL服务的时候跳过权限表认证。 
4. 再开一个DOS窗口（因为刚才那个DOS窗口已经不能动了），转到mysql\bin目录。 
5. 输入mysql回车，如果成功，将出现MySQL提示符 >。 
6. 连接权限数据库： use mysql; 。 
6. 改密码：update user set password=password("123") where user="root";（别忘了最后加分号） 。 
7. 刷新权限（必须步骤）：flush privileges;　。 
8. 退出 quit。 
9. 注销系统，再进入，使用用户名root和刚才设置的新密码123登录