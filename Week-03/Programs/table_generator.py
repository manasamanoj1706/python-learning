# ======================================================
# Multiplication Table Studio
# Author : Manasa Manoj
# ======================================================

print("=" * 45)
print("MULTIPLICATION TABLE STUDIO")
print("=" * 45)

number = int(input("Enter a number: "))
limit = int(input("Enter table limit: "))

print()

for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")

print("\nProgram Completed Successfully!")
