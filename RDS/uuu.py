import boto3

client = boto3.client('rds')
ret = client.describe_db_instances()
# print(ret)
for i in ret['DBInstances']:
    arn = i['DBInstanceArn']
    print(arn)
    response = client.add_tags_to_resource(
        ResourceName=arn,
        Tags=[
            {
                'Key': 'kkk',
                'Value': 'vvvv'
            },
        ]
    )