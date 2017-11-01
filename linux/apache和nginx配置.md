#apache的vhost配置
	

	#ip端口的绑定
    <VirtualHost 172.20.30.50:80>
		#站长邮箱
	    ServerAdmin webmaster@www2.example.org
		#站点目录	    
		DocumentRoot "/www/vhosts/www2"
	    #域名
		ServerName www2.example.org
	    #错误日志	
		ErrorLog "/www/logs/www2/error_log"
		#请求日志	    
		CustomLog "/www/logs/www2/access_log" combined
    </VirtualHost>
#nginx 的分发

	#添加upstream节点。
		upstream apachephp  {
	
	    server 192.168.1.229:8080; #Apache
	}
	 
	##设定地址##
	server {
	    listen 80;
		
	    server_name  192.168.1.229;
	 
	   # access_log  logs/quancha.access.log  main;
	   # error_log  logs/quancha.error.log;
	    root   html;
	    index  index.html index.htm index.php;
	 
	    ## send request back to apache ##
	    location / {
	        proxy_pass  http://apachephp;
	 
	        #Proxy Settings
	        proxy_redirect     off;
	        proxy_set_header   Host             $host;
	        proxy_set_header   X-Real-IP        $remote_addr;
	        proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
	        proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
	        proxy_max_temp_file_size 0;
	        proxy_connect_timeout      90;
	        proxy_send_timeout         90;
	        proxy_read_timeout         90;
	        proxy_buffer_size          4k;
	        proxy_buffers              4 32k;
	        proxy_busy_buffers_size    64k;
	        proxy_temp_file_write_size 64k;
	   }
	}