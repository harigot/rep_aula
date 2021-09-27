#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres; Idade: entre 0 e 150; Salário: maior que zero;
#Sexo: 'f' ou 'm'; Estado Civil: 's', 'c', 'v', 'd';

nome = input('Seu nome: ')
while len(nome) <= 3: #len():Conta o numero de elementos em um objeto.
    print('Erro, seu nome deve possuir mais do que 3 caracteres.')
    nome = input('Seu nome: ')

id = int(input('Sua idade: '))
while id < 0 or id > 150:
    print('Erro, Sua idade deve estar entre 0 e 150.')
    id = int(input('Sua idade: '))

salario = float(input('Seu salario: '))
while salario < 0:
    print('Erro, seu salario deve ser maior ou igual a 0.')
    salario = float(input('Seu salario: '))

sex = input('Seu genero biologico, digite (f) para feminino ou (m) para masculino: ') #add .lower() to avoid crash-error
while sex != 'f' and sex != 'm':
    print('Erro, por favor siga as instruções abaixo.')
    sex = input('Seu genero biologico, digite (f) para feminino ou (m) para masculino: ')

ec = input('Seu estado civil, (s) para solteiro(a), (c) para casado(a), (v) para viuvo(a), (d) para divorciado(a): ')
while ec != 's' and ec != 'c' and ec != 'v' and ec != 'd':
    print('Erro, por favor siga as instruções abaixo.')
    ec = input('Seu estado civil, (s) para solteiro(a), (c) para casado(a), (v) para viuvo(a), (d) para divorciado(a): ')

print('Sucesso')
