grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grades = []
for i in grades:
    average_grades.append(sum(i) / len(i))
students_sort = list(sorted(students))
average_score = dict(zip(students_sort, average_grades))
print(average_score)
