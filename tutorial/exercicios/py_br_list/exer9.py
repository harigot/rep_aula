# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados
# dos elementos do vetor.

# Correção: Não tem referencia ao "vetor A" do enunciado. -0,05
list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
result = 0

for i in range(len(list)):
    result += (list[i])**2

# Comentário: Poderia haver uma maior legibilidade. "A soma dos quadrados são: ..."
print(result)
