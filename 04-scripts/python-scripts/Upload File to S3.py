import boto3

s3 = boto3.client('s3')
s3.upload_file('file.txt', 'my-bucket-name', 'file.txt')
print("Upload complete")
# Upload complete   