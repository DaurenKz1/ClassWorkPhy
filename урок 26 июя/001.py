from random import randint

number1 = randint(-100,100)
number2 = randint(-100,100)

if number1 > number2:
    number1,number2 = number2,number1

numbers = [randint(number1,number2) for _ in range(10)]
print(numbers)

max_len = 1
cur_len = 1

for i in range(1,len(numbers)):
    if numbers[i] >= numbers[i-1]:
        cur_len += 1
    else:
        max_len = max(max_len,cur_len)
        cur_len = 1

max_len = max(max_len, cur_len)
print("Максимальная длина последоваельности чисел равна: ", max_len)
