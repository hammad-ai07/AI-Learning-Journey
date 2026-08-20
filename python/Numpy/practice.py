import numpy as np
marks=np.array([85, 90, 78, 92, 88,77])
print("Marks:",marks)
print("Dimensions:",marks.ndim)
print("Shape:",marks.shape)
print("First marks:",marks[0])
print("Last marrks:",marks[-1])


student_marks = np.array([
    [85, 78, 92],
    [88, 76, 90],
    [70, 82, 75]
])
print("\nStudent Marks:")
print(student_marks)
print("Dimensions:",student_marks.ndim)
print("Shape:",student_marks.shape)
print("First student's first subject:", student_marks[0, 0])
print("Second student's third subject:", student_marks[1, 2])
print("Third student's second subject:", student_marks[2, 1])



# Slicing
print("First three:", marks[:3])
print("Last three:", marks[-3:])
print("Middle:", marks[1:4])

# Operations
print("After adding 5:", marks + 5)
print("After subtracting 5:", marks - 5)
print("Double marks:", marks * 2)

# Statistics
print("Total:", marks.sum())
print("Average:", marks.mean())
print("Highest:", marks.max())
print("Lowest:", marks.min())


print("Marks:", marks)

print("Above 80:", marks[marks > 80])

print("Below 70:", marks[marks < 70])

print("Marks >= 80:", marks[marks >= 80])

student_mark = marks.reshape(2, 3)

print("Original:")
print(marks)

print("Reshaped:")
print(student_mark)
# Zeros
zeros = np.zeros(5)
print("Zeros:", zeros)

# Ones
ones = np.ones(5)
print("Ones:", ones)

# Range
numbers = np.arange(1, 11)
print("Numbers:", numbers)

# Even numbers from 0 to 20
even_numbers = np.arange(0, 21, 2)
print("Even numbers:", even_numbers)

# Random marks
random_marks = np.random.randint(40, 101, 10)
print("Random marks:", random_marks)

# Analyze random marks
print("Average:", random_marks.mean())
print("Highest:", random_marks.max())
print("Lowest:", random_marks.min())

# Students who scored above 70
print("Above 70:", random_marks[random_marks > 70])