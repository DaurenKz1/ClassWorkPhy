keys = ['Dauren', 'Bekarys', 'Ramazan','Ali']
grades = [12,13,13,1]

#my_list = list(zip(keys,grades))
#my_list = list(zip(keys,grades,grades))
my_list = dict(zip(keys,grades))
my_dict = my_list.items()
print(my_list)
print(my_dict)