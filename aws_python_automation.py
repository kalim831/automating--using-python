import boto3

s3 =boto3.resource('s3')
# ec2 =boto3.resource('ec2')
# this code will show all bucket in s3 and their count
c = 0
for bucket in s3.buckets.all():
    print(bucket.name)
    c = c + 1
print (c)

#for downloading objects from s3 bucket
s3.Bucket("kalimking").download_file("Kalim Resume.pdf","Kalim Resume.pdf")

#for creating new s3 bucket
bucket_name = input("Enter the new bucket name: ")

s3.create_bucket(Bucket=bucket_name)
print("Bucket created successfully.")

#for uploading object in s3 bucket
file_path = input("Enter the file path: ")
bucket_name = input("Enter the bucket name: ")

s3.Bucket(bucket_name).upload_file(file_path, "UploadedFile.pdf")
print("File uploaded successfully.")








