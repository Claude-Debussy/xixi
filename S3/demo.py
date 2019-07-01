import boto3

s3_client = boto3.client(
    service_name='s3',
)
s3_resources = boto3.resource('s3')

for bucket in s3_resources.buckets.all():
    bucket_name = bucket.name
    bucket_tagging = s3_resources.BucketTagging(bucket_name)
    # response = bucket_tagging.put(
    #     Tagging={
    #         'TagSet': [
    #             {
    #                 'Key': 'test',
    #                 'Value': 'well'
    #             },
    #         ]
    #     }
    # )
    response = bucket_tagging.delete()
    print(response)