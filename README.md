# Udacity Stedi Human Balance Analytics Project

## Overall Steps From Start To Finish
### Creating S3 Bucket and VPC Gateway Endpoint Connection For AWS Glue
#### 1) aws s3 mb s3://stedi-hba-lakehouse-pr --> makes s3 bucket
#### 2) aws s3 ls s3://stedi-hba-lakehouse-pr --> checks s3 bucket files/sub-folders
#### 3) aws ec2 describe-vpcs --> shows you vpcs information
#### 4) aws ec2 describe-route-tables --> shows you route-table information
#### 5) aws ec2 create-vpc-endpoint --vpc-id (your vpc id goes here) --service-name com.amazonaws.us-east-1.s3 --route-table-ids (Your route table id goes here) --> creates vpc connection for AWS Glue to access S3 bucket

### Creating AWS Glue Service IAM Role
#### 1) aws iam create-role --role-name stedi-dba-lakehouse-pr-service-role --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "glue.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}'

#### NOTE: I meant to write hba for human balance analytics, not dba. However, I just left it as dba.

#### 2) aws iam put-role-policy --role-name stedi-dba-lakehouse-pr-service-role --policy-name S3Access --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ListObjectsInBucket",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::stedi-hba-lakehouse-pr"
            ]
        },
        {
            "Sid": "AllObjectActions",
            "Effect": "Allow",
            "Action": "s3:*Object",
            "Resource": [
                "arn:aws:s3:::stedi-hba-lakehouse-pr/*"
            ]
        }
    ]
}'

#### 3) aws iam put-role-policy --role-name stedi-dba-lakehouse-pr-service-role --policy-name GlueAccess --policy-document '{
>     "Version": "2012-10-17",
>     "Statement": [
>         {
>             "Effect": "Allow",
>             "Action": [
>                 "glue:*",
>                 "s3:GetBucketLocation",
>                 "s3:ListBucket",
>                 "s3:ListAllMyBuckets",
>                 "s3:GetBucketAcl",
>                 "ec2:DescribeVpcEndpoints",
>                 "ec2:DescribeRouteTables",
>                 "ec2:CreateNetworkInterface",
>                 "ec2:DeleteNetworkInterface",
>                 "ec2:DescribeNetworkInterfaces",
>                 "ec2:DescribeSecurityGroups",
>                 "ec2:DescribeSubnets",
>                 "ec2:DescribeVpcAttribute",
>                 "iam:ListRolePolicies",
>                 "iam:GetRole",
>                 "iam:GetRolePolicy",
>                 "cloudwatch:PutMetricData"
>             ],
>             "Resource": [
>                 "*"
>             ]
>         },
>         {
>             "Effect": "Allow",
>             "Action": [
>                 "s3:CreateBucket",
>                 "s3:PutBucketPublicAccessBlock"
>             ],
>             "Resource": [
>                 "arn:aws:s3:::aws-glue-*"
>             ]
>         },
>         {
>             "Effect": "Allow",
>             "Action": [
>                 "s3:GetObject",
>                 "s3:PutObject",
>                 "s3:DeleteObject"
>             ],
>             "Resource": [
>                 "arn:aws:s3:::aws-glue-*/*",
>                 "arn:aws:s3:::*/*aws-glue-*/*"
>             ]
>         },
>         {
>             "Effect": "Allow",
>             "Action": [
>                 "s3:GetObject"
>             ],
>             "Resource": [
>                 "arn:aws:s3:::crawler-public*",
>                 "arn:aws:s3:::aws-glue-*"
>             ]
>         },
>         {
>             "Effect": "Allow",
>             "Action": [
>                 "logs:CreateLogGroup",
>                 "logs:CreateLogStream",
>                 "logs:PutLogEvents",
>                 "logs:AssociateKmsKey"
>             ],
>             "Resource": [
>                 "arn:aws:logs:*:*:/aws-glue/*"
>             ]
>         },
>         {
>             "Effect": "Allow",
>             "Action": [
>                 "ec2:CreateTags",
>                 "ec2:DeleteTags"
>             ],
>             "Condition": {
>                 "ForAllValues:StringEquals": {
>                     "aws:TagKeys": [
>                         "aws-glue-service-resource"
>                     ]
>                 }
>             },
>             "Resource": [
>                 "arn:aws:ec2:*:*:network-interface/*",
>                 "arn:aws:ec2:*:*:security-group/*",
>                 "arn:aws:ec2:*:*:instance/*"
>             ]
>         }
>     ]
> }'

### Moving Data From Udacity's Stedi Human Balance Analytics Github to S3 Landing Area
#### 1) git clone https://github.com/udacity/nd027-Data-Engineering-Data-Lakes-AWS-Exercises.git --> used to copy repo from github
#### 2) aws s3 cp ./customer-1691348231425.json s3://stedi-hba-lakehouse-pr/customer/landing/ --> used to copy data from folder into specified s3 directory
#### 3) aws s3 ls s3://stedi-hba-lakehouse-pr/customer/landing/ --> used to check if the data file is in the desired folder



## Project Overview
### In this project, we are acting as a data engineer for the STEDI team in order to build a data lakehouse solution for sensor data that trains a machine learning model.
### The STEDI Team has been hard work developing a hardware STEDI Step Trainer that:

#### 1) Trains the user to do a STEDI balance exercise
#### 2) Uses sensors on a device that collects data to train a machine-learning algorithm to detect steps
#### 3) Has a companion mobile app that collects data and interacts with the device sensors

### There have been millions of early adopters who are willing to purchase the STEDI Step Trainers and use them
### Several customers have already received their Step Trainers, installed the mobile application, and begun using them together to test their balance. The Step Trainer is just a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions.
### The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used.
### Some of the early adopters have agreed to share their data for research purposes. Only these customers’ Step Trainer and accelerometer data should be used in the training data for the machine learning model.


## Project Objectives
### The goal here, as a data engineer on the STEDI Step Trainer team, is to extract the data produced by the STEDI Step Trainer sensors and the mobile app, and curate them into a data lakehouse solution on AWS so that Data Scientists can train the learning model.
### You'll use the data from the STEDI Step Trainer and mobile app to develop a lakehouse solution in the cloud that curates the data for the machine learning model using:
#### 1) Python and Spark
#### 2) AWS Glue
#### 3) AWS Athena
#### 4) AWS S3

### You'll be creating Python scripts using AWS Glue and Glue Studio. These web-based tools and services contain multiple options for editors to write or generate Python code that uses PySpark.
### You can use any Python editor locally to work with and save code as well, but be aware that to actually test or run Glue Jobs, you'll need to submit them to your AWS Glue environment.


## Project Data

### STEDI has three JSON data sources to use from Step Trainer
#### 1) customer (this data is from fulfillment and the STEDI website)
#### 2) step_trainer (this is the data from the motion sensor)
#### 3) accelerometer (this is the data from the mobile app)




