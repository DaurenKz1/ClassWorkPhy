import random

def get_random_int(min,max):
    number = random.random() * (max - min)
    number += min     
    return int(number)

my_random = get_random_int(1,100)

def game():
    user_number = input("Угадай число от 1 до 100: ")
    try:
        user_number = int(user_number)
    except ValueError:
        print("Ошибка! Введите целое число.")
        game()
    else:
        if user_number < my_random:
            print("Нужно ввести число побольше!")
        elif user_number > my_random:
            print("Нужно ввести число поменьше!")
        elif user_number == my_random:
            print("Вы выиграли!")
            return 
        game()

game()