students = ["Даурен","Асанали","Матвей","Тамерлан","Максим","Даниял"]
marks = [12.0,9.132,10.923,11.93,5.5,11.57]

def make_groups(num):
    students_marks = []
    for i in range(len(students)):
        students_marks.append((students[i],marks[i]))

    sorted_students = sorted(students_marks,key=lambda x: x[1])
    group_size = len(students)//num
    groups = []
    start_index = 0

    for i in range(num):
     
        if i < len(students) % num:
            end_index = start_index + group_size + 1
        else:
            end_index = start_index + group_size

        
        current_group = []
        for j in range(start_index, end_index):
            current_group.append(sorted_students[j][0])

        groups.append(current_group)
        start_index = end_index

    return groups

groups = make_groups(3)
for i,group in enumerate(groups):
    print(f"Группа {i+1}: {group}")
