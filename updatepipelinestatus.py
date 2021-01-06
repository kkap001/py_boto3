
from __future__ import print_function
from boto3.session import Session

import json
import urllib
import boto3
import zipfile
import tempfile
import botocore
import traceback
from io import BytesIO

print('Loading function')

code_pipeline = boto3.client('codepipeline')
def put_job_success(job, message):
    """Notify CodePipeline of a successful job
    
    Args:
        job: The CodePipeline job ID
        message: A message to be logged relating to the job status
        
    Raises:
        Exception: Any exception thrown by .put_job_success_result()
    
    """
    print('Putting job success')
    print(message)
    code_pipeline.put_job_success_result(jobId=job)
def put_job_failure(job, message):
    """Notify CodePipeline of a failed job
    
    Args:
        job: The CodePipeline job ID
        message: A message to be logged relating to the job status
        
    Raises:
        Exception: Any exception thrown by .put_job_failure_result()
    
    """
    print('Putting job failure')
    print(message)
    code_pipeline.put_job_failure_result(jobId=job, failureDetails={'message': message, 'type': 'JobFailed'})

def lambda_handler(event, context):
    try:
        # Extract the Job ID
        job_id = event['CodePipeline.job']['id']
        
        # Extract the Job Data 
        job_data = event['CodePipeline.job']['data']

        bucket = 'tangclnumerbucket'

        s3 = boto3.client('s3', use_ssl=False)
        Key_unzip = '*'

        prefix      = "node_pipeline/BuildArtif/"
        zipped_keys =  s3.list_objects_v2(Bucket=bucket, Prefix=prefix, Delimiter = "/")
        file_list = []
        for key in zipped_keys['Contents']:
            file_list.append(key['Key'])
        #This will give you list of files in the folder you mentioned as prefix
        s3_resource = boto3.resource('s3')
        #Now create zip object one by one, this below is for 1st file in file_list
        zip_obj = s3_resource.Object(bucket_name=bucket, key=file_list[0])
        print (zip_obj)
        buffer = BytesIO(zip_obj.get()["Body"].read())

        z = zipfile.ZipFile(buffer)
        for filename in z.namelist():
            file_info = z.getinfo(filename)
            s3_resource.meta.client.upload_fileobj(
                z.open(filename),
                Bucket=bucket,
                Key='code/' + f'{filename}')
    print('Function complete.')   
    return "Complete."