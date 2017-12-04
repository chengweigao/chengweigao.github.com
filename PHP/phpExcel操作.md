phpxcel 读常规文档操作

	程	厂长	     xxx	计划部
	程1	厂长1	 xxx	计划部1
	程2	厂长2	 xxx	计划部2
	程3	厂长3	 xxx	计划部3
      
如上读成这样的效果
    
    {
	    "1": [
	        "程",
	        "厂长",
	        "     xxx",
	        "计划部"
	    ],
	    "2": [
	        "程1",
	        "厂长1",
	        " xxx",
	        "计划部1"
	    ],
	    "3": [
	        "程2",
	        "厂长2",
	        " xxx",
	        "计划部2"
	    ],
	    "4": [
	        "程3",
	        "厂长3",
	        " xxx",
	        "计划部3"
	    ]
	}
代码如下：

		require_once BASE_URL . '/PHPExcel/PHPExcel.php';//引入PHPExcel类文件
		$objPHPExcel = \PHPExcel_IOFactory::load("./1.xlsx");
        $currentSheet = $objPHPExcel->getSheet(0); /* * 读取excel文件中的第一个工作表 */
       \PHPExcel_Cell::columnIndexFromString(); //字母列转换为数字列 如:AA变为27
        $allColumn = $currentSheet->getHighestColumn();/**取得最大的列号*/
        $allRow = $currentSheet->getHighestRow(); /* * 取得一共有多少行 */
        $all=$currentSheet->getCellCollection();/*取出当前的所有A1,A2,A3*/
		/*笨方法转换  abcd 列值*/
        foreach($all as $v){
            $data[]=$currentSheet->getCell($v)->getColumn();
        }
		/*去重复 统计列宽数  a b c d   1,2,3,4 列*/
        $data=array_unique($data);
		/*双循环获取横向数据*/
		//横向从1开始
         for($i=1;$i<$allRow+1;$i++){
             //纵向从0开始
				for($y=0;$y<count($data);$y++){
               $new[$i][$y]=$currentSheet->getCellByColumnAndRow($y,$i)->getValue();
			}
		}
		echo json_encode($new);die;