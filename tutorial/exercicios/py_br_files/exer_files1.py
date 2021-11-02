"""
1 Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
"""



import os



def ip_validator(ip):
    ip_nth = ip.split('.')
    if len(ip_nth)!= 4:
        return False
    for octet in ip_nth:
        if not octet.isnumeric():
            return False

    first_octet = int(ip_nth[0])
    second_octet = int(ip_nth[1])
    third_octet = int(ip_nth[2])
    fourth_octet = int(ip_nth[3])

    if first_octet == 127 or first_octet == 0 or first_octet > 254:
        return False

    if second_octet > 255 or third_octet > 255 or fourth_octet > 255:
        return False
        
    if 1 <= first_octet <= 126:  #Ip class A
        if (second_octet and third_octet and fourth_octet == 0 or 
            second_octet and third_octet and fourth_octet == 255):
            return False

    if 128 <= first_octet <= 191:  #Ip class B
        if (third_octet and fourth_octet == 0 or 
            third_octet and fourth_octet == 255):
            return False
    
    if 192 <= first_octet <= 224:  #Ip class C
        if 1 > fourth_octet > 254:
            return False

    return True


def report_maker(ip_good, ip_bad):
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, 'files/ip_report.txt')
    with open(file_path, 'w+') as report:
        report.write('valid addresses:\n')
        for i in ip_good:
            report.write(i+'\n')
        report.write('\ninvalid addresses:\n')
        for i in ip_bad:
            report.write(i+'\n')
        report.close()


def ip_database_handler():
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, 'files/ip_database.txt')
    with open(file_path, 'r') as ip_file:
        ip_list = ip_file.read().split('\n')
        ip_good = []
        ip_bad = []

        for ip in ip_list:
            if ip_validator(ip):
                ip_good.append(ip)
            else:
                ip_bad.append(ip)
        ip_file.close()
        return report_maker(ip_good, ip_bad)

ip_database_handler()

