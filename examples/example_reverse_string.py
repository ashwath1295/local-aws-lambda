from local_lambda import LocalLambda

def reverse_string(event, context):
    original = event.get("text", "")
    reversed_text = original[::-1]
    return {"original": original, "reversed": reversed_text}

lambda_runtime = LocalLambda(reverse_string)
event = {"text": "Lambda"}
print(lambda_runtime.invoke(event))
