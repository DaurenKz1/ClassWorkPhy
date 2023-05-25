hour = input("Введите часы: ")
minute = input("Введите минуты: ")
second = input("Введите секунды: ")


try:
    hours = int(hour)
    minutes = int(minute)
    seconds = int(second)
except ValueError:
    print("Ошибка, вы ввели не число!")
else:
    remaining_hours = 24 - hours
    remaining_minutes = 60 - minutes
    remaining_seconds = 60 - seconds

    total = remaining_hours * 60 * 60 + remaining_minutes * 60 + remaining_seconds
    print("Осталось секунд: ", total)
