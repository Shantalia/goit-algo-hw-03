import random


def get_numbers_ticket(min, max, quantity):
    lottery_numbers = []
    i = 0
    while i < quantity:
        lottery_numbers.append(random.randint(min,max))
        clear_lottery_list = set(lottery_numbers)
        if len(clear_lottery_list) != len(lottery_numbers):
            lottery_numbers = list(clear_lottery_list)
        else:
            lottery_numbers = list(clear_lottery_list)
            lottery_numbers.sort()
            i+=1           
    return f"Ваші лотерейні числа: {lottery_numbers}"

while True:
    try:
        min = int(input("Введіть ціле число не менше 1: "))
        max = int(input("Введіть ціле число не більше 1000: "))
        quantity = int(input(f"Введіть ціле число в диапазоні {min} і {max}: "))
        if (min < 1) or (max > 1000) or (quantity < min) or (quantity > max):
            print("Невірне значення!")
            continue
        else:
            print(get_numbers_ticket(min, max, quantity))
        break
    except ValueError:
        print('Невірний тип даних!\n', []) 