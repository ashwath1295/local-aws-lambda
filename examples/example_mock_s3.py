from local_lambda import LocalLambda, MockS3

s3 = MockS3()

def upload_file(event, context):
    s3.put_object(Bucket="test-bucket", Key=event["key"], Body=event["data"])
    return {"message": "File uploaded successfully"}

def retrieve_file(event, context):
    obj = s3.get_object(Bucket="test-bucket", Key=event["key"])
    return obj

# Uploading File
upload_lambda = LocalLambda(upload_file)
print(upload_lambda.invoke({"key": "file1.txt", "data": "Hello, Lambda!"}))

# Retrieving File
retrieve_lambda = LocalLambda(retrieve_file)
print(retrieve_lambda.invoke({"key": "file1.txt"}))
