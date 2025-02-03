from local_lambda import LocalLambda

def add_numbers(event, context):
    a = event.get("a", 0)
    b = event.get("b", 0)
    return {"result": a + b}

lambda_runtime = LocalLambda(add_numbers)
event = {"a": 5, "b": 10}
print(lambda_runtime.invoke(event))
