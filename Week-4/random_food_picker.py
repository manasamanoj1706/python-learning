# Random Food Picker

import random


def add_food(food_list):
    try:
        food = input("Enter a food name: ").strip()

        if not food:
            raise ValueError("Food name cannot be empty.")

        food_list.append(food)

        print("Food added successfully!")

    except ValueError as error:
        print("Error:", error)


def show_foods(food_list):

    if not food_list:
        print("No food items available.")
        return

    print("\n========== FOOD LIST ==========")

    for number, food in enumerate(food_list, start=1):
        print(number, ".", food)


def pick_food(food_list):

    if not food_list:
        print("Add some food items first.")
        return

    selected = random.choice(food_list)

    print("\n🍽️ Today's Random Food:")
    print(selected)


def main():

    food_list = [
        "Biryani",
        "Fried Rice",
        "Dosa",
        "Pizza",
        "Burger"
    ]

    while True:

        print("\n==============================")
        print("      RANDOM FOOD PICKER")
        print("==============================")
        print("1. Add Food")
        print("2. Show Food List")
        print("3. Pick Random Food")
        print("4. Exit")
        print("==============================")

        choice = input("Enter choice: ")

        if choice == "1":
            add_food(food_list)

        elif choice == "2":
            show_foods(food_list)

        elif choice == "3":
            pick_food(food_list)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


try:
    main()

except Exception as error:
    print("Unexpected error:", error)

finally:
    print("Program closed.")