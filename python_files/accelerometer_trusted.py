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
AmazonS3_node1737784544387 = glueContext.create_dynamic_frame.from_catalog(database="stedi-hba-lakehouse-db-pr", table_name="customer_trusted2", transformation_ctx="AmazonS3_node1737784544387")

# Script generated for node Amazon S3
AmazonS3_node1737784545907 = glueContext.create_dynamic_frame.from_catalog(database="stedi-hba-lakehouse-db-pr", table_name="accelerometer_landing", transformation_ctx="AmazonS3_node1737784545907")

# Script generated for node Customer Privacy Filter
CustomerPrivacyFilter_node1737785514803 = Join.apply(frame1=AmazonS3_node1737784544387, frame2=AmazonS3_node1737784545907, keys1=["email"], keys2=["user"], transformation_ctx="CustomerPrivacyFilter_node1737785514803")

# Script generated for node Drop Fields
DropFields_node1737788140482 = DropFields.apply(frame=CustomerPrivacyFilter_node1737785514803, paths=["email", "phone", "lastupdatedate", "sharewithfriendsasofdate", "customername", "sharewithresearchasofdate", "registrationdate", "birthday", "sharewithpublicasofdate", "serialnumber"], transformation_ctx="DropFields_node1737788140482")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=DropFields_node1737788140482, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1737783182769", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1737785557491 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1737788140482, connection_type="s3", format="json", connection_options={"path": "s3://stedi-hba-lakehouse-pr/accelerometer/trusted/", "partitionKeys": []}, transformation_ctx="AmazonS3_node1737785557491")

job.commit()