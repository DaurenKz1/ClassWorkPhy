user_input_count = input("Введите количество смайликов: ")
user_input_smile = input("Введите какой смайлик вы хотите видеть: ")
try:
    user_input_count = int(user_input_count)
except ValueError:
    print("Ошибка! Введите число!")
if user_input_count is None or user_input_count < 0:
    print("Ошибка! Нужно ввести положительное число!")

else:
    i = 0
    while i < user_input_count:
        print(user_input_smile)
        i+=1
print("Конец!")