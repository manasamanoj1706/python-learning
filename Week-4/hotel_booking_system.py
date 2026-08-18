# Hotel Booking System

rooms = {
    101: None,
    102: None,
    103: None,
    104: None,
    105: None
}


def show_rooms():
    print("\n========== HOTEL ROOMS ==========")

    for room, guest in rooms.items():

        if guest is None:
            print(f"Room {room}: Available")
        else:
            print(f"Room {room}: Booked by {guest}")


def book_room():

    try:
        show_rooms()

        room = int(input("\nEnter room number: "))

        if room not in rooms:
            raise ValueError("Invalid room number.")

        if rooms[room] is not None:
            print("Room is already booked.")
            return

        guest = input("Enter guest name: ").strip()

        if not guest:
            raise ValueError("Guest name cannot be empty.")

        rooms[room] = guest

        print("Room booked successfully!")

    except ValueError as error:
        print("Error:", error)


def cancel_booking():

    try:
        room = int(input("Enter room number: "))

        if room not in rooms:
            raise ValueError("Invalid room number.")

        if rooms[room] is None:
            print("Room is already available.")
            return

        guest = rooms[room]
        rooms[room] = None

        print(f"Booking for {guest} cancelled successfully.")

    except ValueError as error:
        print("Error:", error)


def search_guest():

    guest = input("Enter guest name: ").strip().lower()

    for room, name in rooms.items():

        if name is not None and name.lower() == guest:
            print(f"{guest.title()} is staying in Room {room}.")
            return

    print("Guest not found.")


def count_available_rooms():

    count = 0

    for guest in rooms.values():

        if guest is None:
            count += 1

    print("Available Rooms:", count)


def main():

    while True:

        print("\n================================")
        print("       HOTEL BOOKING SYSTEM")
        print("================================")
        print("1. Show Rooms")
        print("2. Book Room")
        print("3. Cancel Booking")
        print("4. Search Guest")
        print("5. Available Rooms")
        print("6. Exit")
        print("================================")

        choice = input("Enter choice: ")

        if choice == "1":
            show_rooms()

        elif choice == "2":
            book_room()

        elif choice == "3":
            cancel_booking()

        elif choice == "4":
            search_guest()

        elif choice == "5":
            count_available_rooms()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


main()