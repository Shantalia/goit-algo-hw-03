import re

def normalize_phone(phone_number):
    code = "+38"
    our_digits = r"[+]?\d+"
    clear_number = []
    for ch in re.findall(our_digits, phone_number):
        clear_number.append(ch)
    phone_number = ""    
    phone_number = phone_number.join(clear_number)
    length = len(phone_number)
    if length > 10:
        number_without_code =  phone_number[-10:]
        clear_number = number_without_code
        string = ""
        for i in code:
            string += i
            if phone_number.startswith(string):
                if phone_number[:3] == code:
                    break
                else:
                    print("Це не український номер!")
                    return ""
            else:
                code = string
            phone_number = ""
            phone_number = code + phone_number.join(clear_number)
    elif length == 10:
        phone_number = ""
        phone_number = code + phone_number.join(clear_number)
    else:
        print("Це не український номер!")
        return ""
    return f"Ваш номер телефону: {phone_number}"

while True:
    try:
        phone_number = input("Введіть номер телефону: ")
        print(normalize_phone(phone_number))
        break
    except ValueError:
        print("Невірний номер!")
    continue
