# ==========================================
# Day 13 - Student Marks Analyzer
# Author: Manasa Manoj
# ==========================================

students = int(input("Enter number of students: "))

highest = 0
lowest = 100
total = 0

for i in range(1, students + 1):

    mark = int(input(f"Enter mark of Student {i}: "))

    total += mark

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

average = total / students

print("\n========== RESULT ==========")
print("Highest Mark :", highest)
print("Lowest Mark :", lowest)
print("Average :", average)
