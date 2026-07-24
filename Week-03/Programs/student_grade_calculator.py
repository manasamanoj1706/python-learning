# ===========================================
# Project : Student Grade Calculator
# Author  : Manasa Manoj
# Day     : 17
# ===========================================

def calculate_total(m1, m2, m3):
    return m1 + m2 + m3

def calculate_average(total):
    return total / 3

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"

name = input("Enter Student Name: ")

mark1 = float(input("Enter Mark 1: "))
mark2 = float(input("Enter Mark 2: "))
mark3 = float(input("Enter Mark 3: "))

total = calculate_total(mark1, mark2, mark3)
average = calculate_average(total)
grade = calculate_grade(average)

print("\n===== RESULT =====")
print("Name    :", name)
print("Total   :", total)
print("Average :", round(average, 2))
print("Grade   :", grade)
