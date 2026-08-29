# Weather Clothing Advisor


def get_advice(temperature, weather):

    if temperature < 15:
        advice = "Wear a jacket or sweater."
    elif temperature < 25:
        advice = "Wear comfortable warm clothes."
    elif temperature < 35:
        advice = "Wear light cotton clothes."
    else:
        advice = "Wear very light clothes and stay hydrated."

    if weather == "rainy":
        advice += " Carry an umbrella."
    elif weather == "sunny":
        advice += " Consider wearing sunglasses."
    elif weather == "windy":
        advice += " Carry a light jacket."

    return advice


def main():

    try:
        temperature = float(input("Enter temperature in °C: "))

        weather = input(
            "Enter weather (sunny/rainy/windy/cloudy): "
        ).lower().strip()

        valid_weather = ["sunny", "rainy", "windy", "cloudy"]

        if weather not in valid_weather:
            raise ValueError("Invalid weather condition.")

        print("\n========== WEATHER ADVISOR ==========")
        print("Temperature:", temperature, "°C")
        print("Weather:", weather)
        print("Advice:", get_advice(temperature, weather))

    except ValueError as error:
        print("Error:", error)

    finally:
        print("\nWeather advisor completed.")


main()