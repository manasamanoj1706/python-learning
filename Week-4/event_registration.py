print("===== EVENT REGISTRATION =====")

registrations = []

while True:
    print("\n1. Register")
    print("2. View participants")
    print("3. Search participant")
    print("4. Show participant count")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter participant name: ")
        email = input("Enter email: ")

        if name == "" or email == "":
            print("Name and email cannot be empty ❌")

        else:
            participant = {
                "name": name,
                "email": email
            }

            registrations.append(participant)
            print("Registration successful! ✅")

    elif choice == "2":
        if not registrations:
            print("No participants registered.")

        else:
            print("\n===== PARTICIPANTS =====")

            for i, participant in enumerate(registrations, start=1):
                print(f"{i}. {participant['name']} - {participant['email']}")

    elif choice == "3":
        search = input("Enter participant name: ")
        found = False

        for participant in registrations:
            if participant["name"].lower() == search.lower():
                print("Participant found! 🔎")
                print("Name:", participant["name"])
                print("Email:", participant["email"])
                found = True
                break

        if not found:
            print("Participant not found ❌")

    elif choice == "4":
        print(f"Total participants: {len(registrations)}")

    elif choice == "5":
        print("Thank you! 👋")
        break

    else:
        print("Invalid choice ❌")