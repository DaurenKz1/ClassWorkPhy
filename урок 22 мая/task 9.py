import math
dlina1_user_input = input("Введите длину 1 катета прямоугольного треугольника: ")
dlina2_user_input = input("Введите длину 2 катета прямоугольного треугольника: ")

try:
    katet1 = float(dlina1_user_input)
    katet2 = float(dlina2_user_input)
except ValueError:
    print("Ошибка! Вы не ввели число!")
else:
    sum_gipotenuza = katet1**2 + katet2**2 
    gipotenuza = math.sqrt(sum_gipotenuza)
    
    print("Ваша гипотенуза, вычисленная по теореме Пифагора равна :", gipotenuza)