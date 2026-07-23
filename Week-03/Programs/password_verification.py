# =====================================================
# Project : Password Verification System
# Author  : Manasa Manoj
# Day     : 16
# =====================================================

correct_password = "python123"

password = ""

attempts = 0

while password != correct_password:

    password = input("Enter Password: ")

    attempts += 1

    if password != correct_password:
        print("Incorrect Password\n")

print("\nAccess Granted!")
print("Attempts:", attempts)
