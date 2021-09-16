#exercicio 4: Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

l = input('Digite uma letra do alfabeto: ')

vog = ['a', 'e', 'i', 'o', 'u']
con = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z']

if l in vog:
    print('Vogal')
elif l in con:
    print('consoante')
else:
    print('erro')
    

