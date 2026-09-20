print("===== ROOM BOOKING SYSTEM =====")

rooms = {
    101: None,
    102: None,
    103: None,
    104: None,
    105: None
}

while True:
    print("\n1. Book room")
    print("2. Check room")
    print("3. Cancel booking")
    print("4. View available rooms")
    print("5. View bookings")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            room = int(input("Enter room number: "))

            if room not in rooms:
                raise ValueError("Room does not exist.")

            if rooms[room] is not None:
                print("Room is already booked ❌")
            else:
                name = input("Enter guest name: ")

                if not name.strip():
                    print("Guest name cannot be empty ❌")
                else:
                    rooms[room] = name
                    print(f"Room {room} booked successfully! 🏨")

        except ValueError as error:
            print("Error:", error)

    elif choice == "2":
        try:
            room = int(input("Enter room number: "))

            if room not in rooms:
                raise ValueError("Room does not exist.")

            if rooms[room] is None:
                print(f"Room {room} is available ✅")
            else:
                print(f"Room {room} is booked by {rooms[room]}.")

        except ValueError as error:
            print("Error:", error)

    elif choice == "3":
        try:
            room = int(input("Enter room number: "))

            if room not in rooms:
                raise ValueError("Room does not exist.")

            if rooms[room] is None:
                print("Room is already available.")
            else:
                rooms[room] = None
                print("Booking cancelled successfully! ✅")

        except ValueError as error:
            print("Error:", error)

    elif choice == "4":
        print("\n===== AVAILABLE ROOMS =====")

        available = False

        for room, guest in rooms.items():
            if guest is None:
                print(f"Room {room}")
                available = True

        if not available:
            print("No rooms available.")

    elif choice == "5":
        print("\n===== CURRENT BOOKINGS =====")

        for room, guest in rooms.items():
            if guest is not None:
                print(f"Room {room}: {guest}")

    elif choice == "6":
        print("Thank you! 👋")
        break

    else:
        print("Invalid choice ❌")