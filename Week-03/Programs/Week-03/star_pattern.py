# ============================================================
# Project Name : Star Pattern Generator
# Author       : Manasa Manoj
# Day          : 14
# Description  : Prints different star patterns using
#                nested loops in Python.
# ============================================================

print("=" * 45)
print("        STAR PATTERN GENERATOR")
print("=" * 45)

rows = int(input("Enter the number of rows: "))

# ------------------------------------------------------------
# Pattern 1 : Half Pyramid
# ------------------------------------------------------------
print("\n1. Half Pyramid\n")

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# ------------------------------------------------------------
# Pattern 2 : Inverted Half Pyramid
# ------------------------------------------------------------
print("\n2. Inverted Half Pyramid\n")

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# ------------------------------------------------------------
# Pattern 3 : Right Triangle using Numbers
# ------------------------------------------------------------
print("\n3. Number Triangle\n")

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# ------------------------------------------------------------
# Pattern 4 : Square Pattern
# ------------------------------------------------------------
print("\n4. Square Pattern\n")

for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()

print("\n" + "=" * 45)
print("Pattern Generation Completed Successfully!")
print("=" * 45)
