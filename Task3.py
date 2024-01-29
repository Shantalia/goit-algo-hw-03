import re

def normalize_phone(phone_number):
    code = "+38"
    our_digits = r"\d+"
    clear_number = []
    for ch in re.findall(our_digits, phone_number):
        clear_number.append(ch)
    string = ""
    for i in code:
        string += i
        if phone_number.startswith(string):
            continue
        else:
            code = string
        phone_number = ""
        phone_number = code + phone_number.join(clear_number)
    return print(f"Ваш номер телефону: {phone_number}")
    
while True:
    try:
        phone_number = input("Введіть номер телефону: ")
        normalize_phone(phone_number)
        break
    except ValueError:
        print("Невірний номер!")
    continue
