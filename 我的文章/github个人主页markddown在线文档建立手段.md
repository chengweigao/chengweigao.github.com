大家好：我想做个个人首页，却又不想申请服务器，所以我通过linux python js html  github markdown实现了这个 静态博客
<a href="https://chengweigao.github.io">https://chengweigao.github.io</a>
先谈必须，

1，首先linux 系统不限本地虚拟机 系统上必须环境  git  python

2，github账户，并建立已用户名开头的仓库

3，克隆用户名开头的仓库到linux本地，上传markdown文档到git目录   使用对应python生成的脚本生成js

4，建立对应的index.html,通过js处理脚本json展示，并通过异步建立在线markdown文件展示

5，建立git脚本  掉用python脚本，并提交推送文档到远端

6，远端根据json会自动更新

使用的时候只需将markdown文档上传到git仓库目录   并执行git自动提交bash脚本

参照脚本

<a href="https://chengweigao.github.io/静态github个人首页制作密集.md">静态github个人首页制作密集.md</a>
