import boto3

client = boto3.client('elasticache')
# ret = client.list_tags_for_resource(
#  #   ResourceName='arn:aws-cn:sns:cn-north-1:497221081160:hbeacon:test',
#     # ResourceName='arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster'
# )
ret = client.describe_cache_clusters()  #遍历所有集群
# print(ret)
arn = ret['CacheClusters'][0]['NotificationConfiguration']['TopicArn']
print(arn)
response = client.add_tags_to_resource(
    ResourceName=arn,
    Tags=[
        {
            'Key': 'qqq',
            'Value': 'vvv'
        },
    ]
)

# 这个arn有问题？  要不应该就okay 了
# arn:aws-cn:rds:cn-north-1:497221081160:db:hbeacon-test
# arn:aws-cn:sns:cn-north-1:497221081160:hbeacon-test
