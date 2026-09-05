print("===== MOVIE WATCHLIST =====")

watchlist = []

while True:
    print("\n1. Add movie")
    print("2. Mark as watched")
    print("3. View watchlist")
    print("4. Remove movie")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        movie = input("Enter movie name: ")

        if movie:
            watchlist.append({
                "name": movie,
                "watched": False
            })
            print("Movie added! 🎬")
        else:
            print("Movie name cannot be empty.")

    elif choice == "2":
        movie = input("Enter movie name: ")
        found = False

        for item in watchlist:
            if item["name"].lower() == movie.lower():
                item["watched"] = True
                print("Marked as watched! ✅")
                found = True
                break

        if not found:
            print("Movie not found ❌")

    elif choice == "3":
        if not watchlist:
            print("Your watchlist is empty.")

        else:
            print("\n===== WATCHLIST =====")

            for item in watchlist:
                status = "Watched ✅" if item["watched"] else "Not watched ⏳"
                print(f"{item['name']} - {status}")

    elif choice == "4":
        movie = input("Enter movie name to remove: ")
        found = False

        for item in watchlist:
            if item["name"].lower() == movie.lower():
                watchlist.remove(item)
                print("Movie removed! 🗑️")
                found = True
                break

        if not found:
            print("Movie not found ❌")

    elif choice == "5":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice ❌")