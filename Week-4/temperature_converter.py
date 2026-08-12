# Temperature Converter

def convert_temperature():

    try:
        temperature = float(input("Enter temperature: "))

        print("\n1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")

        choice = input("Choose conversion: ")

        if choice == "1":
            result = (temperature * 9 / 5) + 32
            print("Fahrenheit:", round(result, 2))

        elif choice == "2":
            result = (temperature - 32) * 5 / 9
            print("Celsius:", round(result, 2))

        else:
            raise ValueError("Invalid conversion choice.")

    except ValueError as error:
        print("Error:", error)

    finally:
        print("Temperature conversion completed.")


convert_temperature()
