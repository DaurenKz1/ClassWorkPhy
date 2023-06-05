def get_max(num1,num2 = 0, num3 = 0, num4 = 0):
    if num2 == 0 and num3 == 0 and num4 == 0:
        return num1
    elif num3 == 0 and num4 == 0:
        return max(num1,num2)
    elif num4 == 0:
        return max(num1,num2,num3)
    else:
        return max(num1,num2,num3,num4)

print(get_max(1,3,2,10))