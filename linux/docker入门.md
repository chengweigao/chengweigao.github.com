#Docker误区+技巧+转换关系
 

##1. 误区：容器重启或者机器重启会丢失容器内的数据

根据https://docs.docker.com/faq/上的问答和本人的实践，在docker容器内创建文件和安装软件，做下面的操作都不会丢失数据和软件：
#A. exit
sudo docker start b430d6f4ff00

#B. sudo docker stop b430d6f4ff00
sudo docker start b430d6f4ff00

#C. reboot host

https://docs.docker.com/faq/
Do I lose my data when the container exits?
Not at all! Any data that your application writes to disk gets preserved in its container until you explicitly delete the container. The file system for the container persists even after the container halts.

 

##2. 如何进入或者退出docker容器？以及如何在主机上对正在运行的容器执行命令？

除了之前介绍的用nsenter:http://blog.csdn.net/yangzhenping/article/details/42297205


还可以使用attach选项：

	sudo docker run --name ubuntu_bash -i -t ubuntu:latest /bin/bash
	sudo docker ps -l
	sudo docker attach b430d6f4ff00


如何退出容器而不停止容器？
组合键：Ctrl+P+Q

另外，如果想对容器执行命令，可以使用exec选项：

	$ sudo docker exec -d ubuntu_bash touch /tmp/execWorks

容器中以后台进程运行touch /tmp/execWorks命令（就是在/tmp目录下创建一个新的文件execWorks）

 

另外有人想直接用ssh去连接上容器的想法，虽然可以，但是有很多弊端，而且docker已经提供了容器内执行的命令，没有必要再折腾每一个容器为sshd服务器
具体为什么不使用，可以看下这篇文章：http://jpetazzo.github.io/2014/06/23/docker-ssh-considered-evil/

 

## 关于几个容器和镜像以及文件的转化关系：

参考：http://tuhrig.de/difference-between-save-and-export-in-docker/

 

容器转成镜像：

	sudo docker commit <CONTAINER ID> imagename01

容器转成文件：

	sudo docker export <CONTAINER ID> > /home/export.tar

镜像转成文件：

	sudo docker save imagename01 > /home/save.tar

注：一般情况下，save.tar比export.tar大一点点而已，export比较小，因为它丢失了历史和数据元metadata
 
		注：这里我们要注意几点问题： 
	1：start 和run的区别 
	run是根据现存的镜像启动一个新的容器，而start是开始一个停止的容器，即退出时是使用exit或者stop的 
	2：commit和save 
	这个意思就是每次对容器做一些修改之后，我们需要先提交到本地库，然后save成tar包以供其他使用，若不进行commit直接save的话，正在对容器所做的改变则不能save下来 
	3：export和save的区别 
	两者都是导出镜像为tar形式，但是export导出的文件要比save保存的小，原因是export导出的会丢失一些log信息和镜像的层信息，具体可参考： 

文件转成镜像：

	cat /home/export.tar | sudo docker import - imagename02:latest

save.tar文件转成镜像：

	docker load < /home/save.tar
	
		
查看转成的镜像：
	sudo docker images

注意：这里一个镜像经过n次转化之后，可以用sudo docker images --tree查看历史，用docker tag <LAYER ID> <IMAGE NAME>你可以回到某个层（只针对save命令可以回到某个层！）


<div class="markdown_views"><p></p><div class="toc">

<p></p>



<h1 id="docker安装"><a name="t0"></a>docker安装</h1>



<h2 id="linux下的安装"><a name="t1"></a>linux下的安装</h2>

<ol>
<li>系统：CentOS7.x</li>
<li><p>内核:3.10及以上的kernel内核版本 <br>
可以通过uname -r查看</p>

<blockquote>
  <p>$ uname -r</p>
</blockquote></li>
<li><p>安装:</p>

<blockquote>
  <p>两种安装方式</p>
  
  <ol><li>yum安装 <br>
  1.更新yum包 <br>
  <span>$</span> sudo yum update <br>
  2.添加yum仓库 <br>
  <span>$</span> sudo tee /etc/yum.repos.d/docker.repo &lt;&lt;-‘EOF’ <br>
  [dockerrepo] <br>
  name=Docker Repository <br>
  baseurl=<a href="https://yum.dockerproject.org/repo/main/centos/7/" target="_blank">https://yum.dockerproject.org/repo/main/centos/7/</a> <br>
  enabled=1 <br>
  gpgcheck=1 <br>
  gpgkey=<a href="https://yum.dockerproject.org/gpg" target="_blank">https://yum.dockerproject.org/gpg</a> <br>
  EOF <br>
  3.安装docker包 <br>
  <span>$</span> sudo yum install docker-engine <br>
  4.运行docker后台进程 <br>
  <span>$</span> sudo service docker start <br>
  5.检测docker是否正确安装 <br>
  <span>$</span> sudo docker run hello-world</li>
  <li>脚本安装 <br>
  1.更新yum包 <br>
  <span>$</span> sudo yum update <br>
  2.运行docker安装脚本 <br>
  <span>$</span> curl -fsSL <a href="https://get.docker.com/" target="_blank">https://get.docker.com/</a> | sh <br>
  3.运行docker后台进程 <br>
  <span>$</span> sudo service docker start <br>
  4.检测docker是否正确安装 <br>
  <span>$</span> sudo docker run hello-world</li></ol>
</blockquote></li>
</ol>



<h2 id="windows下的安装"><a name="t2"></a>windows下的安装</h2>

<ol>
<li>系统：window10个人版或者64位企业版</li>
<li><p>软件下载地址</p>

<blockquote>
  <p>docker下载地址:<a href="http://www.docker.com/products/docker#/windows" target="_blank">http://www.docker.com/products/docker#/windows</a> <br>
  toolbox下载地址<a href="http://www.docker.com/products/docker-toolbox" target="_blank">http://www.docker.com/products/docker-toolbox</a></p>
</blockquote></li>
<li><p>安装:</p>

<blockquote>
  <p>1.双击InstallDocker.msi来运行docker安装程序,一直点击完成即可 <br>
  如果没有InstallDocker.msi文件可以在<a href="https://download.docker.com/win/stable/InstallDocker.msi" target="_blank">这里</a>获取 <br>
  2.启动docker <br>
  通过docker quick start terminal启动</p>
</blockquote></li>
</ol>



<h1 id="docker仓库"><a name="t3"></a>docker仓库</h1>



<h2 id="仓库服务器"><a name="t4"></a>仓库服务器</h2>

<p>拉下官方的registry镜像,并启动镜像</p>



<pre class="prettyprint" name="code"><code class="hljs ruby has-numbering"><span class="hljs-variable">$ </span>docker pull registry
<span class="hljs-variable">$ </span>docker run -d -p <span class="hljs-number">5000</span><span class="hljs-symbol">:</span><span class="hljs-number">5000</span> registry</code><ul class="pre-numbering" style=""></ul></pre>



<h2 id="docker客户端"><a name="t5"></a>docker客户端</h2>

<p>1.修改docker配置文件如下</p>



<pre class="prettyprint" name="code"><code class="language-shell hljs cs has-numbering">$ vi /<span class="hljs-keyword">var</span>/lib/boot2docker/profile</code><ul class="pre-numbering" style=""></ul></pre>

<p>添加–insecure-registry 192.168.1.26:5000 <br>
<img src="http://img.blog.csdn.net/20160830123949872" alt="这里写图片描述" title=""></p>

<p>2.重启docker服务</p>



<pre class="prettyprint" name="code"><code class="hljs ruby has-numbering"><span class="hljs-variable">$ </span>/etc/init.d/docker restart</code><ul class="pre-numbering" style=""><li>1</li></ul></pre>

<p>3.修改要提交镜像名称 <br>
如果本次仓库服务器ip和端口号分别为192.168.1.8:5000 <br>
则镜像名修改命令如下</p>



<pre class="prettyprint" name="code"><code class="hljs ruby has-numbering"><span class="hljs-variable">$ </span>docker tag <span class="hljs-symbol">test:</span>latest  <span class="hljs-number">192.168</span>.<span class="hljs-number">1.8</span><span class="hljs-symbol">:</span><span class="hljs-number">5000</span>/<span class="hljs-symbol">znms:</span>v1
<span class="hljs-variable">$ </span>docker push <span class="hljs-number">192.168</span>.<span class="hljs-number">1.8</span><span class="hljs-symbol">:</span><span class="hljs-number">5000</span>/<span class="hljs-symbol">znms:</span>v1</code></pre>

<p>下载仓库镜像</p>



<pre class="prettyprint" name="code"><code class="hljs ruby has-numbering"><span class="hljs-variable">$ </span>docker pull <span class="hljs-number">192.168</span>.<span class="hljs-number">1.8</span><span class="hljs-symbol">:</span><span class="hljs-number">5000</span>/<span class="hljs-symbol">znms:</span>v1</code></pre>



<h1 id="制作docker镜像"><a name="t6"></a>制作docker镜像</h1>



<h2 id="通过容器制作docker镜像"><a name="t7"></a>通过容器制作docker镜像</h2>



<pre class="prettyprint" name="code"><code class="hljs ruby has-numbering"><span class="hljs-variable">$ </span>docker commit 容器id 镜像名称</code></pre>



<h2 id="通过dockerfile制作docker镜像"><a name="t8"></a>通过Dockerfile制作docker镜像</h2>



<h3 id="编写dockerfile文件"><a name="t9"></a>编写Dockerfile文件</h3>



<pre class="prettyprint" name="code"><code class="hljs ruby has-numbering"><span class="hljs-variable">$ </span>vim <span class="hljs-constant">Dockerfile</span></code></pre>

<p>文件内容如下</p>



<pre class="prettyprint" name="code"><code class="hljs avrasm has-numbering">FROM znms:v1                            <span class="hljs-preprocessor">#制作镜像所需的基础镜像</span>
MAINTAINER <span class="hljs-string">"zhenping"</span> &lt;weizp@zznet<span class="hljs-preprocessor">.cn</span>&gt;  <span class="hljs-preprocessor">#维护者名称</span>
WORKDIR /root                           <span class="hljs-preprocessor">#切换工作目录为root</span>
<span class="hljs-keyword">ADD</span> init<span class="hljs-preprocessor">.sh</span> /root/                      <span class="hljs-preprocessor">#把宿主机当前目录下的</span>
                                        <span class="hljs-preprocessor">#init.sh文件添加到镜像的</span>
                                        <span class="hljs-preprocessor">#root目录中</span>
EXPOSE <span class="hljs-number">80</span>                               <span class="hljs-preprocessor">#暴露端口</span>
EXPOSE <span class="hljs-number">3306</span>
EXPOSE <span class="hljs-number">514</span>
EXPOSE <span class="hljs-number">69</span>
EXPOSE <span class="hljs-number">22</span>
EXPOSE <span class="hljs-number">23</span>
ENV LANG en_US<span class="hljs-preprocessor">.UTF</span>-<span class="hljs-number">8</span>                    <span class="hljs-preprocessor">#修改镜像环境变量</span>
VOLUME /var/www/html/cacti              <span class="hljs-preprocessor">#添加对外的挂载目录</span>
CMD [<span class="hljs-string">"sh"</span>,<span class="hljs-string">"init.sh"</span>]                    <span class="hljs-preprocessor">#镜像每次启动时都会执行</span>
                                        <span class="hljs-preprocessor">#init.sh脚本</span></code></pre>



<h3 id="编写initsh启动脚本"><a name="t10"></a>编写init.sh启动脚本</h3>



<pre class="prettyprint" name="code"><code class="hljs ruby has-numbering"><span class="hljs-variable">$ </span>vim init.sh</code></pre>

<p>init.sh脚本内容如下(下面是目前znms需要开机启动的服务)：</p>



<pre class="prettyprint" name="code"><code class="hljs bash has-numbering"><span class="hljs-shebang">#!/bin/bash</span>
service crond start
service snmpd start
service mysqld start
<span class="hljs-comment">#sed是为了让容器启动时候根据环境变量中的REMOTE_HOST来配置php调试服务</span>
sed -i <span class="hljs-string">'2000c xdebug.remote_host='</span><span class="hljs-variable">$REMOTE_HOST</span><span class="hljs-string">''</span> /usr/local/php5/etc/php.ini
service php-fpm start
service httpd start
service rsyslog start
service xinetd start
service sshd start
<span class="hljs-comment">#tailf命令是为了让容器一直有任务执行,否则容器会stop</span>
tailf /var/www/log/error.log
</code></pre>



<h1 id="docker常用命令"><a name="t11"></a>docker常用命令</h1>

    attach：   进入到正在运行的容器
    build：从Dockerfile构建镜像
    commit：   容器更改之后创建新镜像
    cp：   在容器和本地之间拷贝文件和文件夹
    create：   创建一个新的容器
    diff： 检查容器文件系统上的更改
    events：   从服务器上获取实时事件
    exec： 在正在运行的容器中运行命令
    export：   将容器的文件系统导出为tar存档
    history：  显示镜像的历史记录
    images：   列出镜像
    import：   从tar包导入创建新的文件系统镜像
    info： 显示系统范围的信息
    inspect：  返回容器，映像或任务的低级信息
    kill： 杀死一个或者多个正在运行的容器
    load： 加载一个打包好的镜像
    login：登录到docker的服务
    logout：   退出docker服务
    logs： 获取容器的日志
    network：  管理docker的网络
    node： 管理docker swarm节点
    pause：暂停一个或多个容器中的进程
    port： 列出端口映射或者容器的特定映射
    ps：   列出正在运行的容器（ps -a 列出正在运行和已经停止的容器）
    pull： 从注册表中加载一个镜像
    push： 将镜像提交到注册表中
    rename：   重命名容器
    restart：  重新启动容器
    rm：   删除一个或者多个容器
    rmi：  删除一个或者多个容器
    run：  在容器中运行命令
    save： 将镜像保存成tar文件
    search：   在docker 仓库中搜索镜像
    service：  管理镜像服务
    start：启动一个或者多个已经停止的容器
    stats：显示容器资源使用的实时信息流
    stop： 停止一个或者多个正在运行的容器
    swarm：管理docker swarm
    tag：  将镜像保存在仓库中，也可以作为重命名使用
    top：  显示容器的运行进程
    unpause：  取消暂停一个或多个容器中的所有进程
    update：   更新一个或者多个容器的配置
    version：  显示docker版本信息
    volume：   管理docker卷
    wait： 阻塞知道容器停止，然后打印推出代码

<h2 id="常用命令列表"><a name="t12"></a>常用命令列表</h2>

<table border='2'>
<thead>
<tr>
  <th>作用</th>
  <th>命令</th>
</tr>
</thead>
<tbody border='2'> 
<tr>
  <td>启动docker服务</td>
  <td>1.service docker start<br>2.如果没有docker服务的话执行/etc/init.d/docker restart</td>
</tr>
<tr>
  <td>关闭docker服务</td>
  <td>上述命令中的start修改为stop即可</td>
</tr>
<tr>
  <td>获取镜像</td>
  <td>docker pull 镜像名称</td>
</tr>
<tr>
  <td>提交镜像</td>
  <td>docker push 镜像名称<br>(符合规范为仓库地址:端口号/仓库名:版本号) 例如:192.168.1.8:5000/znms:v1</td>
</tr>
<tr>
  <td>以指定镜像运行容器</td>
  <td><a href="#docker-start命令补全" target="_blank">docker run</a> <br>-i 保持标准输入打开<br>-d 以后台进程模式重启容器<br>-p 指定容器暴露端口在宿主机上所对端口<br>-v 指定容器的挂载目录<br>-e 指定容器的环境变量<br>–restart=always 指定docker服务启动时总是启动容器</td>
</tr>
<tr>
  <td>启动容器</td>
  <td>docker start 镜像名称 <br>-a 待完成<br>-i 启动一个容器并进入交互模式；<br>-t 10 停止或者重启容器的超时时间，超时后系统将杀死进程。</td>
</tr>
<tr>
  <td>关闭容器</td>
  <td>docker stop 镜像名称</td>
</tr>
<tr>
  <td>重启容器</td>
<td>
docker restart 镜像名称 <br>-a 待完成<br>-i 重启启动一个容器并进入交互模式；<br>-t 10 停止或者重启容器的超时时间，超时后系统将杀死进程。<br>-d 以后台进程模式重启容器
</td>
</tr>
<tr>
  <td>列出所有镜像</td>
  <td>docker images</td>
</tr>
<tr>
  <td>列出所有容器</td>
  <td>docker ps<br>-a 列出所有容器（含沉睡容器）；</td>
</tr>
<tr>
  <td>删除镜像</td>
  <td>docker mi 镜像名称</td>
</tr>
<tr>
  <td>删除容器</td>
  <td>docker rm 容器id(可以通过docker ps查询)</td>
</tr>
<tr>
  <td>进入容器</td>
  <td>docker exec -ti 容器id(可以通过docker ps查询) /bin/bash</td>
</tr>
<tr>
  <td>退出容器</td>
  <td>exit</td>
</tr>
<tr>
  <td>通过容器创建镜像</td>
  <td>docker commit 容器id 创建镜像名称(镜像名:tag)例如znms:v1</td>
</tr>
<tr>
  <td>通过Dockerfile创建文件</td>
  <td>进入到Dockerfile所在目录,<br>执行docker build -t 镜像名 .  <br> 所执行命令的点不可缺少,代表当前目录</td>
</tr>
<tr>
  <td>修改镜像名称</td>
  <td>docker tag 镜像名称 要修改成的镜像名称</td>
</tr>
</tbody>
</table>




<h2 id="docker-start命令补全"><a name="t13"></a>docker start命令补全</h2>

	
	$ docker run -i -d -p 1880:80 -p 13306:3306 -p 122:22 -p 123:23 -p 69:69/udp -p 514:514/tcp -v /Users/apple/znms/03_code/trunk/z-nms:/var/www/html/z-nms -e "REMOTE_HOST=调试ip地址" --restart=always znms:v1