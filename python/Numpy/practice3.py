import numpy as np

subjects = np.array([
    "AI", "Python", "AI", "Math",
    "Python", "AI", "Math", "Python",
    "AI", "Math"
])
unique_subjects= np.unique(subjects)
unique_subjects_count = np.unique(subjects, return_counts=True)
print("Subjects:", subjects)
print("Unique Subjects:", unique_subjects)
print("Unique Subjects Count:", unique_subjects_count)

marks = np.array([56, 91, 73, 88, 45, 97, 82, 69])
ascending = np.sort(marks)
descending = ascending[::-1]      #list[start : stop : step]
print("Original:", marks)
print("Ascending:", ascending)
print("Descending:", descending)

highest_index = np.argmax(marks)
lowest_index = np.argmin(marks)

print("Highest marks:", marks[highest_index])
print("Highest marks index:", highest_index)

print("Lowest marks:", marks[lowest_index])
print("Lowest marks index:", lowest_index)

marks_sheet = np.array([
    [80, 75, 90],
    [65, 88, 72],
    [92, 95, 89],
    [55, 60, 58],
    [85, 78, 91]
])

print("Highest mark overall:", marks_sheet.max())
print("Highest mark position:", np.unravel_index(np.argmax(marks_sheet), marks_sheet.shape))

print("Lowest mark overall:", marks_sheet.min())
print("Lowest mark position:", np.unravel_index(np.argmin(marks_sheet), marks_sheet.shape))

# 1. 70 se 90 ke darmiyan marks
between = marks[(marks >= 70) & (marks <= 90)]
print("70-90:", between)

# 2. 50 se kam YA 90 se zyada marks
extreme = marks[(marks < 50) | (marks > 90)]
print("Extreme:", extreme)

# 3. 80 ya us se zyada marks
above_80 = marks[marks >= 80]
print("80+:", above_80)




scores = np.array([
    [78, 85, 92],
    [65, 72, 70],
    [90, 95, 88],
    [55, 60, 58],
    [82, 79, 91]
])

print("Scores:")
print(scores)

student_totals = scores.sum(axis=1)
print("Student totals:", student_totals)

student_averages = scores.mean(axis=1)
print("Student averages:", student_averages)

subject_averages = scores.mean(axis=0)
print("Subject averages:", subject_averages)

highest = scores.max()
highest_position = np.unravel_index(np.argmax(scores), scores.shape)

print("Overall highest:", highest)
print("Highest position:", highest_position)

lowest = scores.min()
lowest_position = np.unravel_index(np.argmin(scores), scores.shape)

print("Overall lowest:", lowest)
print("Lowest position:", lowest_position)

# 6. Student result
results = np.where(
    student_averages >= 80,
    "Excellent",
    np.where(
        student_averages >= 60,
        "Pass",
        "Fail"
    )
)

print("Student results:", results)

# 7. Ascending and descending order
ascending = np.sort(scores)
descending = ascending[:, ::-1]

print("Ascending:")
print(ascending)

print("Descending:")
print(descending)