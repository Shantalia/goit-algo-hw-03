from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    
    today = datetime.today().date()
    congratulations = []
    delta = today + timedelta(days=7)
    future_year = today + timedelta(days=365)
    for user in users:
        birth_day = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        if ((birth_day.day < today.day) and (birth_day.month <= today.month)) or \
            ((birth_day.day > today.day) and (birth_day.month < today.month)):
            congratulation_date = datetime(year = future_year.year, month = birth_day.month, day = birth_day.day)
        else:
            congratulation_date = datetime(year = today.year, month = birth_day.month, day = birth_day.day)
            day_of_week = congratulation_date.weekday()
            if (congratulation_date.date() <= delta):
                if day_of_week >= 5:
                    congratulation_date = datetime(year = today.year, month = birth_day.month, day = birth_day.day+(7-day_of_week))
                congratulations.append({user["name"] : str(congratulation_date.date())})    
    return f"Список привітань на цьому тижні:\n {congratulations}"                 

users = [
    {"name": "John Doe", "birthday": "1985.02.10"},
    {"name": "Jane Smith", "birthday": "1990.01.31"},
    {"name": "Keti Bell", "birthday": "1995.02.04"}
]
print(get_upcoming_birthdays(users))