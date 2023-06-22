
numbers = []

while numbers < 10:
    input_str = input("Введите 10 чисел: ")

    try:
        number = int(input_str)
        numbers.append(number)
    except ValueError:
        print("Ошибка! Введите числа")