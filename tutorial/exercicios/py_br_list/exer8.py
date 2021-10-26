# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo
# vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

age = []
height = []

# Comentário: Poderia ter algo para diferenciar as pessoas. Ex: Pessoa 1, ou pedir o nome da pessoa. -0,0
for i in range(5):
    age.append(int(input('idade: ')))
    height.append(float(input('altura?: ')))

age.reverse()
height.reverse()
print(age, height)
