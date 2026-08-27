# Cinema Seat Booking System

seats = {}

for number in range(1, 21):
    seats[number] = None


def show_seats():
    print("\n========== SEATS ==========")

    for number, customer in seats.items():
        if customer is None:
            print(f"Seat {number}: Available")
        else:
            print(f"Seat {number}: Booked")


def book_seat():
    try:
        seat_number = int(input("Enter seat number (1-20): "))

        if seat_number not in seats:
            raise ValueError("Invalid seat number.")

        if seats[seat_number] is not None:
            print("Seat is already booked.")
            return

        name = input("Enter customer name: ").strip()

        if not name:
            raise ValueError("Customer name cannot be empty.")

        seats[seat_number] = name

        print("Seat booked successfully!")

    except ValueError as error:
        print("Error:", error)


def cancel_seat():
    try:
        seat_number = int(input("Enter seat number: "))

        if seat_number not in seats:
            raise ValueError("Invalid seat number.")

        if seats[seat_number] is None:
            print("Seat is already available.")
            return

        seats[seat_number] = None

        print("Booking cancelled successfully.")

    except ValueError as error:
        print("Error:", error)


def search_customer():
    name = input("Enter customer name: ").strip().lower()

    for seat, customer in seats.items():
        if customer is not None and customer.lower() == name:
            print(f"{name.title()} booked Seat {seat}.")
            return

    print("Customer not found.")


def available_seats():
    count = sum(
        1 for customer in seats.values()
        if customer is None
    )

    print("Available seats:", count)


def main():

    while True:

        print("\n==============================")
        print("      CINEMA BOOKING")
        print("==============================")
        print("1. Show Seats")
        print("2. Book Seat")
        print("3. Cancel Booking")
        print("4. Search Customer")
        print("5. Available Seats")
        print("6. Exit")
        print("==============================")

        choice = input("Enter choice: ")

        if choice == "1":
            show_seats()

        elif choice == "2":
            book_seat()

        elif choice == "3":
            cancel_seat()

        elif choice == "4":
            search_customer()

        elif choice == "5":
            available_seats()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


main()