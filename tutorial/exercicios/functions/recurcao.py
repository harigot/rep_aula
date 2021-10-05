
def factorial(num):
    
    result = 0
    
    if num == 1:
        return num

    else:
        return num * (factorial(num - 1))

print(factorial(3))
