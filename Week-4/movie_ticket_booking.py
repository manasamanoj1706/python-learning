# Movie Ticket Booking System

seats = 50
ticket_price = 150


def show_seats():
    print("\nAvailable Seats:", seats)


def book_ticket():
    global seats

    try:
        number = int(input("Enter number of tickets: "))

        if number <= 0:
            raise ValueError("Number of tickets must be greater than zero.")

        if number > seats:
            print("Not enough seats available.")
            return

        total = number * ticket_price
        seats -= number

        print("\n========== BOOKING ==========")
        print("Tickets Booked :", number)
        print("Ticket Price   : ₹", ticket_price)
        print("Total Amount   : ₹", total)
        print("Remaining Seats:", seats)

    except ValueError as error:
        print("Error:", error)


def cancel_ticket():
    global seats

    try:
        number = int(input("Enter number of tickets to cancel: "))

        if number <= 0:
            raise ValueError("Number must be greater than zero.")

        seats += number

        print("Tickets cancelled successfully!")
        print("Available Seats:", seats)

    except ValueError as error:
        print("Error:", error)


def main():

    try:
        while True:

            print("\n==============================")
            print("    MOVIE TICKET BOOKING")
            print("==============================")
            print("1. Show Available Seats")
            print("2. Book Tickets")
            print("3. Cancel Tickets")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                show_seats()

            elif choice == "2":
                book_ticket()

            elif choice == "3":
                cancel_ticket()

            elif choice == "4":
                print("Thank you!")
                break

            else:
                raise ValueError("Invalid menu choice.")

    except ValueError as error:
        print("Error:", error)

    finally:
        print("Booking system closed.")


main()