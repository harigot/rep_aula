#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados 
#dos elementos do vetor.

list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
result = 0

for i in range(len(list)):
    result += (list[i])**2

print(result)