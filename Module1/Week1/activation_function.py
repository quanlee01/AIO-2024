import math
def sigmoid_function(x):
    result = 1 / (1 + math.e**(-x))
    return result
def relu(x):
    if x <= 0: 
        return 0
    else:
        return x
def elu(x):
    alpha = 0.01
    if x <= 0:
        return alpha * (math.e**x - 1)
    else:
        return x
def is_number(x):
    try:
        float(x)
    except ValueError:
        return False
    return True
def apply_activation_function(x, activation_function_type):
    if (activation_function_type not in {"sigmoid","relu","elu"}):
        print(activation_function_type, " is not supported")
        return
    if (not is_number(x)):
        print("x must be a number")
        return
    x = float(x)
    
    if (activation_function_type == "sigmoid"):
        result = sigmoid_function(x)
    elif (activation_function_type == "relu"):
        result = relu(x)
    elif (activation_function_type == "elu"): 
        result = elu(x)
    print(f"{activation_function_type}: f({x}) = {result}")
x = input("Input x = ")
activation_function_type = input("Input activation function (sigmoid|relu|elu): ")
apply_activation_function(x,activation_function_type)
