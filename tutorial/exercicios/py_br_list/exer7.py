# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

list = [1, 1, 1, 2, 2]

sum = sum(list)
print(sum)  # Correção: Falta de legibilidade -0,5
multiply = 1

for i in range(len(list)):
    multiply *= list[i]

print(multiply)  # Correção: Falta de legibilidade -0,5
