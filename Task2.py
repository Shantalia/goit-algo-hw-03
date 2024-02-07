import random


def get_numbers_ticket(min, max, quantity):
    lottery_numbers = set()
    while len(lottery_numbers) < quantity:
        lottery_numbers.add(random.randint(min,max))
    return sorted(lottery_numbers)

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