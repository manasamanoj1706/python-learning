print("===== APPOINTMENT MANAGER =====")

appointments = []

while True:
    print("\n1. Add appointment")
    print("2. View appointments")
    print("3. Search appointment")
    print("4. Cancel appointment")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter person name: ")
        date = input("Enter date: ")
        time = input("Enter time: ")
        purpose = input("Enter purpose: ")

        if not name or not date or not time or not purpose:
            print("All details are required ❌")
        else:
            appointments.append({
                "name": name,
                "date": date,
                "time": time,
                "purpose": purpose
            })

            print("Appointment added successfully! ✅")

    elif choice == "2":
        if not appointments:
            print("No appointments scheduled.")

        else:
            print("\n===== APPOINTMENTS =====")

            for number, appointment in enumerate(appointments, start=1):
                print(
                    f"{number}. {appointment['name']} | "
                    f"{appointment['date']} | "
                    f"{appointment['time']} | "
                    f"{appointment['purpose']}"
                )

    elif choice == "3":
        search = input("Enter person's name: ")
        found = False

        for appointment in appointments:
            if appointment["name"].lower() == search.lower():
                print("\nAppointment found 🔎")
                print("Name:", appointment["name"])
                print("Date:", appointment["date"])
                print("Time:", appointment["time"])
                print("Purpose:", appointment["purpose"])
                found = True

        if not found:
            print("Appointment not found ❌")

    elif choice == "4":
        name = input("Enter person's name to cancel: ")
        found = False

        for appointment in appointments:
            if appointment["name"].lower() == name.lower():
                appointments.remove(appointment)
                print("Appointment cancelled! 🗑️")
                found = True
                break

        if not found:
            print("Appointment not found ❌")

    elif choice == "5":
        print("Appointment manager closed! 👋")
        break

    else:
        print("Invalid choice ❌")