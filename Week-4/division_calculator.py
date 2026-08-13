# Division Calculator

def divide_numbers():

    try:
        first = int(input("Enter first number: "))
        second = int(input("Enter second number: "))

        result = first / second

        print("\n========== RESULT ==========")
        print("First Number  :", first)
        print("Second Number :", second)
        print("Result        :", result)

    except ValueError:
        print("Error: Please enter numbers only.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    finally:
        print("Division process completed.")


print("===== DIVISION CALCULATOR =====")

divide_numbers()