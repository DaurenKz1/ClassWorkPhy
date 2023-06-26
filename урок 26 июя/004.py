
def find_local_extremes(temperatures):
    n = len(temperatures)
    extremes = []

    # Проверяем каждый день, кроме первого и последнего
    for i in range(1, n - 1):
        if temperatures[i] > temperatures[i - 1] and temperatures[i] > temperatures[i + 1]:
            # Текущий день - локальный максимум
            extremes.append((i + 1, temperatures[i], "максимум"))
        elif temperatures[i] < temperatures[i - 1] and temperatures[i] < temperatures[i + 1]:
            # Текущий день - локальный минимум
            extremes.append((i + 1, temperatures[i], "минимум"))

    return extremes


# Пример использования функции
temperatures = [23, 20, 21, 24, 25, 22, 19, 18, 20, 23, 25, 24, 21]
extremes = find_local_extremes(temperatures)

# Выводим результаты
print("Максимумы:")
for day, temperature, ext_type in extremes:
    if ext_type == "максимум":
        print(f"День {day} - {temperature}°")

print("\nМинимумы:")
for day, temperature, ext_type in extremes:
    if ext_type == "минимум":
        print(f"День {day} - {temperature}°")