#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de 
#crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
#Faça um programa que calcule e escreva o número de anos necessários para que a população do 
#país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento 
#iniciais. Valide a entrada e permita repetir a operação.

anos = 0
r = True

while r == True:
    
    A = input('População de um país A: ')
    while not A.isnumeric():
        print('Erro, a resposta deve ser um numero interio maior que zero.')
        A = input('População de um país A: ')
    A = int(A)

    taxa_a = input('taxa de crescimento da população de um país A em porcentagem: ')
    taxa_a_aux = taxa_a.replace('.', '') #remove os pontos da str pra usar funcoes numericas.
    while not taxa_a_aux.isnumeric():
        print('Erro, a resposta deve ser um numero maior que zero.')
        taxa_a = input('taxa de crescimento da população de um país A em porcentagem: ')
        taxa_a_aux = taxa_a.replace('.', '')
    taxa_a = float(taxa_a)

    B = input('População de um país B: ')
    while not B.isnumeric():
        print('Erro, a resposta deve ser um numero interio maior que zero.')
        B = input('População de um país B: ')
    B = int(B)

    taxa_b = input('taxa de crescimento da população de um país B em porcentagem: ')
    taxa_b_aux = taxa_b.replace('.', '')
    while not taxa_b_aux.isnumeric():
        print('Erro, a resposta deve ser um numero maior que zero.')
        taxa_b = input('taxa de crescimento da população de um país A em porcentagem: ')
        taxa_b_aux = taxa_b.replace('.', '')
    taxa_b = float(taxa_b)

    while A < B:
        A = A + A * (taxa_a / 100)
        B = B + B * (taxa_b / 100)
        anos = anos + 1

        if (A - B) > (A + (A * (taxa_a / 100))) - (B + (B * (taxa_b / 100))):
            print('Nessas condições a população de A nunca ultrapassará a população de b')
            break
        else:
            print(anos, 'anos.')
    else:
        print(anos, 'anos.')
    
    r = input('Deseja repetir a operação? ')
    while r != 'y' and r != 'n': 
        print('Erro, resposta fora do padrão.')
        r = input('Deseja repetir a operação? ')

    if r == 'y':
        r = True
    elif r == 'n':
        r = False
        print('operação finalizada.')    

