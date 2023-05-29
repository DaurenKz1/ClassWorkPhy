import math
count = input("Введите количество сторон многоугольника: ")
diametr = input("Введите диаметр окружности: ")
try:
    n = float(count)
    d = float(diametr)
except ValueError:
    result = "Введите числа!"
else:
    result = d*math.sin(math.pi/n)
print(result)