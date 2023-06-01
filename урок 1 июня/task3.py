def calculator(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Нельзя нелья делить на ноль")
    else:
        print("Введите знак!")

result = calculator("+", 10,24)
print(result)
result = calculator("-", 10,24)
print(result)
result = calculator("*", 10,24)
print(result)
result = calculator("/", 10,0)

if result is not None:
    print(result)