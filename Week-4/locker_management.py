print("===== LOCKER MANAGEMENT SYSTEM =====")

lockers = {}

while True:
    print("\n1. Assign locker")
    print("2. Release locker")
    print("3. Check locker")
    print("4. View all lockers")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            locker_no = int(input("Enter locker number: "))

            if locker_no <= 0:
                raise ValueError("Locker number must be positive.")

            if locker_no in lockers:
                print("Locker is already occupied ❌")
            else:
                name = input("Enter user name: ")

                if not name.strip():
                    print("Name cannot be empty ❌")
                else:
                    lockers[locker_no] = name
                    print("Locker assigned successfully! 🔒")

        except ValueError as error:
            print("Error:", error)

    elif choice == "2":
        try:
            locker_no = int(input("Enter locker number: "))

            if locker_no in lockers:
                del lockers[locker_no]
                print("Locker released successfully! ✅")
            else:
                print("Locker is already empty.")

        except ValueError:
            print("Enter a valid locker number.")

    elif choice == "3":
        try:
            locker_no = int(input("Enter locker number: "))

            if locker_no in lockers:
                print(f"Locker {locker_no} is occupied by {lockers[locker_no]}.")
            else:
                print(f"Locker {locker_no} is available.")

        except ValueError:
            print("Enter a valid locker number.")

    elif choice == "4":
        if not lockers:
            print("No lockers are currently occupied.")

        else:
            print("\n===== OCCUPIED LOCKERS =====")

            for locker_no, name in lockers.items():
                print(f"Locker {locker_no}: {name}")

    elif choice == "5":
        print("Locker system closed! 👋")
        break

    else:
        print("Invalid choice ❌")