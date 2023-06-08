number_user_input = input("Введите число: ")
try:
    number_user_input = int(number_user_input)
except ValueError:
    print("Ошибка! Введите число!")
else:
    factorial = 1
    counter = 1

    while counter <= number_user_input:
        factorial *= counter
        counter += 1

print("Факториал числа равен: ", factorial)