from local_lambda import LocalLambda

def divide_numbers(event, context):
    try:
        numerator = event["numerator"]
        denominator = event["denominator"]
        result = numerator / denominator
        return {"result": result}
    except ZeroDivisionError:
        return {"error": "Cannot divide by zero"}

lambda_runtime = LocalLambda(divide_numbers)
event = {"numerator": 10, "denominator": 0}
print(lambda_runtime.invoke(event))
