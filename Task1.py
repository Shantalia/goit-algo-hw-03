from datetime import datetime
import re

def get_days_from_today(): # формат РРРР-ММ-ДД
    date = input("Введіть дату в форматі РРРР-ММ-ДД: ")
    pattern = r'\d{4}\-\d{2}\-\d{2}$'
    if bool(re.match(pattern, date)):
        date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        difference = today - date
        return print(f"{int(difference.days)}")
    else: 
        print("Невірний формат!")
        get_days_from_today()
    
try: 
    get_days_from_today()
except ValueError:
    print('Невірна або неіснуюча дата!')