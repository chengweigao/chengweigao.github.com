.htaccess文件简洁路径

	#把url里的zhifangranshao   替换成/n/zhifangranshao/
	Redirect permanent /zhifangranshao/  /n/zhifangranshao/
	<IfModule expires_module>
    #打开缓存
	     ExpiresActive on
	#文件缓存864000/3600/24=10天
	     ExpiresByType text/css A3600
	     ExpiresByType application/x-JavaScript A3600
	     ExpiresByType application/javascript A3600
	     ExpiresByType text/html A3600
	     ExpiresByType image/jpeg A3600
	     ExpiresByType image/gif A3600
	     ExpiresByType image/png A3600
	     ExpiresByType image/x-icon A3600
	</IfModule>