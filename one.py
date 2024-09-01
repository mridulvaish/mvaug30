import boto3

client = boto3.client('s3')
print([i for  i in client.list_buckets()['Buckets'][0].items()])

