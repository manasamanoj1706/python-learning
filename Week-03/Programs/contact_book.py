# ===========================================
# Project : Contact Book
# Author  : Manasa Manoj
# Day     : 19
# ===========================================

contacts = []

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. View Contacts")
    print("4. Search Contact")
    print("5. Sort Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        contacts.append(name)
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            contacts.remove(name)
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "3":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\n===== Contact List =====")
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. {contact}")

    elif choice == "4":
        name = input("Enter contact name to search: ")

        if name in contacts:
            print(name, "is available.")
        else:
            print("Contact not found!")

    elif choice == "5":
        contacts.sort()
        print("Contacts sorted successfully!")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
