#Пользователь вводит значения a и b для формулы a * x + b = 0, а программа считает и выводит значение x.

a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
x = -b / a
print("Значение x равно:", x)