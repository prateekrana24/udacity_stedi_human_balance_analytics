import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Amazon S3
AmazonS3_node1737794243346 = glueContext.create_dynamic_frame.from_catalog(database="stedi-hba-lakehouse-db-pr", table_name="accelerometer_trusted", transformation_ctx="AmazonS3_node1737794243346")

# Script generated for node Amazon S3
AmazonS3_node1737794244983 = glueContext.create_dynamic_frame.from_catalog(database="stedi-hba-lakehouse-db-pr", table_name="step_trainer_landing", transformation_ctx="AmazonS3_node1737794244983")

# Script generated for node Join
Join_node1737794426055 = Join.apply(frame1=AmazonS3_node1737794243346, frame2=AmazonS3_node1737794244983, keys1=["user"], keys2=["sensorreadingtime"], transformation_ctx="Join_node1737794426055")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=Join_node1737794426055, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1737789021593", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1737794675991 = glueContext.getSink(path="s3://stedi-hba-lakehouse-pr/machine_learning_curated/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1737794675991")
AmazonS3_node1737794675991.setCatalogInfo(catalogDatabase="stedi-hba-lakehouse-db-pr",catalogTableName="machine_learning_curated")
AmazonS3_node1737794675991.setFormat("json")
AmazonS3_node1737794675991.writeFrame(Join_node1737794426055)
job.commit()