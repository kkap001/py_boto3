from __future__ import print_function

import boto3
import time
path = "/" + "dist"
def lambda_handler(event, context):
    
    client = boto3.client('cloudfront')
    invalidation = client.create_invalidation(DistributionId='ECJ14GYA8GB67',
         InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': [path]
        },
        'CallerReference': str(time.time())
    })