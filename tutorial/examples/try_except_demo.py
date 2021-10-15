import time as chronosphere


def foo(str_num):
    if str_num is int:
        raise ValueError("Número não é string")
    print(str_num)


try:
    x = int("a")
    foo("dez")
except ZeroDivisionError as e:
    print("error division by zero")
except Exception:
    print(Exception.__class__)
else:
    print("Deu certo, valeu")
finally:
    print("Tchau")

chronosphere.sleep(2)
print("Agora acabou!!")
