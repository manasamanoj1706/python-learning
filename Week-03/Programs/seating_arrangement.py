# ======================================================
# Project : Seating Arrangement Generator
# Author  : Manasa Manoj
# Day     : 15
# ======================================================

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of seats per row: "))

print("\n========== CLASSROOM SEATING ==========\n")

seat_number = 1

for i in range(1, rows + 1):

    print(f"Row {i}:")

    for j in range(1, cols + 1):

        print(f"S{seat_number}", end="\t")
        seat_number += 1

    print("\n")

print("=" * 40)
print("Total Seats :", rows * cols)
print("Arrangement Generated Successfully!")
