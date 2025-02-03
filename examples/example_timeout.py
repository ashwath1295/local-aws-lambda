from local_lambda import LocalLambda
import time

def long_running_task(event, context):
    time.sleep(5)  # Simulate a long-running task
    return {"message": "Task completed"}

lambda_runtime = LocalLambda(long_running_task, timeout=3)
event = {}
print(lambda_runtime.invoke(event))
