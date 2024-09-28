"""#grades

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades = sorted(grades)
sorted_grades.reverse()
print(sorted_grades)

average_grade_sum = sum(sorted_grades) 
average_grade = average_grade_sum / 10

print(average_grade)"""

"""#2 advanced methods
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve","Alice", "Frank"]

if "Alice" in submitted and "Alice" in attended:
    print("Yes")
else:
    pass"""

#3 slicing practice
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
all_da_hunnids = []
no_more_hunnids = [temperatures[23:]]
second_week_temps = [temperatures[7:14]]


all_da_hunnids.append(no_more_hunnids)

print(second_week_temps)
print(len(temperatures))
print(all_da_hunnids)
