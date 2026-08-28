# Expense Splitter

def calculate_split(total, people):
    return total / people


def main():
    try:
        print("\n==============================")
        print("       EXPENSE SPLITTER")
        print("==============================")

        total = float(input("Enter total bill amount: ₹"))
        people = int(input("Enter number of people: "))

        if total <= 0:
            raise ValueError("Bill amount must be greater than zero.")

        if people <= 0:
            raise ValueError("Number of people must be greater than zero.")

        share = calculate_split(total, people)

        print("\n========== BILL SUMMARY ==========")
        print("Total Bill       : ₹", round(total, 2))
        print("Number of People :", people)
        print("Each Person Pays : ₹", round(share, 2))

    except ValueError as error:
        print("Error:", error)

    finally:
        print("\nExpense splitter completed.")


main()