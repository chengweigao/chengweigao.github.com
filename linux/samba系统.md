samba实战  用来windows链接linux目录   方便windows下开发调试


安装samba   

  	yum install samba

 配置文件

	/etc/samba/smb.cof
 添加配置

	[koorey]
    comment = koorey
    path = /home/koorey
    writable = yes

防火墙设置

		Linux中/etc/passwd里的用户和Samba里的用户几乎没啥关系，硬说有的话，
		那就是：Samba的所有用户都必须是系统里已存在的用户。我们要授权系统用户访问Samba的话，通过命令：
        smbpasswd  -a   koorey  #添加用户koorey到Samba用户数据库中
        这条命令输入完后，会提示为新建的用户koorey设置访问密码。最后再执行一下service smb restart命令就OK了。
		至此，Samba服务器就架设好了。
		不信？为啥？因为后面还有章节，哈哈，说的没错。
		理论上说确实已经架设好了，可千万不要忽略了Linux的安全机制的存在：iptables和selinux。其中本人就吃了selinux不少苦头。
		因为只弄了iptables，却忘记了selinux这个牛叉叉的家伙。
		关于iptables本人会在后面的博客从头到脚，从里到外，循序渐进的以此和大家交待它的来龙去脉。当然，如果你感兴趣的话。

		在对待iptables的问题上：
        普通青年：直接在命令行敲…
            service  iptables stop。
        文艺青年：依次在命令行敲…
            iptables -I RH-Firewall-1-INPUT 5 -m state --state NEW -m tcp -p tcp --dport 139 -j ACCEPT
            iptables -I RH-Firewall-1-INPUT 5 -m state --state NEW -m tcp -p tcp --dport 445 -j ACCEPT
            iptables -I RH-Firewall-1-INPUT 5 -p udp -m udp --dport 137 -j ACCEPT
            iptables -I RH-Firewall-1-INPUT 5 -p udp -m udp --dport 138-j ACCEPT
            iptables-save
            service iptables  restart
		同样，在对在selinux的问题上：（这丫的把我坑惨了呀）
        普通青年：直接在命令行敲…
            setenforce 0
            vi /etc/selinux/config
        将SELINUX=enforcing改为SELINUX=disabled为开机重启后不再执行setenfore节约光阴。
       	文艺青年：依次在命令行敲…
            setsebool -Psamba_enable_home_dirs on
            setsebool -Psamba_export_all_rw on
       	完事儿之后再：getsebool  -a  | grep  samba一把，你懂得…