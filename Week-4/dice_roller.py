# Dice Roller

import random


def roll_dice():

    try:
        choice = input("Roll the dice? (yes/no): ").lower()

        if choice == "yes":

            number = random.randint(1, 6)

            print("\nYou rolled:", number)

            if number == 6:
                print("🎉 You got 6!")

        elif choice == "no":
            print("Game ended.")

        else:
            raise ValueError("Please enter yes or no.")

    except ValueError as error:
        print("Error:", error)


roll_dice()