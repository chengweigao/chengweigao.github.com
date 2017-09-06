###碰到json不正常 又没办法处理，只能强行替换


    <?php
    
    $arr=<<<STYI
    {"i":""肉类-谷类-水果（理想的互补性）各种水果和蔬菜（植物微量营养素的协同作用）"","ti":"","yn":"","zhii":""}
    STYI;
    /*去除特殊符号*/
    $arr=preg_replace('/\s/', '', $arr);
    /*所有引号替换成单引号*/
    $arr=str_replace(array('""'),"''",$arr);
    /*保留最结尾空白值*/
    $arr=str_replace(array("''}"),'""}',$arr);
    /*将正常的空置替换成双引号*/
    $arr=str_replace(":'',",':"",',$arr);
    /*将不正常的开头结尾替换掉*/
    $arr=str_replace(":''",':"\'',$arr);
    $arr=str_replace("'',",'\'",',$arr);
    
    $arr=json_decode($arr,true);
    //echo json_last_error_msg();
    
    //var_dump($arr);die;
    
    ?>
#php json_encode时中文被转义
		可以分析json错误原因
		json_last_error()

		#这样就避免了中文转义
		json_encode($_FILES, JSON_UNESCAPED_UNICODE );

		下面的常量可以和 json_encode() 的 form 选项结合使用。

		JSON_HEX_TAG (integer)
		所有的 < 和 > 转换成 \u003C 和 \u003E。 自 PHP 5.3.0 起生效。
		JSON_HEX_AMP (integer)
		所有的 & 转换成 \u0026。 自 PHP 5.3.0 起生效。
		JSON_HEX_APOS (integer)
		所有的 ' 转换成 \u0027。 自 PHP 5.3.0 起生效。
		JSON_HEX_QUOT (integer)
		所有的 " 转换成 \u0022。 自 PHP 5.3.0 起生效。
		JSON_FORCE_OBJECT (integer)
		使一个非关联数组输出一个类（Object）而非数组。 在数组为空而接受者需要一个类（Object）的时候尤其有用。 自 PHP 5.3.0 起生效。
		JSON_NUMERIC_CHECK (integer)
		将所有数字字符串编码成数字（numbers）。 自 PHP 5.3.3 起生效。
		JSON_PRETTY_PRINT (integer)
		用空白字符格式化返回的数据。 自 PHP 5.4.0 起生效。
		JSON_UNESCAPED_SLASHES (integer)
		不要编码 /。 自 PHP 5.4.0 起生效。
		JSON_UNESCAPED_UNICODE (integer)
		以字面编码多字节 Unicode 字符（默认是编码成 \uXXXX）。 自 PHP 5.4.0 起生效。
        JSON 错误码
			常量	含义	可用性
			JSON_ERROR_NONE	没有错误发生	 
			JSON_ERROR_DEPTH	到达了最大堆栈深度	 
			JSON_ERROR_STATE_MISMATCH	无效或异常的 JSON	 
			JSON_ERROR_CTRL_CHAR	控制字符错误，可能是编码不对	 
			JSON_ERROR_SYNTAX	语法错误	 
			JSON_ERROR_UTF8	异常的 UTF-8 字符，也许是因为不正确的编码。	PHP 5.3.3
			JSON_ERROR_RECURSION	One or more recursive references in the value to be encoded	PHP 5.5.0
			JSON_ERROR_INF_OR_NAN	One or more NAN or INF values in the value to be encoded	PHP 5.5.0
			JSON_ERROR_UNSUPPORTED_TYPE	指定的类型，值无法编码。	PHP 5.5.0
			JSON_ERROR_INVALID_PROPERTY_NAME	指定的属性名无法编码。	PHP 7.0.0
			JSON_ERROR_UTF16	畸形的 UTF-16 字符，可能因为字符编码不正确。	PHP 7.0.0