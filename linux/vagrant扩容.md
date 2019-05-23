有的时候在vagrant下载的box，容量太小了，因此就想怎么扩容，mark一下操作步骤：
转换为VGI格式


	VBoxManage clonehd "centos-vm-disk1.vmdk" "box-disk1.vdi" –format vdi

需要先vagrant halt，然后进入到虚拟机的安装目录下执行
扩展容量为40G

	VBoxManage modifyhd "box-disk1.vdi"  --resize 40960
打开Oracle VM VirtualBox 管理器界面，选中虚拟机右键->设置->存储，删除原来的盘片，增加扩容后的盘片 或者使用命令行处理



	VBoxManage storageattach leopard_default_1533786337049_17725 --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "box-disk1.vdi"

也可以将vdi转换成vmdk

	 VBoxManage clonehd "box-disk1.vdi" "box-disk1.vmdk" --format vmdk
启动虚拟机
	vagrant up

查看磁盘并格式化，然后重启

	(1).fdisk -l
	(2).fdisk /dev/sda
	(3).按p显示分区表，默认是 sda1 和 sda2。
	(4).按n新建主分区。
	(5).按p设置为主分区。
	(6).输入3设置为第三分区。
	(7).输入两次回车设置默认磁盘起始位置。
	(8).输入t改变分区格式
	(9).输入3选择第三分区
	(10).输入8e格式成LVM格式
	(11).输入w执行
	(12).reboot

登录虚拟机后

	(1).pvcreate /dev/sda3 # 最好reboot一下
	(2).pvdisplay # 可以看到原来的/下的/dev/sda2的VG Name为 centos
	(3).vgextend centos /dev/sda3 # 扩充到/下
	(4).lvextend /dev/mapper/centos-root /dev/sda3
	(5).resize2fs /dev/mapper/centos-root

在centos 7下，这一步会出错，只需执行以下命令

	xfs_growfs /dev/mapper/centos-root
	df -h #检查容量