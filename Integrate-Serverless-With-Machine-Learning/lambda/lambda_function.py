import pickle
import boto3
import json
import os
import warnings
import numpy as np
warnings.filterwarnings('ignore')

class NpEncoder(json.JSONEncoder):
    def default(self,obj):
        if(isinstance(obj, np.integer)):
            return int(obj)
        if(isinstance(obj, np.floating)):
            return float(obj)
        if(isinstance(obj, np.ndarray)):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)
    
S3_BUCKET_NAME = os.environ["Bucket_Name"]
MODEL_FILE_NAME = os.environ["Model_File"]

s3_client = boto3.client(service_name='s3')
file_path = f'/tmp/{MODEL_FILE_NAME}'

with open(file_path, 'wb') as data:
    s3_client.download_fileobj(S3_BUCKET_NAME,MODEL_FILE_NAME, data)


pickle_in = open(file_path,'rb')
model = pickle.load([pickle_in])

def lambda_handler(event, context):
    print(event)

    input = [event["variance"], event["skewness"], event["curtosis"], event["entropy"]]
    result = model.predict([[input]])
    print(result)
    return{
        'statusCode': 200,
        'body': json.dumps({'prediction': result[0]},cls=NpEncoder),
        'headers':{
            'Access-Control-Allow-Headers':'Content-Type',
            'Access-Control-Allow_Origin':'*',
            'Access-Control-Allow_Methods':'OPTIONS,POST,GET'

        }
    }



