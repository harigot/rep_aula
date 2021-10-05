def login():
    l, s = login_input()
    return l == s

def login_input():
    l = input('Insira login de usuario: ')
    s = input('Insira senha de usuario: ')
    return l, s

while login():
    print('erro')

print('sucesso')

