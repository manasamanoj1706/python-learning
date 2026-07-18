# =====================================
# Python Revision - Day 11
# Name: Manasa Manoj
# =====================================

print("=== Python Revision Day 11 ===")

# Variables
name = "Manasa"
age = 21
cgpa = 8.2
passed = True

print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Passed:", passed)

print()

# Arithmetic Operators
a = 20
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print()

# Comparison Operators
print("Age >= 18:", age >= 18)
print("Age == 21:", age == 21)

print()

# If-Else
if age >= 18:
    print("Status: Adult")
else:
    print("Status: Minor")

print()

# Grade Checker
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

print()

# Nested If
username = "admin"
password = "python123"

if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Username Not Found")

print()
print("Revision Completed Successfully!")
