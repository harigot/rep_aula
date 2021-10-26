#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva 
#uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a 
#data seja inválida.

from datetime import datetime

def day_validator(value):
    while True:
        try:
            value = int(value)
            while value < 1 or value > 31:
                value = int(input('Please enter a valid day: '))
            return value
        except:
            while not value.isnumeric():
                value = input('Please enter a valid day: ')
            value = int(value)
            continue

def month_validator(value):
    while True:
        try:
            value = int(value)
            while value < 1 or value > 12:
                value = int(input('Please enter a valid day: '))
            return value
        except:
            while not value.isnumeric():
                value = input('Please enter a valid day: ')
            value = int(value)
            continue

def year_validator(value):
    while True:
        try:
            value = int(value)
            while value < 1 or value > 9999:
                value = int(input('Please enter a valid year: '))
            return value
        except:
            while not value.isnumeric():
                value = input('Please enter a valid year: ')
            value = int(value)
            continue

def date_writer():
    day = day_validator(input('Day: '))
    month = month_validator(input('Month: '))
    year = year_validator(input('Year: '))

    date = datetime(year, month, day)
        
    return print('Date:', date.strftime("%d of %B of %Y"))

date_writer()
