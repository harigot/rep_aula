#Faça um programa, com uma função que necessite de três argumentos, 
#e que forneça a soma desses três argumentos.

print('Insira 3 numeros para serem somados.')
a = int(input('Primeiro numero: '))
b = int(input('segundo numero: '))
c = int(input('terceiro numero: '))

def sum(a, b, c):
    result = a + b + c
    return result

print ('A soma dos numeros é:', sum(a, b, c))