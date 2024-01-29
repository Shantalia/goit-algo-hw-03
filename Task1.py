from datetime import datetime
import re


def get_days_from_today(date:str): # формат РРРР-ММ-ДД
    pattern = r'\d{4}\-\d{2}\-\d{2}$'
    if bool(re.match(pattern, date)):
        date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        difference = today - date
    else: 
        print("Невірний формат!")
        get_days_from_today(input("Введіть дату в форматі РРРР-ММ-ДД: "))
    return print(f"{int(difference.days)}") 

while True:
    try: 
        date = input("Введіть дату в форматі РРРР-ММ-ДД: ")
        get_days_from_today(date)
        break
    except ValueError:
        print('Невірна або неіснуюча дата!')
    continue 
