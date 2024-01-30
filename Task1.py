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
        get_days_from_today()
    return f"{int(difference.days)}" 

try: 
    date = "2025-01-17"
    print(get_days_from_today(date))
except ValueError:
    print('Невірна або неіснуюча дата!')