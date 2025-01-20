# Udacity Stedi Human Balance Analytics Project

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




