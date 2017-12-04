线上项目apk安装包  在别的浏览器都没问题 唯独到了百度浏览器   莫名其妙的变成了文件名.txt
一脸懵逼的我只好百度原因   解决方案如下


	在mime.types添加如下两句
	application/vnd.android.package-archive                    apk
	application/vnd.webos.ipk                    ipk	