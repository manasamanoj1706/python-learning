print("===== PARKING SLOT FINDER =====")

slots = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None
}

while True:
    print("\n1. Park vehicle")
    print("2. Remove vehicle")
    print("3. View slots")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        vehicle = input("Enter vehicle number: ")

        for slot, parked_vehicle in slots.items():
            if parked_vehicle is None:
                slots[slot] = vehicle
                print(f"Vehicle parked in slot {slot} 🚗")
                break
        else:
            print("No parking slots available ❌")

    elif choice == "2":
        try:
            slot = int(input("Enter slot number: "))

            if slot not in slots:
                raise ValueError("Invalid slot number")

            if slots[slot] is None:
                print("Slot is already empty.")

            else:
                print(f"{slots[slot]} removed.")
                slots[slot] = None

        except ValueError as error:
            print("Error:", error)

    elif choice == "3":
        print("\n===== PARKING STATUS =====")

        for slot, vehicle in slots.items():
            status = vehicle if vehicle else "Empty"
            print(f"Slot {slot}: {status}")

    elif choice == "4":
        print("Parking system closed 👋")
        break

    else:
        print("Invalid choice ❌")