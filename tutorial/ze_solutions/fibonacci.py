def fibonacci(terms):
    sum = 0

    if terms <= 2:
        print(0)
        print(1)
        return 0, 1
    else:
        a, b = fibonacci(terms-1)
        sum = a + b
        print(sum)
        return b, sum


fibonacci(20)
