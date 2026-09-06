print("===== DIGITAL WALLET =====")

balance = 0
transactions = []

while True:
    print("\n1. Add money")
    print("2. Spend money")
    print("3. Check balance")
    print("4. Transaction history")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter amount to add: ₹"))

            if amount <= 0:
                raise ValueError("Amount must be greater than 0")

            balance += amount

            transactions.append({
                "type": "Added",
                "amount": amount
            })

            print(f"₹{amount:.2f} added successfully! 💰")

        except ValueError as error:
            print("Error:", error)

    elif choice == "2":
        try:
            amount = float(input("Enter amount to spend: ₹"))

            if amount <= 0:
                raise ValueError("Amount must be greater than 0")

            if amount > balance:
                print("Insufficient balance ❌")

            else:
                balance -= amount

                transactions.append({
                    "type": "Spent",
                    "amount": amount
                })

                print(f"₹{amount:.2f} spent successfully! ✅")

        except ValueError as error:
            print("Error:", error)

    elif choice == "3":
        print(f"Current balance: ₹{balance:.2f}")

    elif choice == "4":
        if not transactions:
            print("No transactions yet.")

        else:
            print("\n===== TRANSACTION HISTORY =====")

            for transaction in transactions:
                print(
                    f"{transaction['type']}: "
                    f"₹{transaction['amount']:.2f}"
                )

    elif choice == "5":
        print("Thank you for using Digital Wallet! 👋")
        break

    else:
        print("Invalid choice ❌")