print("===== LOAN EMI CALCULATOR =====")

while True:
    print("\n1. Calculate EMI")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            principal = float(input("Enter loan amount: ₹"))
            annual_rate = float(input("Enter annual interest rate (%): "))
            years = int(input("Enter loan period (years): "))

            if principal <= 0 or annual_rate < 0 or years <= 0:
                raise ValueError("Enter valid positive values.")

            monthly_rate = annual_rate / (12 * 100)
            months = years * 12

            if monthly_rate == 0:
                emi = principal / months
            else:
                emi = (
                    principal
                    * monthly_rate
                    * (1 + monthly_rate) ** months
                    / ((1 + monthly_rate) ** months - 1)
                )

            total_payment = emi * months
            total_interest = total_payment - principal

            print("\n===== LOAN DETAILS =====")
            print(f"Monthly EMI    : ₹{emi:.2f}")
            print(f"Total Payment  : ₹{total_payment:.2f}")
            print(f"Total Interest : ₹{total_interest:.2f}")

        except ValueError as error:
            print("Error:", error)

    elif choice == "2":
        print("Calculator closed! 👋")
        break

    else:
        print("Invalid choice ❌")