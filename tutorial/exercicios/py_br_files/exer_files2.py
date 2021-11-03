'''
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de 
arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado 
pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da 
Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa 
que gere um relatório, chamado "relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, 
de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes 
deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do 
percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
'''



import os



def user_data_reporter(users_data):
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, 'files/relatorio.txt')
    with open(file_path, 'w+') as users_report:
        users_report.write('ACME Inc.' + ' ' * 15 + 'Uso do espaço em disco pelos usuários\n')
        users_report.write('-' * 72 + '\n')
        users_report.write(
            'Nr.'.ljust(5)
            + 'Usuário'.ljust(15)
            + 'Espaço utilizado'.ljust(21)
            + '% do uso'.ljust(9)
            + '\n\n'
            )

        user_total_space = 0
        for user in users_data:
            user_total_space += int(user.split()[1])
        total_space_mb = user_total_space / 1024 / 1024

        for user in users_data:
            user_name = user.split()[0]
            user_space = user.split()[1]
            user_space_mb = int(user_space) / 1024 / 1024
            user_percentage = (user_space_mb / total_space_mb) * 100
            users_report.write(
                str(users_data.index(user) + 1).ljust(5)
                + user_name.ljust(15)
                + str(round(user_space_mb, 2)).rjust(7) + ' MB'
                + str(round(user_percentage, 2)).rjust(18) + '%\n'
                )
        users_report.write(
            '\nEspaço total ocupado: '
            + str(round(total_space_mb, 2)) + ' MB\n'
            )
        users_report.write(
            'Espaço médio ocupado: '
            + str(round(total_space_mb / len(users_data), 2)) + ' MB\n'
            )
        users_report.close()

def user_data_handler():
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, 'files/usuarios.txt')
    with open(file_path, 'r') as users_file:
        users_data = users_file.read().split('\n')
        users_file.close()
    return user_data_reporter(users_data)


user_data_handler()
