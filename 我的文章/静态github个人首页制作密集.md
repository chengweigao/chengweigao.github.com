1,首先粘上自制的python脚本  通过这个来生成文档json 请自己注意缩进

	#!/usr/bin/env python
    import os
    import json
    import sys
    
    reload(sys)
    sys.setdefaultencoding('utf8')
	#过滤对应不显示文件
    listOver = ['_config.yml', 'gitBush.sh', 'dirToJson.py', 'index.html', '.idea', '.git','dir.md','dir.js']
    def thefileTree(mm):
	    a = {}
	    mm1 = os.listdir(mm)
    
	    for i in mm1:
	    
	    	if i in listOver:
	    		continue
		    if os.path.isdir(mm + i + '/'):
		    	dirname = mm + i + '/'
		    	a[dirname] = (thefileTree(dirname))
		    else:
		    	dirname = mm + i
		   		 a[dirname] = i
	    
   		 return a
    def writeToFile(mm):
    jsonStr = json.dumps(mm)
    f = open('dir.md', 'w')
    f.write("var a=" + jsonStr)
    
    
    xx = thefileTree('./')
    # print xx
    writeToFile(xx)

2,再粘上朕的git提交代码   前提是已经配置好了git的密码账户  可以直接git操作并不用输入密码

    #!/bin/bash
    #by chengwigao
    #使用脚本生成js文档目录
    python dirToJson.py;
    #git提交文件删除文件
    git add -A;
    #定义提交备注
    DATEFORMATTYPE1=$(date +%Y%m%d%H%M);
    git commit -m "${DATEFORMATTYPE1}";
    #推送提交
    git push;
    #多次提交只为保证文件一致
    git add .;
    #定义提交备注
    DATEFORMATTYPE1=$(date +%Y%m%d%H%M);
    git commit -m "${DATEFORMATTYPE1}";
    #推送提交
    git push;

3,再贴上index代码   由于个人对设计欠缺   代码凑合只为可以预览 切记https  引入js http的cdn会挂的

    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>chengweigao'S Pages</title>
    <!--读取文档json-->
    <script src="dir.md"></script>
    <script src="https://code.jquery.com/jquery-2.0.0.min.js"></script>
    <script src="https://cdn.bootcss.com/pagedown/1.0/Markdown.Converter.js"></script>
    <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css"
      integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    
    <!-- 可选的 Bootstrap 主题文件（一般不用引入） -->
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap-theme.min.css"
      integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    
    <!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
    <script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js"
    integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
    crossorigin="anonymous"></script>
    
    </head>
    <body>
    
    
    <div class="row">
    <div id="list" class="col-md-2" style="overflow: auto">
    
    </div>
    <div id="myDiv" class="col-md-10"  style="overflow: auto;border: 2px dotted black;padding: 20px; border-radius:20px ">
    
    </div>
    </div>
    
    
    <script>
    /*将文档做成列表*/
    function writeUl(a, ax) {
    if (!ax) {
    
    var str = '<ul class="sidebar-menu list-group">';
    } else {
    var str = '<ul class="treeview-menu" style="display: none">';
    }
    
    $.each(a, function (x, y) {
    if ((typeof(y)) == "string") {
    str += '<li class="list-group-item" onclick="dothe(' + "'" + x + "'" + ',this)" >' + y + '</li>';
    } else {
    str += '<li class="list-group-item" value="0" onclick="doSeeSon(this)">' + x;
    str += writeUl(y, 1);
    str += "</li>";
    }
    })
    str += "</ul>";
    return str
    }
    var liList = writeUl(a);
    /*点击展示列表内容*/
    function dothe(x,a) {
    
    if($(a).parent().parent().attr('value')==1){
    $(a).parent().parent().attr('value',0);
    }
    document.title= x+"来自chengweigao'S Pages";
    
    htmlobj = $.ajax({url: x, async: false});
    var converter = new Markdown.Converter();
    var htm = converter.makeHtml(htmlobj.responseText);
    $('#myDiv').html(htm);
    
    
    }
    function doSeeSon(a){
    
    if($(a).attr("value")!=1){
    $(a).attr("value",1);
    $(a).children("ul").show(500);
    }else{
    $(a).attr("value",0);
    $(a).children("ul").hide(500);
    }
    
    }
    //展示列表
    $("#list").html(liList);
       $(function(){
       $("#myDiv").css('height',window.screen.availHeight);
       $("#list").css('height',window.screen.availHeight);
    
       })
    </script>
    
    </body>
    </html>