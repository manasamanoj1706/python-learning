# ============================================================
# Project Name : Number Pattern Generator
# Author       : Manasa Manoj
# Day          : 14
# Description  : Prints different number patterns using
#                nested loops.
# ============================================================

rows = int(input("Enter number of rows: "))

print("\nAscending Number Pattern\n")

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()

print("\nSequential Number Pattern\n")

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nReverse Number Pattern\n")

for i in range(rows, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()

print("\nProgram Finished Successfully!")
