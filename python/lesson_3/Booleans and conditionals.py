def check_number(num):
    """Check if the number is positive, negative, or zero."""
    if num > 0:
        return f"{num} is positive."
    elif num < 0:
        return f"{num} is negative."
    else:
        return f"{num} is zero."

def check_even_odd(num):
    """Check if the number is even or odd."""
    if num % 2 == 0:
        return f"{num} is even."
    else:
        return f"{num} is odd."

def can_vote(age):
    """Check if the person is eligible to vote."""
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

def largest(a, b, c):
    """Return the largest of three numbers."""
    if a >= b and a >= c:
        return f"The largest number is {a}."
    elif b >= a and b >= c:
        return f"The largest number is {b}."
    else:
        return f"The largest number is {c}."

def get_grade(marks):
    """Return the grade based on marks."""
    if marks >= 90:
        return "Grade: A"
    elif marks >= 80:
        return "Grade: B"
    elif marks >= 70:
        return "Grade: C"
    elif marks >= 60:
        return "Grade: D"
    else:
        return "Grade: F"
def login(username, password):
    """Check if the username and password are correct."""
    correct_username = "admin"
    correct_password = "password123"
    
    if username == correct_username and password == correct_password:
        return "Login successful."
    else:
        return "Invalid username or password."
def should_take_umbrella(weather):
    """Check if you should take an umbrella based on the weather."""
    if weather.lower() in ["rainy", "stormy"]:
        return "You should take an umbrella."
    else:
        return "No need for an umbrella."

def is_adult(age):
    """Check if the person is an adult."""
    if age >= 18:
        return "You are an adult."
    else:
        return "You are not an adult."
check_number(10)
print(can_vote(20))
print(largest(10, 20, 30))
print(get_grade(85))
print(login("admin", "password123"))
print(should_take_umbrella("rainy"))
print(is_adult(20))
