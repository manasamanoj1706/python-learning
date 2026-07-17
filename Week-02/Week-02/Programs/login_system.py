# Login System
# Day 10 - Nested if Statements

correct_username = "admin"
correct_password = "python123"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username:
    if password == correct_password:
        print("Login Successful ✅")
    else:
        print("Wrong Password ❌")
else:
    print("Username Not Found ❌")
