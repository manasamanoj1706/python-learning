# ===========================================
# Project : Library Book Management System
# Author  : Manasa Manoj
# Day     : 19
# ===========================================

books = []

while True:
    print("\n===== Library Book Manager =====")
    print("1. Add Book")
    print("2. Insert Book")
    print("3. Remove Book")
    print("4. View Books")
    print("5. Sort Books")
    print("6. Reverse Books")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        book = input("Enter book name: ")
        index = int(input("Enter index: "))

        if 0 <= index <= len(books):
            books.insert(index, book)
            print("Book inserted successfully!")
        else:
            print("Invalid index!")

    elif choice == "3":
        book = input("Enter book name to remove: ")

        if book in books:
            books.remove(book)
            print("Book removed successfully!")
        else:
            print("Book not found!")

    elif choice == "4":
        if len(books) == 0:
            print("Library is empty.")
        else:
            print("\nBooks Available:")
            for i, book in enumerate(books, start=1):
                print(f"{i}. {book}")

    elif choice == "5":
        books.sort()
        print("Books sorted successfully!")

    elif choice == "6":
        books.reverse()
        print("Books reversed successfully!")

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
