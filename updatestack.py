import boto3

client = boto3.client('cloudformation')
response = client.update_stack(
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

)