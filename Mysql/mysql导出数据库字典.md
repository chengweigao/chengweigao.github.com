可用如下sql查询结果，得出对应的字段  可导出xls   可网页展示   剩下的就看自己怎么diy了      
    
    select 
	#库
  	TABLE_SCHEMA,
	#表	
	TABLE_NAME,
	#字段名称	
	COLUMN_NAME，
	#字段类型
	COLUMN_TYPE,
	#字段备注		
	COLUMN_COMMENT 
	from 
	information_schema.columns 
	where TABLE_SCHEMA='您的库名' 