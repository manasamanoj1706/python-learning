# Daily Habit Tracker

habits = {}


def add_habit():
    habit = input("Enter habit name: ").strip()

    if not habit:
        print("Habit name cannot be empty.")
        return

    if habit in habits:
        print("Habit already exists.")
        return

    habits[habit] = 0
    print("Habit added successfully!")


def mark_habit():
    if not habits:
        print("No habits available.")
        return

    show_habits()

    habit = input("Enter habit to mark as completed: ").strip()

    if habit in habits:
        habits[habit] += 1
        print("Habit marked as completed!")
    else:
        print("Habit not found.")


def show_habits():
    if not habits:
        print("No habits available.")
        return

    print("\n========== HABITS ==========")

    for number, (habit, days) in enumerate(habits.items(), start=1):
        print(f"{number}. {habit} - {days} day(s) completed")


def remove_habit():
    habit = input("Enter habit to remove: ").strip()

    if habit in habits:
        del habits[habit]
        print("Habit removed successfully!")
    else:
        print("Habit not found.")


def main():

    while True:

        print("\n==============================")
        print("       DAILY HABIT TRACKER")
        print("==============================")
        print("1. Add Habit")
        print("2. Mark Habit Completed")
        print("3. View Habits")
        print("4. Remove Habit")
        print("5. Exit")
        print("==============================")

        choice = input("Enter choice: ")

        if choice == "1":
            add_habit()

        elif choice == "2":
            mark_habit()

        elif choice == "3":
            show_habits()

        elif choice == "4":
            remove_habit()

        elif choice == "5":
            print("Tracker closed.")
            break

        else:
            print("Invalid choice.")


try:
    main()

except Exception as error:
    print("Unexpected error:", error)

finally:
    print("Thank you for using the habit tracker!")