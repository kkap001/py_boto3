import zipfile

import boto3

s3 = boto3.client("s3")
s3_object = s3.get_object(Bucket="tangclnumerbucket")
streaming_body = s3_object["Body"]

with zipfile.ZipFile(streaming_body) as zf:
    print(zf.namelist())