
为了设计mysql的个人排行统计对比查询
到网上借鉴了一些方法   有些方法是自己在sql定义变量   set @rownum=0
如下这种方法 很机智 其效率  有待商榷

	SELECT *
	FROM (SELECT @rownum := @rownum + 1 AS rownum, 某表.*
		FROM (SELECT @rownum := 0
			) r, 某表
		ORDER BY 某表.字段 DESC
		) a
	WHERE 某表.字段 = '某值'
	ORDER BY 某表.字段 DESC
	LIMIT 2