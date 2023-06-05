import random


def get_random_int(min,max):
    number = random.random() * (max - min)
    number += min     
    return int(number)
 

my_int = get_random_int(3,15)
print(my_int)
