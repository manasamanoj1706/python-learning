# Bank Account Management System

accounts = {}


def create_account():
    name = input("Enter account holder name: ")

    if name in accounts:
        print("Account already exists.")
        return

    try:
        initial_deposit = float(input("Enter initial deposit: "))

        if initial_deposit < 0:
            raise ValueError("Deposit cannot be negative.")

        accounts[name] = {
            "balance": initial_deposit,
            "transactions": []
        }

        accounts[name]["transactions"].append(
            f"Account created with ₹{initial_deposit}"
        )

        print("Account created successfully!")

    except ValueError as error:
        print("Error:", error)


def deposit():
    name = input("Enter account holder name: ")

    if name not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        accounts[name]["balance"] += amount
        accounts[name]["transactions"].append(
            f"Deposited ₹{amount}"
        )

        print("Deposit successful!")


    except ValueError as error:
        print("Error:", error)


def withdraw():
    name = input("Enter account holder name: ")

    if name not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if amount > accounts[name]["balance"]:
            print("Insufficient balance.")
            return

        accounts[name]["balance"] -= amount
        accounts[name]["transactions"].append(
            f"Withdrawn ₹{amount}"
        )

        print("Withdrawal successful!")

    except ValueError as error:
        print("Error:", error)


def check_balance():
    name = input("Enter account holder name: ")

    if name not in accounts:
        print("Account not found.")
        return

    print("Account Holder:", name)
    print("Balance: ₹", accounts[name]["balance"])


def transaction_history():
    name = input("Enter account holder name: ")

    if name not in accounts:
        print("Account not found.")
        return

    print("\n========== TRANSACTION HISTORY ==========")

    for transaction in accounts[name]["transactions"]:
        print("-", transaction)


def main():

    while True:

        print("\n================================")
        print("       BANK ACCOUNT SYSTEM")
        print("================================")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            check_balance()

        elif choice == "5":
            transaction_history()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


main()