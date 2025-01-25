CREATE EXTERNAL TABLE `customer_curated`(
  `customername` string COMMENT 'from deserializer',
  `email` string COMMENT 'from deserializer',
  `phone` string COMMENT 'from deserializer',
  `birthday` string COMMENT 'from deserializer',
  `serialnumber` string COMMENT 'from deserializer',
  `registrationdate` bigint COMMENT 'from deserializer',
  `lastupdatedate` bigint COMMENT 'from deserializer',
  `sharewithresearchasofdate` bigint COMMENT 'from deserializer',
  `sharewithpublicasofdate` bigint COMMENT 'from deserializer',
  `sharewithfriendsasofdate` bigint COMMENT 'from deserializer')
ROW FORMAT SERDE
  'org.openx.data.jsonserde.JsonSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://stedi-hba-lakehouse-pr/customer/curated/'
TBLPROPERTIES (
  'CreatedByJob'='Customer Curated Zone',
  'CreatedByJobRun'='jr_c8797809fd2f99c0ae02267326df7a477dd33bf23f588cb59b14c8a3115a4f03',
  'classification'='json')