# ATM Simulator

balance = 10000
pin = 1234


def check_balance():
    print("\nCurrent Balance: ₹", balance)


def deposit():
    global balance

    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        balance += amount
        print("Deposit successful!")
        print("New Balance: ₹", balance)

    except ValueError as error:
        print("Error:", error)


def withdraw():
    global balance

    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Please collect your cash.")
            print("Remaining Balance: ₹", balance)

    except ValueError as error:
        print("Error:", error)


def atm():

    try:
        entered_pin = int(input("Enter your PIN: "))

        if entered_pin != pin:
            raise ValueError("Incorrect PIN.")

        print("\nLogin successful!")

        while True:

            print("\n========== ATM ==========")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                check_balance()

            elif choice == "2":
                deposit()

            elif choice == "3":
                withdraw()

            elif choice == "4":
                print("Thank you for using the ATM!")
                break

            else:
                print("Invalid choice.")

    except ValueError as error:
        print("Error:", error)

    finally:
        print("ATM session completed.")


atm()