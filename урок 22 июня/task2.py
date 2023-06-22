list1 = [1,2,3,4,5,6,7]
list2 = [7,6,5,4,3,2,1]

for i in range(len(list1)):
    if list1[i] == list2[i]:
        print(f"Значение на позиции {i} одинакова: {list1[i]}")
    else:
        print(f"Значение на позиции {i} отличается: {list1[i]} и {list2[i]}")