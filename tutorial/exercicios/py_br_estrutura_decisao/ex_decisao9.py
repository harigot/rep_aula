#Exercicio 9: Faça um Programa que leia três números e mostre-os em ordem decrescente.

n = []
q = 3

for i in range(q):
    e = int(input('Digite um numero: '))
    n.append(e) #.append(): Adiciona elementos a lista

n.sort(reverse = True) #.sort(): organiza de arcordo com os parametros
print(n)