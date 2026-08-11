# Simple Login System

correct_username = "manasa"
correct_password = "python123"


def login():
    try:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username == "" or password == "":
            raise ValueError("Username and password cannot be empty.")

        if username == correct_username and password == correct_password:
            print("\nLogin Successful!")
            return True

        print("\nInvalid Username or Password.")
        return False

    except ValueError as error:
        print("Error:", error)
        return False


print("========== LOGIN SYSTEM ==========")

attempts = 3

while attempts > 0:

    if login():
        break

    attempts -= 1
    print("Attempts remaining:", attempts)

    if attempts == 0:
        print("Account temporarily locked.")