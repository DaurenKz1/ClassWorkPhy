user_number = input("Введите число: ")
try:
    number = int(user_number)
except ValueError:
    print("Вы не ввели число!")
else:
    message = "Ваше число в"
    message += "\n - в двоичном виде: %s" % bin(number)
    message += "\n - в восьмиричном виде: %s" % oct(number)
    message += "\n - в щестнадцатиричном виде: %s" % hex(number)

print(message)