# ===========================================
# Project : Movie Collection Manager
# Author  : Manasa Manoj
# Day     : 19
# ===========================================

movies = []

while True:
    print("\n===== Movie Collection Manager =====")
    print("1. Add Movie")
    print("2. Insert Movie")
    print("3. Remove Movie")
    print("4. View Movies")
    print("5. Sort Movies")
    print("6. Reverse Movie List")
    print("7. Search Movie")
    print("8. Total Movies")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        movie = input("Enter movie name: ")
        movies.append(movie)
        print("Movie added successfully!")

    elif choice == "2":
        movie = input("Enter movie name: ")
        index = int(input("Enter position: "))

        if 0 <= index <= len(movies):
            movies.insert(index, movie)
            print("Movie inserted successfully!")
        else:
            print("Invalid position!")

    elif choice == "3":
        movie = input("Enter movie name to remove: ")

        if movie in movies:
            movies.remove(movie)
            print("Movie removed successfully!")
        else:
            print("Movie not found!")

    elif choice == "4":
        if len(movies) == 0:
            print("No movies available.")
        else:
            print("\n===== Movie Collection =====")
            for i, movie in enumerate(movies, start=1):
                print(f"{i}. {movie}")

    elif choice == "5":
        movies.sort()
        print("Movies sorted successfully!")

    elif choice == "6":
        movies.reverse()
        print("Movie list reversed!")

    elif choice == "7":
        movie = input("Enter movie name to search: ")

        if movie in movies:
            print(movie, "is available in your collection.")
        else:
            print(movie, "not found.")

    elif choice == "8":
        print("Total Movies:", len(movies))

    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
