   
	svnadmin create xxxx目录

	进入xxxx/conf目录（该svn版本库配置文件）
	
		1authz文件是权限控制文件
			[/]
		
			dan=rw
			
			w=r
			
			意思是版本库的根目录dan对其有读写权限，w只有读权限。
	
		passwd是帐号密码文件
	
			在[users]块中添加用户和密码，格式：帐号=密码
	
		svnserve.conf SVN服务配置文件
			打开下面的几个注释：

			anon-access = read #匿名用户可读
			
			auth-access = write #授权用户可写
			
			password-db = passwd #使用哪个文件作为账号文件
			
			authz-db = authz #使用哪个文件作为权限文件
			
			realm = xxxx(目录)   #认证空间名，版本库所在目录
	启动svn服务
	svnserve -d -r xxxx

	svnserve -d -r 目录 --listen-port 端口号
	-r: 配置方式决定了版本库访问方式。
	
	--listen-port: 指定SVN监听端口，不加此参数，SVN默认监听3690
	
	由于-r 配置方式的不一样，SVN启动就可以有两种不同的访问方式
	
	方式一：-r直接指定到版本库(称之为单库svnserve方式)


[http://www.runoob.com/svn/svn-start-mode.html](http://www.runoob.com/svn/svn-start-mode.html "菜鸟手册")