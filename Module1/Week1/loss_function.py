import random
import math
def mae(n):
    result = 1 / n
    sum = 0
    for i in range(n):
        target = random.uniform(0, 10)
        predict = random.uniform(0, 10)
        sum += abs(target - predict)
        print(f"loss name: MAE, sample: {i}, pred: {predict}, target: {target}, loss: {sum}")
    result *= sum
    print(f"final MAE: {result}")
def mse(n):
    result = 1 / n
    sum = 0
    for i in range(n):
        target = random.uniform(0, 10)
        predict = random.uniform(0, 10)
        sum += (target - predict)**2
        print(f"loss name: MSE, sample: {i}, pred: {predict}, target: {target}, loss: {sum}")
    result *= sum
    print(f"final MAE: {result}")
def rmse(n):
    result = 1 / n
    sum = 0
    for i in range(n):
        target = random.uniform(0, 10)
        predict = random.uniform(0, 10)
        sum += (target - predict)**2
        print(f"loss name: RMSE, sample: {i}, pred: {predict}, target: {target}, loss: {sum}")
    result *= sum
    result = math.sqrt(result)
    print(f"final MAE: {result}")
def calculate_loss():
    n = input("Input number of samples (integer number) which are generated: ")
    loss_function = input("Input loss function")
    if(not n.isnumeric()):
        print("number of samples must be an integer number")
        return
    if(loss_function == "MAE"):
        mae(n)
        return
    if(loss_function == "MSE"):
        mse(n)
        return
    rmse(n)
    return
calculate_loss()
