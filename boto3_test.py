import boto3

BUCKET_NAME = 'boto-test-bucket-v1'

s3 = boto3.client('s3')



# Upload files to bucket
with open('./banana.txt', 'rb') as file:
    s3.upload_fileobj(file, BUCKET_NAME, 'banana.txt')

# all object in bucket
response = s3.list_objects_v2(Bucket=BUCKET_NAME)
for obj in response['Contents']:
    print(obj)

# Download files
s3.download_file(BUCKET_NAME, 'banana.txt', 'downloaded_banana.txt')

# Downloaded file with binary data
with open('downloaded_banana.txt', 'wb') as f:
    s3.download_fileobj(BUCKET_NAME, 'banana.txt', f)
    # some code here (examle send img to frontend)

# Make presigned url to give limited access unatirozed users
url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket": BUCKET_NAME, "Key": "banana.txt"},
    ExpiresIn=120,
)
print(url)

# Create NEW bucket (in this case publik)
bucket_location = s3.create_bucket(

    ACL="public-read", Bucket="new-test-bucket-v12",
    CreateBucketConfiguration={'LocationConstraint': 'eu-central-1'}
)

print(bucket_location)

# Copy file between buckets
s3.copy_object(
    ACL="public-read",
    Bucket="new-test-bucket-v12",
    CopySource=f"/{BUCKET_NAME}/banana.txt",
    Key="Copied_banana.txt"
)

# GET data about obj
response = s3.get_object(Bucket=BUCKET_NAME, Key='banana.txt')
print(response)
