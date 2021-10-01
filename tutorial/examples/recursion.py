x = 100


def f(num):
    print(num)
    if num <= 0:
        return 0
    return num + f(num-1)


print(f"A soma dos numeros entre 0 e 100 é: {f(x)}")
