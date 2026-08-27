# Simple Password Manager

passwords = {}


def add_account():
    try:
        website = input("Enter website: ").strip()
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if not website or not username or not password:
            raise ValueError("All fields are required.")

        passwords[website] = {
            "username": username,
            "password": password
        }

        print("Account saved successfully!")

    except ValueError as error:
        print("Error:", error)


def view_accounts():

    if not passwords:
        print("\nNo accounts saved.")
        return

    print("\n========== SAVED ACCOUNTS ==========")

    for number, (website, details) in enumerate(
        passwords.items(), start=1
    ):
        print("\nAccount", number)
        print("Website :", website)
        print("Username:", details["username"])
        print("Password:", "*" * len(details["password"]))


def search_account():

    website = input("Enter website to search: ").strip()

    if website in passwords:
        details = passwords[website]

        print("\nAccount Found!")
        print("Website :", website)
        print("Username:", details["username"])
        print("Password:", details["password"])
    else:
        print("Account not found.")


def delete_account():

    website = input("Enter website to delete: ").strip()

    if website in passwords:
        del passwords[website]
        print("Account deleted successfully!")
    else:
        print("Account not found.")


def main():

    while True:

        print("\n================================")
        print("       PASSWORD MANAGER")
        print("================================")
        print("1. Add Account")
        print("2. View Accounts")
        print("3. Search Account")
        print("4. Delete Account")
        print("5. Exit")
        print("================================")

        choice = input("Enter choice: ")

        if choice == "1":
            add_account()

        elif choice == "2":
            view_accounts()

        elif choice == "3":
            search_account()

        elif choice == "4":
            delete_account()

        elif choice == "5":
            print("Password manager closed.")
            break

        else:
            print("Invalid choice.")


main()