import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
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

# Script generated for node Accelerometer Landing
AccelerometerLanding_node1737790803017 = glueContext.create_dynamic_frame.from_catalog(database="stedi-hba-lakehouse-db-pr", table_name="accelerometer_landing", transformation_ctx="AccelerometerLanding_node1737790803017")

# Script generated for node Customer Trusted
CustomerTrusted_node1737790808553 = glueContext.create_dynamic_frame.from_catalog(database="stedi-hba-lakehouse-db-pr", table_name="customer_trusted2", transformation_ctx="CustomerTrusted_node1737790808553")

# Script generated for node Join
Join_node1737790893073 = Join.apply(frame1=CustomerTrusted_node1737790808553, frame2=AccelerometerLanding_node1737790803017, keys1=["email"], keys2=["user"], transformation_ctx="Join_node1737790893073")

# Script generated for node Drop Fields and Duplicates
SqlQuery0 = '''
select distinct customername, email, phone, birthday,
serialnumber, registrationdate, lastupdatedate,
sharewithresearchasofdate, sharewithpublicasofdate,
sharewithfriendsasofdate from myDataSource
'''
DropFieldsandDuplicates_node1737790978441 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"myDataSource":Join_node1737790893073}, transformation_ctx = "DropFieldsandDuplicates_node1737790978441")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=DropFieldsandDuplicates_node1737790978441, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1737789021593", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1737791199049 = glueContext.getSink(path="s3://stedi-hba-lakehouse-pr/customer/curated/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1737791199049")
AmazonS3_node1737791199049.setCatalogInfo(catalogDatabase="stedi-hba-lakehouse-db-pr",catalogTableName="customer_curated")
AmazonS3_node1737791199049.setFormat("json")
AmazonS3_node1737791199049.writeFrame(DropFieldsandDuplicates_node1737790978441)
job.commit()