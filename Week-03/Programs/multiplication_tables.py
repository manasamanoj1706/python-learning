# ==========================================
# Day 13 - Multiplication Tables
# Author: Manasa Manoj
# ==========================================

start = int(input("Enter starting table: "))
end = int(input("Enter ending table: "))

for table in range(start, end + 1):

    print("\n===================")
    print("Table of", table)
    print("===================")

    for i in range(1, 11):
        print(f"{table} x {i} = {table * i}")
