# Currency Converter

rates = {
    "USD": 0.012,
    "EUR": 0.011,
    "GBP": 0.0095
}


def convert_currency():

    try:
        amount = float(input("Enter amount in INR: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        print("\n1. USD")
        print("2. EUR")
        print("3. GBP")

        choice = input("Choose currency: ")

        currencies = {
            "1": "USD",
            "2": "EUR",
            "3": "GBP"
        }

        if choice not in currencies:
            raise ValueError("Invalid currency choice.")

        currency = currencies[choice]
        converted = amount * rates[currency]

        print("\n========== RESULT ==========")
        print("INR Amount :", amount)
        print("Currency   :", currency)
        print("Converted  :", round(converted, 2))

    except ValueError as error:
        print("Error:", error)


def main():

    while True:

        print("\n==============================")
        print("      CURRENCY CONVERTER")
        print("==============================")
        print("1. Convert Currency")
        print("2. Exit")
        print("==============================")

        choice = input("Enter choice: ")

        if choice == "1":
            convert_currency()

        elif choice == "2":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


main()