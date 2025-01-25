CREATE EXTERNAL TABLE `accelerometer_trusted`(
  `timestamp` bigint COMMENT 'from deserializer',
  `user` string COMMENT 'from deserializer',
  `x` float COMMENT 'from deserializer',
  `y` float COMMENT 'from deserializer',
  `z` float COMMENT 'from deserializer',
  `customername` string COMMENT 'from deserializer',
  `email` string COMMENT 'from deserializer',
  `phone` string COMMENT 'from deserializer',
  `birthday` string COMMENT 'from deserializer',
  `serialnumber` string COMMENT 'from deserializer',
  `registrationdate` bigint COMMENT 'from deserializer',
  `lastupdatedate` bigint COMMENT 'from deserializer',
  `sharewithresearchasofdate` bigint COMMENT 'from deserializer',
  `sharewithpublicasofdate` bigint COMMENT 'from deserializer')
ROW FORMAT SERDE
  'org.apache.hive.hcatalog.data.JsonSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://stedi-hba-lakehouse-pr/accelerometer/trusted/new/'
TBLPROPERTIES (
  'auto.purge'='false',
  'has_encrypted_data'='false',
  'numFiles'='-1',
  'presto_query_id'='20250125_195909_00175_j2hdh',
  'presto_version'='0.215-21820-g882377f',
  'totalSize'='-1',
  'transactional'='false',
  'write.compression'='NONE')