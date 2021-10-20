from datetime import datetime

def month_validator(month):
    while True:
        try:
            if month.isnumeric():
                month = int(month)
                if 1 < month < 12:
                    return month
            
            month = input('The entry must be a number between 1 and 12.\nMonth of the year: ')
        
        except:
            continue

def day_validator(day, month):
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]
    date_helper = datetime(1, month, 1)
    
    while True:
        try:
            if day.isnumeric():
                day = int(day)
                if month in months_31 and 1 < day < 31:
                    return day
                elif month in months_30 and 1 < day <30:
                    return day
                elif 1 < day < 29:
                    return day
                elif month in months_31:
                    print(date_helper.strftime('%B'), 'have 31 days.')
                elif month in months_30:
                    print(date_helper.strftime('%B'), 'have 30 days.')
                else:
                    print(date_helper.strftime('%B'), 'have 29 days.')
            
            day = input('Please enter a valid day: ')

        except:
            continue    

def year_validator(year):
    while True:
        try:
            if year.isnumeric():
                year = int(year)
                if 1 < year < 9999:
                    return year
            
            year = input('This program only support years between 0 and 9999.\nInsert a valid year: ')
        
        except:
            continue

def date_writer():

    month = input('Month: ')
    month = month_validator(month)

    day = input('Day: ')
    day = day_validator(day, month)

    year = input('Year: ')
    year = year_validator(year)

    date = datetime(year, month, day)
        
    return print('Date:', date.strftime('%B %d, %Y'))

date_writer()