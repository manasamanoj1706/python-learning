# ============================================================
# Project : Advanced Pattern Collection
# Author  : Manasa Manoj
# Day     : 15
# ============================================================

rows = int(input("Enter number of rows: "))

print("\n========== Pattern 1 ==========\n")

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n========== Pattern 2 ==========\n")

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n========== Pattern 3 ==========\n")

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n========== Pattern 4 ==========\n")

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nPatterns Completed Successfully!")
