CREATE EXTERNAL TABLE `customer_trusted`(
  `serialnumber` string COMMENT 'from deserializer',
  `sharewithpublicasofdate` bigint COMMENT 'from deserializer',
  `birthday` string COMMENT 'from deserializer',
  `registrationdate` bigint COMMENT 'from deserializer',
  `sharewithresearchasofdate` bigint COMMENT 'from deserializer',
  `customername` string COMMENT 'from deserializer',
  `sharewithfriendsasofdate` bigint COMMENT 'from deserializer',
  `email` string COMMENT 'from deserializer',
  `lastupdatedate` bigint COMMENT 'from deserializer',
  `phone` string COMMENT 'from deserializer')
ROW FORMAT SERDE
  'org.openx.data.jsonserde.JsonSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://stedi-hba-lakehouse-pr/customer/trusted/'
TBLPROPERTIES (
  'CreatedByJob'='Customer Landing To Trusted',
  'CreatedByJobRun'='jr_06840fb9ba43b17408c77aa3dfc48fe9951aaf10d81d1e72e15ed0502c5165b9',
  'classification'='json')