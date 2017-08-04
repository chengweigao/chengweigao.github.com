#用php获取当前目录树的json
	<?php
	header("Content-Type:text/html; charset=utf-8");
	ini_set('display_errors','On');
	error_reporting(E_ALL);
	$dir='D:/www/';
	function traverse($path = '.') {
    $current_dir = opendir($path);    //opendir()返回一个目录句柄,失败返回false
    $dirData=[];
    while(($file = readdir($current_dir)) !== false) {    //readdir()返回打开目录句柄中的一个条目
		//windows下字符转码
        $file=iconv('GB2312', 'UTF-8', $file);
        $sub_dir = $path . DIRECTORY_SEPARATOR . $file;    //构建子目录路径
        if($file == '.' || $file == '..') {
            continue;
        } else if(is_dir($sub_dir)) {    //如果是目录,进行递归


            $dirData[$file]=traverse($sub_dir);
        } else {    //如果是文件,直接输出
            $dirData[]=$file;

        }
    }

    return $dirData;
	}
	$re=traverse($dir);
	//链接字符串
	$str="<?php  return ";
	$str.=var_export($re,true);
	$str .=";";
	//写入文件
	file_put_contents('./1.php',$str);
	$li=include_once  './1.php';
	file_put_contents('./1.txt',json_encode($li));
	if(json_last_error()===0){
    echo "成功了<a href='1.txt'>查看json</a>";
    echo "<br>";
    $data=include './1.php';
    var_dump($data);

	};
	///var_dump(getDir($dir));
