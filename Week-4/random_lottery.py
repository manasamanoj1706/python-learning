# Random Lottery Number Generator

import random


def generate_numbers():

    try:
        count = int(input("How many numbers do you want? "))

        if count <= 0:
            raise ValueError("Count must be greater than zero.")

        if count > 50:
            raise ValueError("You can generate a maximum of 50 numbers.")

        numbers = random.sample(range(1, 101), count)

        numbers.sort()

        print("\n========== LOTTERY NUMBERS ==========")

        for number in numbers:
            print(number, end=" ")

        print("\n\nNumbers generated successfully!")

    except ValueError as error:
        print("Error:", error)

    finally:
        print("\nLottery generator completed.")


generate_numbers()