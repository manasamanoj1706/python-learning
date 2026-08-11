# Number Validation Program

def get_number():
    while True:
        try:
            number = int(input("Enter a number: "))

            if number > 0:
                print("Positive number")
            elif number < 0:
                print("Negative number")
            else:
                print("Zero")

            return number

        except ValueError:
            print("Invalid input! Please enter a number.")


def check_number(number):

    if number % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")


print("===== NUMBER VALIDATION PROGRAM =====")

number = get_number()

check_number(number)

print("Program completed successfully.")