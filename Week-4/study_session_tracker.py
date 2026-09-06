print("===== STUDY SESSION TRACKER =====")

sessions = []

while True:
    print("\n1. Add study session")
    print("2. View sessions")
    print("3. Calculate total study time")
    print("4. Find longest session")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        subject = input("Enter subject: ")

        try:
            minutes = int(input("Enter study time (minutes): "))

            if minutes <= 0:
                raise ValueError("Time must be greater than 0")

            sessions.append({
                "subject": subject,
                "minutes": minutes
            })

            print("Study session added! 📚")

        except ValueError as error:
            print("Error:", error)

    elif choice == "2":
        if not sessions:
            print("No study sessions yet.")

        else:
            print("\n===== STUDY SESSIONS =====")

            for session in sessions:
                print(
                    f"{session['subject']} - "
                    f"{session['minutes']} minutes"
                )

    elif choice == "3":
        total = sum(session["minutes"] for session in sessions)

        print(f"Total study time: {total} minutes")

    elif choice == "4":
        if not sessions:
            print("No sessions available.")

        else:
            longest = max(sessions, key=lambda x: x["minutes"])

            print(
                f"Longest session: {longest['subject']} "
                f"({longest['minutes']} minutes)"
            )

    elif choice == "5":
        print("Keep studying! 🚀")
        break

    else:
        print("Invalid choice ❌")