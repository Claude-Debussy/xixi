import boto3

client = boto3.client('dynamodb')
response = client.list_tables()
for i in response['TableNames']:
    response = client.tag_resource(
        ResourceArn=i,
        Tags=[
            {
                'Key': 'n',
                'Value': 'aaa'
            },
        ]
    )
