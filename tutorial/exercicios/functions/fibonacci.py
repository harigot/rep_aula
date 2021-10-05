
def fibonacci(num):

    if num <= 1:
        return num

    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def fibo_input():
    global num
    num = int(input('number of terms? '))
    return num


def fibo_check():  # Name suggestion: fibo_input_validator
    try:
        if fibo_input() >= 0:
            # print('certo')
            return False
        else:
            # print('errado')
            return True

    except ValueError:
        # print('errado')
        return True


num = 0

while fibo_check():
    print('error, plese enter a non negative number')

for i in range(num+1):
    print(fibonacci(i))
else:
    print(num)
