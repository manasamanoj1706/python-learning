# Age Checker

def check_age():

    try:
        age = int(input("Enter your age: "))

        if age < 0:
            raise ValueError("Age cannot be negative.")

        if age < 13:
            print("Category: Child")
        elif age < 18:
            print("Category: Teenager")
        elif age < 60:
            print("Category: Adult")
        else:
            print("Category: Senior Citizen")

    except ValueError as error:
        print("Error:", error)

    finally:
        print("Age checking completed.")


check_age()
