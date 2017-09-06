demo演示地址：
[https://chengweigao.github.io](https://chengweigao.github.io/JS/index.html "渐变百分比图表")

	<!doctype html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Document</title>
	    <style>
	        * {
	            margin: 0;
	            padding: 0;
	        }
	
	        .c {
	            float: left;
	
	        }
	    </style>
	    <script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>
	</head>
	<body>
	
	<!--<div style="width: 186px;height: 186px;background: #ffffff;border: 1px solid;border-radius: 50%;">-->
	<!--<img src="./currentcode.png" alt="" style="position: relative">-->
	
	
	<!--</div>-->
	<!--<div style="margin:  0 auto;position: relative">-->
	
	
	<!--</div>-->
	<!--<div style="background: red;width:1px;border-bottom: 50px solid transparent;border-left: 50px solid transparent;border-right: 50px solid transparent">-->
	
	<!--</div>-->
	<!--
	<!--&ndash;&gt;-->
	<div style="position: relative;margin: 0 auto;width: 200px;box-sizing: content-box">
	    <canvas id="myCanvas" width="162" height="162"
	            style="margin: 0 auto;height: 160px;width: 160px;border-radius: 50%;border: 1px solid; overflow: hidden;box-sizing: content-box;position: absolute;top:0;z-index: 3;">
	        Your browser does not support the canvas element.
	    </canvas>
	    <div style="position: absolute;height: 135px;width: 135px;border-radius: 50%;z-index:6;border: 1px solid;overflow: hidden;background: #ffffff;top:12px;left: 12px;">
	
	    </div>
	    <div style="height: 160px;width: 160px;border-radius: 50%; overflow: hidden;border: 1px solid;box-sizing: content-box;position: relative;z-index:2"
	         id="box-show">
	
	
	        <div class="c">
	            <div id="c2" style="position: relative;width: 80px;height: 80px;background: -webkit-linear-gradient(  #5FACF7, #B583B7);
	    background: -moz-linear-gradient(  #5FACF7, #B583B7);
	    background: linear-gradient( #5FACF7, #B583B7);z-index: -1">
	
	            </div>
	
	            <div id="c1" style="position: relative;width: 80px;height: 80px;background: -webkit-linear-gradient(#B583B7, #FF646C);
	    background: -moz-linear-gradient( #B583B7, #FF646C);
	    background: linear-gradient( #B583B7, #FF646C);z-index: -1">
	
	            </div>
	        </div>
	        <div class="c">
	
	
	            <div id="c3" style="position: relative;width: 80px;height: 80px;background: -webkit-linear-gradient( #5FACF7, #3CCED6);
	    background: -moz-linear-gradient( #5FACF7, #3CCED6);
	    background: linear-gradient( #5FACF7, #3CCED6);z-index: -1">
	
	            </div>
	            <div id="c4" style="position: relative;width: 80px;height: 80px;background: -webkit-linear-gradient( #3CCED6, #29E9A5);
	    background: -moz-linear-gradient( #3CCED6, #29E9A5);
	    background: linear-gradient( #3CCED6, #29E9A5);z-index: -1">
	
	            </div>
	        </div>
	    </div>
	    <br>
	    <br>
	
	    <form action="">
	        <label for="num">
	            比率
	            <input type="number" id="num" value="10" max="100" min="1"/>
	        </label>
	        <input type="button" id="submit" onclick="drawMove(cxt,$('#num').val());" value="设置"/>
	    </form>
	</div>
	
	
	<script type="text/javascript">
	    var c = document.getElementById("myCanvas");
	    var cxt = c.getContext("2d");
	    cxt.fillStyle = "red";
	    cxt.beginPath();
	    /*旋转画布做处理画园*/
	    cxt.translate(80, 80);
	    cxt.rotate(90 * Math.PI / 180);
	    cxt.translate(-80, -80);
	    cxt.fill();
	    cxt.closePath();
	    function drawMove(ctx, du) {
	        ctx.clearRect(0, 0, 162, 162);
	        if (du < 100) {
	            /*按比例画圆弧
	            * */
	            ctx.beginPath();
	            ctx.strokeStyle = "#ffffff";
	            ctx.lineWidth = '60';
	            ctx.arc(80, 80, 70, 0, Math.PI * (du / 100) * 360 / 180, true);
	            ctx.stroke();
	            ctx.closePath();
	            return true;
	        }
	
	    }
	
	    drawMove(cxt, 100);
	
	
	    function tuDo() {
	        var num = parseInt($("#num").val());
	        if (num < 101 && num > 0) {
	            drawMove(cxt, num);
	            return true;
	        } else {
	            alert("值太小");
	            return true;
	        }
	
	    }
	
	
	</script>
