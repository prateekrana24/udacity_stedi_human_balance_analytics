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
AmazonS3_node1737839777325 = glueContext.create_dynamic_frame.from_catalog(database="stedi-hba-lakehouse-db-pr", table_name="customer_trusted", transformation_ctx="AmazonS3_node1737839777325")

# Script generated for node Amazon S3
AmazonS3_node1737839778181 = glueContext.create_dynamic_frame.from_catalog(database="stedi-hba-lakehouse-db-pr", table_name="accelerometer_landing", transformation_ctx="AmazonS3_node1737839778181")

# Script generated for node Join
Join_node1737839815932 = Join.apply(frame1=AmazonS3_node1737839777325, frame2=AmazonS3_node1737839778181, keys1=["email"], keys2=["user"], transformation_ctx="Join_node1737839815932")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=Join_node1737839815932, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1737835676707", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1737839858396 = glueContext.write_dynamic_frame.from_options(frame=Join_node1737839815932, connection_type="s3", format="json", connection_options={"path": "s3://stedi-hba-lakehouse-pr/customer/curated/", "partitionKeys": []}, transformation_ctx="AmazonS3_node1737839858396")

job.commit()