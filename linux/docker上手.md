#1、Docker介绍
Docker是一个开源的应用容器引擎，让开发者可以打包他们的应用以及以来到一个可移植的容器中，然后发布到任何流行的linux机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口。几乎没有性能开销，可以很容易的在机器和数据中心中运行。最重要的是他们不依赖任何与语言、框架和系统。这个貌似比vagrant牛叉点 

#2、Docker安装
	yum install docker-io
	#启动docker

	systemctl start docker
	#如果在启动过程中出现如下告警

	Usage of loopback devices is strongly discouraged for production use. Either use `--	storage-opt dm.thinpooldev` or use `--storage-opt dm.no_warn_on_loop_devices=true`

	#设置/etc/sysconfig/docker-storage

	vim /etc/sysconfig/docker-storage

	 DOCKER_STORAGE_OPTIONS="--storage-opt dm.no_warn_on_loop_devices=true"

	#重启docker

	systemctl start docker

	#下载官方的Centos镜像到本地

	docker pull centos:latest

	#查看镜像是否安装成功

	docker images centos

	#运行一个docker容器

	docker run -i -t centos /bin/bash