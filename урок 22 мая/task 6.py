s = input("Введите расстояние в км: ")
t = input("За сколько хотите добратсья: ")

try:
    distance = float(s)
    time = float(t)
    speed = distance/time
except ValueError:
    print("Ошибка! Вы ввели не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
else:
    print("Вам понадобится: ", speed)