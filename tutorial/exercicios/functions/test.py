def fibo_input():
    global num
    num = int(input('number of terms? '))
    return num

def fibo_check():
    try:
        if fibo_input() >= 0:
            print('certo')
            return False
        else:
            print('errado')
            return True     
    
    except ValueError:
        print('errado')
        return True

fibo_check()