	git  init  当当前目录创建仓库
    git init --bare 初始化的目录等同于一个.git目录的内容。这样就比较好理解git的本质：本地仓库的.git和服务器仓库。它们是一回事情。


git pusg报错误：
#receive.denyCurrentBranch' configuration variable to 'refuse'
这是由于git默认拒绝了push操作，需要进行设置

	git config receive.denyCurrentBranch=ignore

或修改.git/config添加如下代码：

    [receive]
    denyCurrentBranch = ignore
