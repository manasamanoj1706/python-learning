# Random Color Generator

import random


def generate_color():
    try:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        hex_color = "#{:02X}{:02X}{:02X}".format(
            red, green, blue
        )

        print("\n========== RANDOM COLOR ==========")
        print("Red   :", red)
        print("Green :", green)
        print("Blue  :", blue)
        print("HEX   :", hex_color)

    except ValueError as error:
        print("Error:", error)

    finally:
        print("Color generation completed.")


def main():

    while True:

        print("\n==============================")
        print("     RANDOM COLOR GENERATOR")
        print("==============================")
        print("1. Generate Color")
        print("2. Exit")
        print("==============================")

        choice = input("Enter choice: ")

        if choice == "1":
            generate_color()

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()