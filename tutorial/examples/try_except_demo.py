import time


def foo(str_num):
    if str_num is int:
        raise ValueError("Número não é string")
    print(str_num)


try:
    x = int("a")
    foo("dez")
except ZeroDivisionError as e:
    print("error division by zero")
except Exception as e:
    print(e.__class__)
else:
    print("Deu certo, valeu")
finally:
    print("Tchau")

time.sleep(10)
print("Agora acabou")
