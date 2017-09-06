#datepicker is not defined
该死的错误，排查了jq版本，排查了js引入顺序

	jQuery.Deferred exception: $(...).datepicker is not a function TypeError: $(...).datepicker is not a function
    at HTMLDocument.<anonymous> (http://aa.com/xcc/web/index:410:26)
    at j (http://aa.com/js/jquery.js:2:29948)
    at k (http://aa.com/js/jquery.js:2:30262) undefined

最后把他放到外边即可 如下代码  分析原因 

    $(function(){
    
	})
    $("#datepicker").datepicker({
    		todayHighlight: true,
    		language: 'zh-CN'
    });

