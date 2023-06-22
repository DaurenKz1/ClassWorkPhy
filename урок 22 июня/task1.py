numbers = input("Введите 5 чисел: ").split(",")
print(numbers)

numbers = [int(num) for num in numbers]

sum_numbers = sum(numbers)
print(sum_numbers)

average = sum_numbers/len(numbers)
print(average)
