hour = int(input("Введите часы: "))
minute = int(input("Введите минуты: "))
second = int(input("Введите секунды: "))

remaining_hours = 24 - hour
remaining_minutes = 60 - minute
remaining_seconds = 60 - second

total = remaining_hours * 60 * 60 + remaining_minutes * 60 + remaining_seconds
print("Осталось секунд: ", total)
