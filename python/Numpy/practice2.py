import numpy as np

marks = np.array([
    [80, 70, 90],
    [85, 75, 95],
    [90, 80, 88]
])

print("Marks:")
print(marks)

print("Total:", marks.sum())

print("Column totals:", marks.sum(axis=0))

print("Row totals:", marks.sum(axis=1))
print("Column average:", marks.mean(axis=0))
print("Row average:", marks.mean(axis=1))

print("Highest in each subject:", marks.max(axis=0))
print("Highest for each student:", marks.max(axis=1))

print("Lowest in each subject:", marks.min(axis=0))
print("Lowest for each student:", marks.min(axis=1))
bonus = np.array([5, 10, 2])

new_marks = marks + bonus

print("Original marks:")
print(marks)

print("Bonus:")
print(bonus)

print("Marks after bonus:")
print(new_marks)



marks_sheet = np.array([45, 67, 82, 91, 55, 76, 88])

result = np.where(marks_sheet >= 80, "Excellent", "Normal")

print("Marks:", marks_sheet)
print("Result:", result)

# Bonus: 50 se kam marks ko "Fail" aur baqi ko "Pass" karo
result2 = np.where(marks_sheet < 50, "Fail", "Pass")

print("Pass/Fail:", result2)