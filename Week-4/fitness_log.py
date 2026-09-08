print("===== FITNESS LOG =====")

workouts = []

while True:
    print("\n1. Add workout")
    print("2. View workouts")
    print("3. Total calories burned")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        exercise = input("Exercise name: ")

        try:
            minutes = int(input("Duration (minutes): "))
            calories = int(input("Calories burned: "))

            if minutes <= 0 or calories <= 0:
                raise ValueError("Values must be greater than 0")

            workouts.append({
                "exercise": exercise,
                "minutes": minutes,
                "calories": calories
            })

            print("Workout added! 💪")

        except ValueError as error:
            print("Error:", error)

    elif choice == "2":
        if not workouts:
            print("No workouts recorded.")

        else:
            for workout in workouts:
                print(
                    f"{workout['exercise']} - "
                    f"{workout['minutes']} min - "
                    f"{workout['calories']} kcal"
                )

    elif choice == "3":
        total = sum(w["calories"] for w in workouts)
        print(f"Total calories burned: {total} kcal 🔥")

    elif choice == "4":
        print("Keep going! 🚀")
        break

    else:
        print("Invalid choice ❌")