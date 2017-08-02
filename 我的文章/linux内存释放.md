**`1.	 [root@www chat]# free -m  `**
`2.	             total       used       free     shared    buffers     cached  `
`3.	Mem:         15830      15600        229          0        216      14493  `
`4.	-/+ buffers/cache:        890      14939  `
`5.	Swap:         7983          0       7983  `
`6.	[root@www chat]# echo 3 > /proc/sys/vm/drop_caches`
`7.	[root@www chat]# free -m ` 
`8.	             total       used       free     shared   buffers     cached ` 
`9.	Mem:         15830        506      15323          0          1         27  `
`10.	-/+ buffers/cache:        477      15352  `
`11.	Swap:         7983          0       7983  `
**`12.	[root@www chat]# echo 3 > /proc/sys/vm/drop_caches `**
    