# ==========================================
# Day 13 - Number Analyzer
# Author: Manasa Manoj
# ==========================================

print("========== NUMBER ANALYZER ==========")

number = int(input("Enter a positive number: "))

print("\nNumbers from 1 to", number)

total = 0
even_count = 0
odd_count = 0

for i in range(1, number + 1):
    print(i)

    total += i

    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\n========== RESULT ==========")
print("Sum of numbers :", total)
print("Even numbers :", even_count)
print("Odd numbers :", odd_count)
