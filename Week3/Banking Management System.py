# ==========================================
# BANKING MANAGEMENT SYSTEM
# Author : Manasa Manoj
# ==========================================

accounts = {}

def create_account():
    print("\n===== CREATE ACCOUNT =====")

    acc_no = int(input("Enter Account Number: "))

    if acc_no in accounts:
        print("Account already exists!")
        return

    name = input("Enter Customer Name: ")
    age = int(input("Enter Age: "))
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    pin = input("Set 4-digit PIN: ")
    balance = float(input("Enter Initial Deposit: "))

    accounts[acc_no] = {
        "name": name,
        "age": age,
        "phone": phone,
        "address": address,
        "pin": pin,
        "balance": balance,
        "transactions": []
    }

    accounts[acc_no]["transactions"].append(
        f"Account Created with ₹{balance}"
    )

    print("Account Created Successfully!")

def view_accounts():

    print("\n===== ALL ACCOUNTS =====")

    if len(accounts) == 0:
        print("No Accounts Found")
        return

    for acc_no, details in accounts.items():

        print("\n---------------------------")
        print("Account Number :", acc_no)

        for key, value in details.items():

            if key != "transactions":
                print(f"{key.capitalize()} : {value}")

def search_account():

    print("\n===== SEARCH ACCOUNT =====")

    acc_no = int(input("Enter Account Number: "))

    if acc_no not in accounts:
        print("Account Not Found")
        return

    print("\nAccount Details")

    for key, value in accounts[acc_no].items():

        if key != "transactions":
            print(f"{key.capitalize()} : {value}")

def deposit_money():

    print("\n===== DEPOSIT MONEY =====")

    acc_no = int(input("Enter Account Number: "))

    if acc_no not in accounts:
        print("Account Not Found")
        return

    amount = float(input("Enter Deposit Amount: "))

    accounts[acc_no]["balance"] += amount

    accounts[acc_no]["transactions"].append(
        f"Deposited ₹{amount}"
    )

    print("Amount Deposited Successfully!")

def withdraw_money():

    print("\n===== WITHDRAW MONEY =====")

    acc_no = int(input("Enter Account Number: "))

    if acc_no not in accounts:
        print("Account Not Found")
        return

    pin = input("Enter PIN: ")

    if pin != accounts[acc_no]["pin"]:
        print("Wrong PIN")
        return

    amount = float(input("Enter Withdrawal Amount: "))

    if amount > accounts[acc_no]["balance"]:
        print("Insufficient Balance")
        return

    accounts[acc_no]["balance"] -= amount

    accounts[acc_no]["transactions"].append(
        f"Withdrawn ₹{amount}"
    )

    print("Withdrawal Successful!")

while True:

    print("\n=================================")
    print("     BANKING MANAGEMENT SYSTEM")
    print("=================================")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Exit")
    print("=================================")

    choice = input("Enter Choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        view_accounts()

    elif choice == "3":
        search_account()

    elif choice == "4":
        deposit_money()

    elif choice == "5":
        withdraw_money()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")