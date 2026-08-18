# Smart Parking Management System

parking_slots = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None
}


def show_slots():
    print("\n========== PARKING SLOTS ==========")

    for slot, vehicle in parking_slots.items():

        if vehicle is None:
            print(f"Slot {slot}: Available")
        else:
            print(f"Slot {slot}: {vehicle}")


def park_vehicle():

    try:
        show_slots()

        slot = int(input("\nEnter slot number: "))

        if slot not in parking_slots:
            raise ValueError("Invalid slot number.")

        if parking_slots[slot] is not None:
            print("This slot is already occupied.")
            return

        vehicle = input("Enter vehicle number: ").strip()

        if vehicle == "":
            raise ValueError("Vehicle number cannot be empty.")

        parking_slots[slot] = vehicle

        print("Vehicle parked successfully!")

    except ValueError as error:
        print("Error:", error)


def remove_vehicle():

    try:
        slot = int(input("Enter slot number: "))

        if slot not in parking_slots:
            raise ValueError("Invalid slot number.")

        if parking_slots[slot] is None:
            print("Slot is already empty.")
            return

        vehicle = parking_slots[slot]
        parking_slots[slot] = None

        print(f"{vehicle} removed successfully!")

    except ValueError as error:
        print("Error:", error)


def search_vehicle():

    vehicle = input("Enter vehicle number: ").strip()

    for slot, parked_vehicle in parking_slots.items():

        if parked_vehicle == vehicle:
            print(f"Vehicle found in Slot {slot}")
            return

    print("Vehicle not found.")


def available_slots():

    count = 0

    for vehicle in parking_slots.values():

        if vehicle is None:
            count += 1

    print("\nAvailable Slots:", count)


def main():

    while True:

        print("\n================================")
        print("    SMART PARKING MANAGEMENT")
        print("================================")
        print("1. Show Parking Slots")
        print("2. Park Vehicle")
        print("3. Remove Vehicle")
        print("4. Search Vehicle")
        print("5. Available Slots")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_slots()

        elif choice == "2":
            park_vehicle()

        elif choice == "3":
            remove_vehicle()

        elif choice == "4":
            search_vehicle()

        elif choice == "5":
            available_slots()

        elif choice == "6":
            print("Parking system closed.")
            break

        else:
            print("Invalid choice.")


main()