def welcome():
    print("Welcome to the Python Learning Journey!")

def greet(name):
    print(f"Hello, {name}! Let's start learning Python.")

def add(a,b):
    return f"Addition result: {a + b}"
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is even."
    else:
        return f"{num} is odd."

def calculate_square(num):
    """Return the square of the given number."""
    return f"{num} squared is {num ** 2}"

def round_two_decimal(num):
    """Return the given number rounded to two decimal places."""
    return f"{num:.2f}"

def student_info(name, age, marks):
    """Display the student's name, age, and marks."""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Marks: {marks}")

welcome()
greet("Hammad")
print(add(5, 3))
print(check_even_odd(7))
print(calculate_square(4))
print(round_two_decimal(3.14159))
student_info("Hammad", 20, 85)