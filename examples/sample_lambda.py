from local_lambda import LocalLambda

def test_lambda(event, context):
    return {"message": "Hello from Local AWS Lambda!", "event": event}

lambda_runtime = LocalLambda(test_lambda)
print(lambda_runtime.invoke({"key": "value"}))
