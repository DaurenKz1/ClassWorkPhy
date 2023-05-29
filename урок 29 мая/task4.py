hour = int(input("Введите ваш час: "))
minutes = int(input("Введите ваши минуты: "))
seconds = int(input("Введите ваши секнуды: "))

if 0 >= hour or hour > 24:
    print("Введите часы!")
if 0 >= minutes or minutes > 60:
    print("Введите минуты!")
if 0 >= seconds or seconds > 60:
    print("Введите секунды!")
else:
    print("Ваши данные корректны!")