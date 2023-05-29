wallet = input("Введите вашу сумму денег в кошельке: ")
price = input("Введите цену шоколадки в вашем магазине: ")

try:
    money_count = float(wallet)
    price_chocolate = float(price)
    chocolate = money_count/price_chocolate
    change = money_count % price_chocolate
except ValueError:
    print("Ошибка, вы ввели не числа!")
except ZeroDivisionError:
    print("Вы не сможете купить шоколад :(")
else:
    print("Количество шоколадок, которые вы можете купить: ", chocolate)
    print("Ваша сдача: ", change)