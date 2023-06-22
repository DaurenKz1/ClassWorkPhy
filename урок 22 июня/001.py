#user_in = input("Введите числа через запятую: ")
#my_list = user_in.split(",")
#print(my_list)
#
#outut = ":".join(my_list)
#print(outut)

#list1 = [214112,4,23,4,1,43,1]
#list1.append(74498345)
#print(list1)
#
#list2 = [2411,234,1,41,2134]
#list2.extend(list1)
#print(list2)
#
#list2.insert(2,900000000000)
#print(list2)



#leap_years = [x + 2000 for x in range(0,30,4)]
#
#print(leap_years)
#1 TASK:
#numbers = input("Введите 5 чисел: ").split(",")
#print(numbers)
#
#numbers = [int(num) for num in numbers]
#
#sum_numbers = sum(numbers)
#print(sum_numbers)
#
#average = sum_numbers/len(numbers)
#print(average)

#№2 задача:

list1 = [1,2,3,4,5,6,7]
list2 = [7,6,5,4,3,2,1]

for i in range(len(list1)):
    if list1[i] == list2[i]:
        print(f"Значение на позиции {i} одинакова: {list1[i]}")
    else:
        print(f"Значение на позиции {i} отличается: {list1[i]} и {list2[i]}")

