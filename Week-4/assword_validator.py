# Password Validator

def validate_password():

    try:
        password = input("Enter your password: ")

        if password == "":
            raise ValueError("Password cannot be empty.")

        if len(password) < 8:
            raise ValueError("Password must contain at least 8 characters.")

        if password.isdigit():
            raise ValueError("Password cannot contain only numbers.")

        if password.isalpha():
            raise ValueError("Password should contain numbers or special characters.")

        print("Password is valid!")

    except ValueError as error:
        print("Invalid Password:", error)


print("========== PASSWORD VALIDATOR ==========")

validate_password()

print("Program completed.")
