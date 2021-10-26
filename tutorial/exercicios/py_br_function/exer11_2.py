from datetime import datetime
  

  
def year_validator(year):
    while True:
        try:
            if year.isnumeric():
                year = int(year)
                if 1 <= year <= 9999:
                    return year
            
            year = input('This program only support years between 0 and 9999.\nInsert a valid year: ')
        
        except:
            continue


def year_formatter(year_validated):
    digit_string = str(year_validated)
    digit_map = map(int, digit_string)
    user_input_result = list(digit_map)
    user_input_result.reverse()

    format = [0, 0, 0, 0]

    for index, value in enumerate(user_input_result):
        format[index] = value

    format.reverse()
    strings = [str(integer) for integer in format]
    final_format = "".join(strings)

    return final_format


def month_validator(month):
    while True:
        try:
            if month.isnumeric():
                month = int(month)
                if 1 <= month <= 12:
                    return month
            
            month = input('The entry must be a number between 1 and 12.\nMonth of the year: ')
        
        except:
            continue


def day_validator(day, month_validated, year_validated):
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]
    date_helper = datetime(1, month_validated, 1)
    
    while True:
        try:
            if day.isnumeric():
                day = int(day)
                if month_validated in months_31:
                    if 1 <= day <= 31:
                        return day
                    else:
                        print(date_helper.strftime('%B'), 'have 31 days.')

                elif month_validated in months_30:
                    if 1 <= day <= 30:
                        return day
                    else:
                        print(date_helper.strftime('%B'), 'have 30 days.')

                elif (year_validated % 4) == 0:
                    if 1 <= day <= 29:
                        return day
                    else:
                        print(year_validated, 'is a leap year.', date_helper.strftime('%B'), 'have 29 days.')
                        
                elif 1 <= day <= 28:
                    return day
                else:
                    print(date_helper.strftime('%B'), 'have 28 days.')
            
            day = input('Please enter a valid day: ')

        except:
            continue  


def date_writer():
    year = input('Year: ')
    year_validated = year_validator(year)
    year_final_format = year_formatter(year_validated)

    month = input('Month: ')
    month_validated = month_validator(month)

    day = input('Day: ')
    day_validated = day_validator(day, month_validated, year_validated)

    date = datetime(year_validated, month_validated, day_validated)
        
    return print('Date:', date.strftime('%B %d,'), year_final_format)

date_writer()
