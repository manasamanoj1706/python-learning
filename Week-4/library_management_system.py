# Library Management System

def add_book():
    with open("library.txt", "a") as file:

        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        category = input("Enter Category: ")
        copies = input("Enter Number of Copies: ")

        file.write(f"Book ID : {book_id}\n")
        file.write(f"Title : {title}\n")
        file.write(f"Author : {author}\n")
        file.write(f"Category : {category}\n")
        file.write(f"Copies : {copies}\n")
        file.write("-" * 40 + "\n")

        print("Book added successfully!")


def view_books():

    try:

        with open("library.txt", "r") as file:

            data = file.read()

            if data:
                print("\n========== LIBRARY BOOKS ==========\n")
                print(data)
            else:
                print("No books available.")

    except FileNotFoundError:
        print("Library file not found.")


def search_book():

    try:

        title = input("Enter Book Title: ").lower()

        with open("library.txt", "r") as file:

            lines = file.readlines()

            found = False

            for line in lines:

                if title in line.lower():
                    found = True

                if found:
                    print(line, end="")

                    if "----------------------------------------" in line:
                        break

            if not found:
                print("Book not found.")

    except FileNotFoundError:
        print("Library file not found.")


def count_books():

    try:

        count = 0

        with open("library.txt", "r") as file:

            for line in file:

                if line.startswith("Book ID"):
                    count += 1

        print("Total Books :", count)

    except FileNotFoundError:
        print("Library file not found.")


while True:

    print("\n===================================")
    print(" LIBRARY MANAGEMENT SYSTEM ")
    print("===================================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Count Books")
    print("5. Exit")
    print("===================================")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        count_books()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
