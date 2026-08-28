# Parking Fee Calculator

def calculate_fee(hours):
    if hours <= 1:
        return 20
    elif hours <= 3:
        return 40
    elif hours <= 5:
        return 70
    else:
        return 100


def main():
    records = []

    while True:
        print("\n==============================")
        print("      PARKING FEE SYSTEM")
        print("==============================")
        print("1. Add Vehicle")
        print("2. View Records")
        print("3. Exit")
        print("==============================")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                vehicle = input("Enter vehicle number: ").strip()
                hours = float(input("Enter parking hours: "))

                if not vehicle:
                    raise ValueError("Vehicle number cannot be empty.")

                if hours <= 0:
                    raise ValueError("Hours must be greater than zero.")

                fee = calculate_fee(hours)

                record = {
                    "vehicle": vehicle,
                    "hours": hours,
                    "fee": fee
                }

                records.append(record)

                print("\nVehicle:", vehicle)
                print("Parking Hours:", hours)
                print("Parking Fee: ₹", fee)
                print("Record added successfully!")

            except ValueError as error:
                print("Error:", error)

        elif choice == "2":

            if not records:
                print("No parking records available.")
                continue

            print("\n========== PARKING RECORDS ==========")

            total = 0

            for number, record in enumerate(records, start=1):
                print(
                    number,
                    record["vehicle"],
                    "-",
                    record["hours"],
                    "hours - ₹",
                    record["fee"]
                )
                total += record["fee"]

            print("-------------------------------------")
            print("Total Collection: ₹", total)

        elif choice == "3":
            print("Parking system closed.")
            break

        else:
            print("Invalid choice.")


main()