import os
import boto3

client = boto3.client('cloudformation')
response = client.create_change_set(
    StackName='teststack',
    UsePreviousTemplate=True,
    Parameters=[
        {
            'ParameterKey': 'codecommitBranch',
            'ParameterValue': 'dmaster',
            'UsePreviousValue': False,

        },
    ],
    Capabilities=[
        'CAPABILITY_IAM',
    ],

    ChangeSetName='test123',

        
)