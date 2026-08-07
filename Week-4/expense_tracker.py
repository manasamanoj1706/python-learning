# Expense Tracker using File Handling

def add_expense():

    try:
        with open("expenses.txt", "a") as file:

            date = input("Enter Date (DD-MM-YYYY): ")
            category = input("Enter Category: ")
            amount = float(input("Enter Amount: "))

            file.write(f"{date},{category},{amount}\n")

            print("Expense Added Successfully!")

    except ValueError:
        print("Amount should be a number.")


def view_expenses():

    try:

        with open("expenses.txt", "r") as file:

            print("\n====== ALL EXPENSES ======")

            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("Expense file not found.")


def total_expense():

    try:

        total = 0

        with open("expenses.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                total += float(data[2])

        print(f"\nTotal Expense : ₹{total}")

    except FileNotFoundError:
        print("Expense file not found.")

    except ValueError:
        print("Invalid data found in file.")


while True:

    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expense")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")