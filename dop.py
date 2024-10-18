grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list = list(students)
sort_ = sorted(students)
print(sort_)
sum_sublist = [sum(sublist) for sublist in grades] # суммируем подсписки
print(sum_sublist, type(sum_sublist))
len_sublist = [len(sublist) for sublist in grades] # количество элементов в подсписках
print(len_sublist, type(len_sublist))
average_score = [a/b for a,b in zip(sum_sublist, len_sublist)]
print(average_score)
dict_ = dict(zip(sort_,average_score))
print(dict_)
