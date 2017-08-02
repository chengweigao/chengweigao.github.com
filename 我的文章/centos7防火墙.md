systemctl stop firewalld.service #停止firewall

systemctl disable firewalld.service #禁止firewall开机启动


 关闭即可搞定


vim /etc/selinux/config

将SELINUX=enforcing改为SELINUX=disabled 按下保存，reboot。然后执行下面语句



vim /etc/sysconfig/iptables