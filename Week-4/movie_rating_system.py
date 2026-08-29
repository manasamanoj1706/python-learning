# Movie Rating System

movies = {}


def add_movie():
    try:
        name = input("Enter movie name: ").strip()
        rating = float(input("Enter rating (1-10): "))

        if not name:
            raise ValueError("Movie name cannot be empty.")

        if rating < 1 or rating > 10:
            raise ValueError("Rating must be between 1 and 10.")

        movies[name] = rating

        print("Movie added successfully!")

    except ValueError as error:
        print("Error:", error)


def show_movies():

    if not movies:
        print("\nNo movies available.")
        return

    print("\n========== MOVIE RATINGS ==========")

    for number, (name, rating) in enumerate(movies.items(), start=1):
        print(f"{number}. {name} - {rating}/10")


def find_best_movie():

    if not movies:
        print("No movies available.")
        return

    best_movie = max(movies, key=movies.get)

    print("\n========== TOP RATED MOVIE ==========")
    print("Movie :", best_movie)
    print("Rating:", movies[best_movie], "/10")


def search_movie():

    name = input("Enter movie name: ").strip()

    if name in movies:
        print("Rating:", movies[name], "/10")
    else:
        print("Movie not found.")


def main():

    while True:

        print("\n==============================")
        print("      MOVIE RATING SYSTEM")
        print("==============================")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Find Best Movie")
        print("4. Search Movie")
        print("5. Exit")
        print("==============================")

        choice = input("Enter choice: ")

        if choice == "1":
            add_movie()

        elif choice == "2":
            show_movies()

        elif choice == "3":
            find_best_movie()

        elif choice == "4":
            search_movie()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


main()