def get_modulo(num1,num2):
    divide = num1/num2
    whole_part = int(divide)
    result = num1 - (whole_part * num2)
    return result
result = get_modulo(23,4)
print(result)

