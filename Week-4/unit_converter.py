# Unit Converter


def km_to_miles(km):
    return km * 0.621371


def miles_to_km(miles):
    return miles * 1.60934


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():

    while True:

        print("\n==============================")
        print("        UNIT CONVERTER")
        print("==============================")
        print("1. Kilometers → Miles")
        print("2. Miles → Kilometers")
        print("3. Celsius → Fahrenheit")
        print("4. Fahrenheit → Celsius")
        print("5. Exit")
        print("==============================")

        choice = input("Enter choice: ")

        try:

            if choice == "1":
                value = float(input("Enter kilometers: "))
                print("Miles:", round(km_to_miles(value), 2))

            elif choice == "2":
                value = float(input("Enter miles: "))
                print("Kilometers:", round(miles_to_km(value), 2))

            elif choice == "3":
                value = float(input("Enter Celsius: "))
                print("Fahrenheit:", round(celsius_to_fahrenheit(value), 2))

            elif choice == "4":
                value = float(input("Enter Fahrenheit: "))
                print("Celsius:", round(fahrenheit_to_celsius(value), 2))

            elif choice == "5":
                print("Converter closed.")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")


main()