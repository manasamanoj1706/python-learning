# ==========================================================
# Project : ATM Simulator
# Author  : Manasa Manoj
# Day     : 16
# Description : Simple ATM using while loop
# ==========================================================

balance = 10000

while True:

    print("\n" + "=" * 40)
    print("        ATM SIMULATOR")
    print("=" * 40)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print(f"\nCurrent Balance: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))

        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Updated Balance: ₹{balance}")
        else:
            print("Invalid amount!")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Invalid amount!")

        elif amount > balance:
            print("Insufficient Balance!")

        else:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Remaining Balance: ₹{balance}")

    elif choice == "4":
        print("\nThank you for using our ATM!")
        break

    else:
        print("\nInvalid Choice! Please try again.")
