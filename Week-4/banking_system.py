# Simple Banking System

balance = 10000


def check_balance():
    print("\nCurrent Balance: ₹", balance)


def deposit():
    global balance

    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
        else:
            balance += amount
            print("Amount deposited successfully!")
            print("New Balance: ₹", balance)

    except ValueError:
        print("Please enter a valid number.")


def withdraw():
    global balance

    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")

        elif amount > balance:
            print("Insufficient balance.")

        else:
            balance -= amount
            print("Please collect your cash.")
            print("Remaining Balance: ₹", balance)

    except ValueError:
        print("Please enter a valid number.")


while True:

    print("\n==============================")
    print("       BANKING SYSTEM")
    print("==============================")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you for using our bank!")
            break

        else:
            raise ValueError("Invalid menu choice")

    except ValueError as error:
        print("Error:", error)