number = input("Введите число: ")

try:
    number = int(number)
except ValueError:
    print("Ошибка! Введите число!")
else:
    while number >= 0:
        print(number)
        number = number - 1
print("Конец")













