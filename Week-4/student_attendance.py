# Student Attendance Management System

students = {}


def add_student():
    try:
        name = input("Enter student name: ").strip()

        if not name:
            raise ValueError("Name cannot be empty.")

        if name in students:
            print("Student already exists.")
            return

        students[name] = {
            "present": 0,
            "absent": 0
        }

        print("Student added successfully!")

    except ValueError as error:
        print("Error:", error)


def mark_attendance():

    try:
        name = input("Enter student name: ").strip()

        if name not in students:
            raise ValueError("Student not found.")

        status = input("Enter P for Present or A for Absent: ").upper()

        if status == "P":
            students[name]["present"] += 1
            print("Marked Present.")

        elif status == "A":
            students[name]["absent"] += 1
            print("Marked Absent.")

        else:
            raise ValueError("Enter only P or A.")

    except ValueError as error:
        print("Error:", error)


def view_attendance():

    if not students:
        print("No students available.")
        return

    print("\n========== ATTENDANCE ==========")

    for name, data in students.items():

        total = data["present"] + data["absent"]

        if total > 0:
            percentage = (data["present"] / total) * 100
        else:
            percentage = 0

        print("\nName:", name)
        print("Present:", data["present"])
        print("Absent:", data["absent"])
        print("Attendance:", round(percentage, 2), "%")


def search_student():

    name = input("Enter student name: ").strip()

    if name in students:
        print("\nStudent Found!")
        print("Name:", name)
        print("Present:", students[name]["present"])
        print("Absent:", students[name]["absent"])
    else:
        print("Student not found.")


def main():

    while True:

        print("\n================================")
        print("    STUDENT ATTENDANCE SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Search Student")
        print("5. Exit")
        print("================================")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            mark_attendance()

        elif choice == "3":
            view_attendance()

        elif choice == "4":
            search_student()

        elif choice == "5":
            print("Attendance system closed.")
            break

        else:
            print("Invalid choice.")


main()