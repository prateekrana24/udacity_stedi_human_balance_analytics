CREATE EXTERNAL TABLE `step_trainer_trusted`(
  `sensorreadingtime` bigint COMMENT 'from deserializer',
  `serialnumber` string COMMENT 'from deserializer',
  `distancefromobject` int COMMENT 'from deserializer')
ROW FORMAT SERDE
  'org.apache.hive.hcatalog.data.JsonSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://stedi-hba-lakehouse-pr/step_trainer/trusted/'
TBLPROPERTIES (
  'auto.purge'='false',
  'has_encrypted_data'='false',
  'numFiles'='-1',
  'presto_query_id'='20250125_221646_00104_rguqt',
  'presto_version'='0.215-21820-g882377f',
  'totalSize'='-1',
  'transactional'='false',
  'write.compression'='NONE')