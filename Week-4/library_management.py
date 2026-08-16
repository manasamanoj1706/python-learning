# Library Management System

books = [
    "Python Programming",
    "Data Science",
    "Artificial Intelligence",
    "Machine Learning",
    "Web Development"
]

borrowed_books = []


def show_books():
    print("\n========== AVAILABLE BOOKS ==========")

    if len(books) == 0:
        print("No books available.")
        return

    for number, book in enumerate(books, start=1):
        print(number, ".", book)


def borrow_book():

    try:
        show_books()

        if len(books) == 0:
            return

        choice = int(input("\nEnter book number to borrow: "))

        if choice < 1 or choice > len(books):
            raise ValueError("Invalid book number.")

        book = books.pop(choice - 1)
        borrowed_books.append(book)

        print("Book borrowed successfully!")
        print("Book:", book)

    except ValueError as error:
        print("Error:", error)


def return_book():

    try:

        if len(borrowed_books) == 0:
            print("No borrowed books.")
            return

        print("\n========== BORROWED BOOKS ==========")

        for number, book in enumerate(borrowed_books, start=1):
            print(number, ".", book)

        choice = int(input("Enter book number to return: "))

        if choice < 1 or choice > len(borrowed_books):
            raise ValueError("Invalid book number.")

        book = borrowed_books.pop(choice - 1)
        books.append(book)

        print("Book returned successfully!")
        print("Book:", book)

    except ValueError as error:
        print("Error:", error)


def show_borrowed_books():

    print("\n========== BORROWED BOOKS ==========")

    if len(borrowed_books) == 0:
        print("No borrowed books.")
    else:
        for book in borrowed_books:
            print("-", book)


def main():

    try:

        while True:

            print("\n================================")
            print("      LIBRARY MANAGEMENT")
            print("================================")
            print("1. Show Available Books")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Show Borrowed Books")
            print("5. Exit")
            print("================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                show_books()

            elif choice == "2":
                borrow_book()

            elif choice == "3":
                return_book()

            elif choice == "4":
                show_borrowed_books()

            elif choice == "5":
                print("Thank you for using the library!")
                break

            else:
                raise ValueError("Invalid menu choice.")

    except ValueError as error:
        print("Error:", error)

    finally:
        print("Library system closed.")


main()