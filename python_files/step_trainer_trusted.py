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
AmazonS3_node1737842152684 = glueContext.create_dynamic_frame.from_catalog(database="stedi-hba-lakehouse-db-pr", table_name="customer_curated", transformation_ctx="AmazonS3_node1737842152684")

# Script generated for node Amazon S3
AmazonS3_node1737842163803 = glueContext.create_dynamic_frame.from_catalog(database="stedi-hba-lakehouse-db-pr", table_name="step_trainer_landing", transformation_ctx="AmazonS3_node1737842163803")

# Script generated for node Join
Join_node1737842192195 = Join.apply(frame1=AmazonS3_node1737842152684, frame2=AmazonS3_node1737842163803, keys1=["serialnumber"], keys2=["serialnumber"], transformation_ctx="Join_node1737842192195")

# Script generated for node Drop Fields
DropFields_node1737842222371 = DropFields.apply(frame=Join_node1737842192195, paths=["customername", "email", "phone", "birthday", "serialnumber", "registrationdate", "lastupdatedate", "sharewithresearchasofdate", "sharewithpublicasofdate"], transformation_ctx="DropFields_node1737842222371")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=DropFields_node1737842222371, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1737840911494", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1737842257347 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1737842222371, connection_type="s3", format="json", connection_options={"path": "s3://stedi-hba-lakehouse-pr/step_trainer/trusted/", "partitionKeys": []}, transformation_ctx="AmazonS3_node1737842257347")

job.commit()