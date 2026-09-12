print("===== MEDICINE REMINDER =====")

medicines = []

while True:
    print("\n1. Add medicine")
    print("2. View medicines")
    print("3. Mark medicine as taken")
    print("4. Search medicine")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Medicine name: ")
        time = input("Reminder time: ")

        if name.strip() == "" or time.strip() == "":
            print("Details cannot be empty ❌")
        else:
            medicines.append({
                "name": name,
                "time": time,
                "taken": False
            })

            print("Medicine reminder added! ✅")

    elif choice == "2":
        if not medicines:
            print("No medicines added.")

        else:
            print("\n===== MEDICINE LIST =====")

            for number, medicine in enumerate(medicines, start=1):
                status = "Taken" if medicine["taken"] else "Pending"

                print(
                    f"{number}. {medicine['name']} | "
                    f"Time: {medicine['time']} | "
                    f"Status: {status}"
                )

    elif choice == "3":
        name = input("Enter medicine name: ")

        found = False

        for medicine in medicines:
            if medicine["name"].lower() == name.lower():
                medicine["taken"] = True
                print("Medicine marked as taken! 💊✅")
                found = True
                break

        if not found:
            print("Medicine not found ❌")

    elif choice == "4":
        search = input("Search medicine: ")
        found = False

        for medicine in medicines:
            if search.lower() in medicine["name"].lower():
                print(
                    f"{medicine['name']} - "
                    f"{medicine['time']}"
                )
                found = True

        if not found:
            print("No matching medicine found ❌")

    elif choice == "5":
        print("Reminder system closed. 👋")
        break

    else:
        print("Invalid choice ❌")