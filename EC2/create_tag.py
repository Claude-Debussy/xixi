import boto3
client = boto3.client('ec2')
response = client.create_tags(
    DryRun=False,
    Resources=[
        'i-007cfb9c44f275b52',
    ],
    Tags=[
        {
            'Key': 'otk',
            'Value': 'tenon'
        },
    ]
)
print(response)