'''
print("1==1:", 1==1 )
print("1==2:", 1==2 )
print("1!=1:", 1!=1 )
print("1!=2:", 1!=2 )
print("1>1:", 1>1 )
print("1>2:", 1>2 )
'''

"""
cost = 100
if cost < 1000:
    print("Скидок нет")
elif cost < 2000:
    print("скидка 2%")
elif cost < 5000:
    print("скидка 10%")
else:
    print("Скидка 10%")
"""

name_input = input("Введите возраст: ")

try:
    name = int(name_input)
except ValueError:
    print("Введите ваш возраст!")
else:
    if  0 < name < 18:
        print("К сожалению вы не можете посетить наш сайт :(")
    elif name == 0:
        print("Вам не может быть 0 лет!")
    else:
        print("Добро Пожаловать!")







