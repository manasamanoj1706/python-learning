print("===== STUDENT GRADE CALCULATOR =====")

students = []

while True:
    print("\n1. Add student")
    print("2. View results")
    print("3. Find topper")
    print("4. Search student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Student name: ")

        try:
            mark = float(input("Enter mark (0-100): "))

            if mark < 0 or mark > 100:
                raise ValueError("Mark must be between 0 and 100.")

            if mark >= 90:
                grade = "A+"
            elif mark >= 80:
                grade = "A"
            elif mark >= 70:
                grade = "B"
            elif mark >= 60:
                grade = "C"
            elif mark >= 50:
                grade = "D"
            else:
                grade = "F"

            students.append({
                "name": name,
                "mark": mark,
                "grade": grade
            })

            print("Student added successfully! ✅")

        except ValueError as error:
            print("Error:", error)

    elif choice == "2":
        if not students:
            print("No student records.")

        else:
            print("\n===== RESULTS =====")

            for student in students:
                print(
                    f"{student['name']} | "
                    f"Mark: {student['mark']} | "
                    f"Grade: {student['grade']}"
                )

    elif choice == "3":
        if not students:
            print("No students available.")

        else:
            topper = max(students, key=lambda student: student["mark"])

            print(
                f"🏆 Topper: {topper['name']} "
                f"({topper['mark']} marks)"
            )

    elif choice == "4":
        name = input("Enter student name: ")
        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                print("\nStudent found 🔎")
                print("Name:", student["name"])
                print("Mark:", student["mark"])
                print("Grade:", student["grade"])
                found = True
                break

        if not found:
            print("Student not found ❌")

    elif choice == "5":
        print("Program closed. 👋")
        break

    else:
        print("Invalid choice ❌")