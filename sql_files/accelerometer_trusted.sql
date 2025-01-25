CREATE EXTERNAL TABLE IF NOT EXISTS `stedi-hba-lakehouse-db-pr`.`accelerometer_trusted` (
  `user` string,
  `timeStamp` bigint,
  `x` float,
  `y` float,
  `z` float
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://stedi-hba-lakehouse-pr/accelerometer/trusted/'
TBLPROPERTIES (
  'classification' = 'json',
  'write.compression' = 'NONE'
);