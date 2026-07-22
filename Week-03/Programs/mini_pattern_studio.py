# ======================================================
# Mini Pattern Studio
# Author : Manasa Manoj
# ======================================================

rows = int(input("Enter rows: "))

print("\n========== STAR PATTERN ==========\n")

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n========== REVERSE STAR ==========\n")

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n========== NUMBER PATTERN ==========\n")

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n========== REPEATED NUMBER ==========\n")

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()

print("\nThanks for using Mini Pattern Studio!")
