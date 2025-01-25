import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1737793137797 = glueContext.create_dynamic_frame.from_catalog(database="stedi-hba-lakehouse-db-pr", table_name="step_trainer_landing", transformation_ctx="AmazonS3_node1737793137797")

# Script generated for node Amazon S3
AmazonS3_node1737793139206 = glueContext.create_dynamic_frame.from_catalog(database="stedi-hba-lakehouse-db-pr", table_name="customer_curated", transformation_ctx="AmazonS3_node1737793139206")

# Script generated for node Renamed keys for Join
RenamedkeysforJoin_node1737793361488 = ApplyMapping.apply(frame=AmazonS3_node1737793137797, mappings=[("sensorreadingtime", "long", "right_sensorreadingtime", "long"), ("serialnumber", "string", "right_serialnumber", "string"), ("distancefromobject", "int", "right_distancefromobject", "int")], transformation_ctx="RenamedkeysforJoin_node1737793361488")

# Script generated for node Join
Join_node1737793178896 = Join.apply(frame1=AmazonS3_node1737793139206, frame2=RenamedkeysforJoin_node1737793361488, keys1=["serialnumber"], keys2=["right_serialnumber"], transformation_ctx="Join_node1737793178896")

# Script generated for node Drop Fields
DropFields_node1737793391000 = DropFields.apply(frame=Join_node1737793178896, paths=["right_sensorreadingtime", "right_serialnumber", "right_distancefromobject"], transformation_ctx="DropFields_node1737793391000")

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node1737793410662 = glueContext.getSink(path="s3://stedi-hba-lakehouse-pr/step_trainer/curated/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="StepTrainerTrusted_node1737793410662")
StepTrainerTrusted_node1737793410662.setCatalogInfo(catalogDatabase="stedi-hba-lakehouse-db-pr",catalogTableName="step_trainer_trusted")
StepTrainerTrusted_node1737793410662.setFormat("json")
StepTrainerTrusted_node1737793410662.writeFrame(DropFields_node1737793391000)
job.commit()