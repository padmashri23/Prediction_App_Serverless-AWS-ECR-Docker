# Prediction_App_Serverless-AWS-ECR-Docker
building an End to End ML Prediction Application.

1.Machine Learning Model: Train and test RandomForestClassifier model using Kaggle Dataset
https://www.kaggle.com/datasets/ritesaluja/bank-note-authentication-uci-data?select=BankNote_Authentication.csv

2.BackEnd: After local testing in Google Collab, the model is saved to Amazon S3 bucket. Python code and dependencies are packaged as Docker Image and uploaded to Amazon Elastic Container Registry. A Lambda is created using the container image, which downloads the model file from S3 and respond to user requests with predictions.

3.Frontend: We will create an API gateway that integrates with the Lambda function. For user interface, we will create a React Application that post the user form to api gateway, parses the response and shows result.

PROJECT ARCHITECTURE:
![image](https://github.com/user-attachments/assets/cdd570eb-07c1-4956-9b12-816690c4c304)

