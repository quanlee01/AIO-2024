factorial_array = [1,1,2]
def factorial(n):
    if(n >= len(factorial_array)):
        for i in range(len(factorial_array), n + 1):
            ith_fact = factorial_array[i-1] * i
            factorial_array.append(ith_fact)
    return factorial_array[n]
def taylor_sin(x, n):
    base = x
    power = x
    sum = x
    sign = -1
    for i in range(1,n):
        power = power * base * base
        sum += power * sign / factorial(2*i + 1)
        sign *= -1
    print(sum)
def taylor_cos(x, n):
    base = x 
    power = 1
    sum = 1
    sign = -1
    for i in range(1,n):
        power = power * base * base
        sum += power * sign / factorial(2*i)
        sign *= -1
    print(sum)
def taylor_sinh(x, n):
    base = x
    power = x
    sum = x
    for i in range(1,n):
        power = power * base * base
        sum += power / factorial(2*i + 1)
    print(sum)
def taylor_cosh(x, n):
    base = x 
    power = 1
    sum = 1
    for i in range(1,n):
        power = power * base * base
        sum += power / factorial(2*i)
    print(sum)
taylor_sin(3.14, 10)
taylor_cos(3.14, 10)
taylor_sinh(3.14, 10)
taylor_cosh(3.14, 10)