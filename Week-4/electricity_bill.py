# Electricity Bill Calculator

def calculate_bill():

    try:
        units = float(input("Enter electricity units: "))

        if units < 0:
            raise ValueError("Units cannot be negative.")

        if units <= 100:
            bill = units * 2

        elif units <= 200:
            bill = (100 * 2) + ((units - 100) * 3)

        elif units <= 300:
            bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

        else:
            bill = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 7)

        print("\n========== ELECTRICITY BILL ==========")
        print("Units Used :", units)
        print("Total Bill : ₹", round(bill, 2))

    except ValueError as error:
        print("Error:", error)

    finally:
        print("Bill calculation completed.")


calculate_bill()
