# Contact Book using File Handling

def add_contact():

    try:

        with open("contacts.txt", "a") as file:

            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")

            file.write(f"{name},{phone},{email}\n")

            print("Contact Added Successfully!")

    except Exception as e:
        print("Error:", e)


def view_contacts():

    try:

        with open("contacts.txt", "r") as file:

            print("\n========== CONTACT LIST ==========\n")

            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("No contacts found.")


def search_contact():

    try:

        search = input("Enter Name to Search: ").lower()

        found = False

        with open("contacts.txt", "r") as file:

            for line in file:

                if search in line.lower():
                    print("\nContact Found")
                    print(line.strip())
                    found = True

        if not found:
            print("Contact Not Found")

    except FileNotFoundError:
        print("No contacts found.")


def delete_contact():

    try:

        name = input("Enter Name to Delete: ").lower()

        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

        with open("contacts.txt", "w") as file:

            deleted = False

            for contact in contacts:

                if name not in contact.lower():
                    file.write(contact)
                else:
                    deleted = True

        if deleted:
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found")

    except FileNotFoundError:
        print("No contacts found.")


while True:

    print("\n================================")
    print("      CONTACT BOOK SYSTEM")
    print("================================")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print("================================")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")