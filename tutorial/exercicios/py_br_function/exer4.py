#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de
#caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

print('Insira um numero para saber se e negativo ou positivo.')
num = int(input('digite um número: '))

def positive_negative(num):
    if num >= 0:
        return print('O número é positivo.')
    else:
        return print('O número é negativo.')

positive_negative(num)


