# ============================================================
# Project Name : ASCII Art Generator
# Author       : Manasa Manoj
# Day          : 14
# Description  : Generates different ASCII art patterns
#                using nested loops.
# ============================================================

rows = int(input("Enter number of rows: "))

print("\n" + "=" * 50)
print("        ASCII ART GENERATOR")
print("=" * 50)

# ------------------------------------------------------------
# Pattern 1 : Hollow Square
# ------------------------------------------------------------
print("\n1. Hollow Square\n")

for i in range(rows):
    for j in range(rows):

        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# ------------------------------------------------------------
# Pattern 2 : X Pattern
# ------------------------------------------------------------
print("\n2. X Pattern\n")

for i in range(rows):
    for j in range(rows):

        if i == j or i + j == rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# ------------------------------------------------------------
# Pattern 3 : Checkerboard
# ------------------------------------------------------------
print("\n3. Checkerboard Pattern\n")

for i in range(rows):
    for j in range(rows):

        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print("-", end=" ")

    print()

print("\n" + "=" * 50)
print("ASCII Art Generation Completed!")
print("=" * 50)
