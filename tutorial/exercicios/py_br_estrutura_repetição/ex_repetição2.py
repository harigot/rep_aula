#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do 
#usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

l = input('Insira login de usuario: ')
s = input('Insira senha de usuario: ')

while l == s:
    print('Erro! Usuario e senhas devem ser diferentes.')
    l = input('Insira login de usuario: ')
    s = input('Insira senha de usuario: ')
else:
    print('Sucesso!')
