print("===== BUS TICKET BOOKING SYSTEM =====")

tickets = []
ticket_number = 1001

while True:
    print("\n1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. View Bookings")
    print("4. Search Ticket")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Passenger name: ")
        destination = input("Destination: ")

        try:
            age = int(input("Passenger age: "))
            seats = int(input("Number of seats: "))

            if age <= 0 or seats <= 0:
                raise ValueError("Age and seats must be greater than 0.")

            ticket = {
                "ticket_no": ticket_number,
                "name": name,
                "age": age,
                "destination": destination,
                "seats": seats
            }

            tickets.append(ticket)

            print("\n✅ Ticket booked successfully!")
            print("Ticket Number:", ticket_number)

            ticket_number += 1

        except ValueError as error:
            print("Error:", error)

    elif choice == "2":
        try:
            number = int(input("Enter ticket number: "))

            for ticket in tickets:
                if ticket["ticket_no"] == number:
                    tickets.remove(ticket)
                    print("Ticket cancelled successfully! ✅")
                    break
            else:
                print("Ticket not found ❌")

        except ValueError:
            print("Enter a valid ticket number.")

    elif choice == "3":
        if not tickets:
            print("No bookings available.")

        else:
            print("\n===== ALL BOOKINGS =====")

            for ticket in tickets:
                print(
                    f"Ticket: {ticket['ticket_no']} | "
                    f"Name: {ticket['name']} | "
                    f"Destination: {ticket['destination']} | "
                    f"Seats: {ticket['seats']}"
                )

    elif choice == "4":
        try:
            number = int(input("Enter ticket number: "))

            for ticket in tickets:
                if ticket["ticket_no"] == number:
                    print("\n===== TICKET DETAILS =====")
                    print("Ticket Number:", ticket["ticket_no"])
                    print("Passenger:", ticket["name"])
                    print("Age:", ticket["age"])
                    print("Destination:", ticket["destination"])
                    print("Seats:", ticket["seats"])
                    break
            else:
                print("Ticket not found ❌")

        except ValueError:
            print("Invalid ticket number.")

    elif choice == "5":
        print("Thank you for using Bus Ticket Booking! 🚌")
        break

    else:
        print("Invalid choice ❌")