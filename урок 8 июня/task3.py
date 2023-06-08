number1_input = input("Введите 1 чило: ")
number2_input = input("Введите 2 чило: ")

try:
    number1_input = float(number1_input)
    number2_input = float(number2_input)
except ValueError:
    print("Ошибка! Введите числа!")
else:
    min_num = min(number1_input,number2_input)
    message = ""
    i = 1
    while i <= min_num:
        if number1_input % i == 0 and number2_input % i == 0:
            message += str(i) + " "
        i+=1
print("Общие делители чисел", number1_input, "и", number2_input, ":", message)