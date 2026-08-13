# Input Validator

def get_integer():
    while True:

        try:
            number = int(input("Enter an integer: "))
            print("Valid integer:", number)
            return number

        except ValueError:
            print("Invalid input! Please enter a number.")


def get_age():

    while True:

        try:
            age = int(input("Enter your age: "))

            if age < 0:
                print("Age cannot be negative.")
                continue

            print("Valid age:", age)
            return age

        except ValueError:
            print("Please enter a valid age.")


print("========== INPUT VALIDATOR ==========")

number = get_integer()
age = get_age()

print("\n========== RESULT ==========")
print("Number:", number)
print("Age:", age)
print("Program completed successfully.")