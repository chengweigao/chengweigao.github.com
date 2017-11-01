

.htaccess文件简洁路径

	# 为了正常启用URL Rewrite，请将apache配置文件中“LoadModule rewrite_module modules/mod_rewrite.so”
	# 前的注释去掉，并将apache的DocumentRoot开启AllowOverride
 
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