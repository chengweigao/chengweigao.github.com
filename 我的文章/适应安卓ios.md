    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="viewport" content="width=device-width">
    <meta name="viewport" content="width=320,maximum-scale=1.0,user-scalable=no">
     <link rel="stylesheet" href="/css/bootstrap.min.css">
    <!-- //   <meta content="user-scalable=0;" name="viewport" />-->
    
    <title><?php echo $data->title ?></title>
    <style>
    
    *{
    margin: 0;
    padding: 0;
    
    }
    .zoombox{
    /*font-size: 60px !important;*/
    /*//  zoom:2 !important*/
    /*line-height: 80px !important;*/
    }
    .zoombox img{
    width:100% !important
    }
    </style>
    </head>
    
    <body style="background:#8f8f94">
    <div class="container-fluid">
    <div style="width: 100%;margin: 0 auto;padding:12px;background: #ffffff" >
    <?php   echo $data->content; ?>
    </div>
    </div>
    <script type="text/javascript" src="http://code.jquery.com/jquery-1.11.0.js"></script>
    <script type="text/javascript">
    var browser={
    versions:function(){
    var u = navigator.userAgent, app = navigator.appVersion;
    return {//移动终端浏览器版本信息
    trident: u.indexOf('Trident') > -1, //IE内核
    presto: u.indexOf('Presto') > -1, //opera内核
    webKit: u.indexOf('AppleWebKit') > -1, //苹果、谷歌内核
    gecko: u.indexOf('Gecko') > -1 && u.indexOf('KHTML') == -1, //火狐内核
    mobile: !!u.match(/AppleWebKit.*Mobile.*/)||!!u.match(/AppleWebKit/), //是否为移动终端
    ios: !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/), //ios终端
    android: u.indexOf('Android') > -1 || u.indexOf('Linux') > -1, //android终端或者uc浏览器
    iPhone: u.indexOf('iPhone') > -1 || u.indexOf('Mac') > -1, //是否为iPhone或者QQHD浏览器
    iPad: u.indexOf('iPad') > -1, //是否iPad
    webApp: u.indexOf('Safari') == -1 //是否web应该程序，没有头部与底部
    };
    }(),
    language:(navigator.browserLanguage || navigator.language).toLowerCase()
    }
    
    
    $(function() {
    
    if(browser.versions.iPhone){
    $(".container-fluid").addClass('zoombox');
    }
    $(".container-fluid").addClass('zoombox');
    var colorlist=['red','yellow','blue','green','#c0c0c0','#8f8f94','#ffffff','#cccccc'];
    $("body").css('background',colorlist[Math.ceil(Math.random()*6)])
    });
    
    </script>
    
    </body>
    </html>
    