from tutorial.exercicios.functions.change import login


x = 5

def is_int(value):
    value = '5'
    global r
    r = 2
    return isinstance(value, int)

is_int(x)
print(type(x))
print(r)
print(value)

