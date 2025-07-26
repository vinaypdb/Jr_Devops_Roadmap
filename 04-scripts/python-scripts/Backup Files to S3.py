import boto3
import os

s3 = boto3.client('s3')
bucket_name = 'my-devops-backup'

backup_dir = '/etc/'

for root, _, files in os.walk(backup_dir):
    for file in files:
        filepath = os.path.join(root, file)
        s3.upload_file(filepath, bucket_name, f"{root}/{file}")
print("Backup complete")