> 使用portsnap来更新步骤
> (可以修改/etc/portsnap.conf的配置文件SERVERNAME=portsnap.hshh.org，以提高你的下载速度)
> 
> 修改完毕后执行
> #portsnap fetch
> #portsnap extract
> #portsnap update
> 
> 使用cvsup安装更新步骤
> a、首先安装cvsup
> cd /usr/ports/net/cvsup-without-gui
> make install clean
> b、配置cvsup
> cp /usr/share/examples/cvsup/ports-supfile /etc/ports-supfile
> 修改配置文件
> ee /etc/ports-supfile
> 将*default host=CHANGE_THIS.FreeBSD.org修改为*default host=cvsup.cn.FreeBSD.org
> c、执行cvsup
> cvsup -L 2 /etc/ports-supfile
> 
> 
> 
> 
> bsdinstall  系统安装重置
> bsdconfig  系统配置
> 
> 
> 
> 目前FreeBSD pkg包管理体系的repo源多了一些，速度快了很多。
> 仓库中目前的版本为3.14，安装gnome3很简单。
> pkg install xorg gnome3
> echo "exec /usr/local/bin/gnome-session" ~/.xinitrc
> vi /etc/rc.conf
> hald_enable="YES"
> dbus_enable="YES"
> gdm_enable="YES"
> 就搞定了。
> 桌面的体验比gnome2感觉要流畅很多。
>  
> linux教程：在 ubuntu 15.04 的 GNOME 终端中开启多个标签 
> 
> 