# Attendance Management System

def mark_attendance():

    try:

        with open("attendance.txt", "a") as file:

            roll = input("Enter Roll Number: ")
            name = input("Enter Student Name: ")
            status = input("Attendance (Present/Absent): ")

            file.write(f"{roll},{name},{status}\n")

            print("Attendance Marked Successfully!")

    except Exception as e:
        print("Error:", e)


def view_attendance():

    try:

        with open("attendance.txt", "r") as file:

            print("\n====== ATTENDANCE RECORD ======")

            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("Attendance file not found.")


def search_student():

    try:

        roll = input("Enter Roll Number: ")

        found = False

        with open("attendance.txt", "r") as file:

            for line in file:

                if line.startswith(roll + ","):
                    print("\nStudent Record")
                    print(line.strip())
                    found = True
                    break

        if not found:
            print("Student Not Found")

    except FileNotFoundError:
        print("Attendance file not found.")


def count_attendance():

    try:

        present = 0
        absent = 0

        with open("attendance.txt", "r") as file:

            for line in file:

                if "Present" in line:
                    present += 1

                elif "Absent" in line:
                    absent += 1

        print("\nAttendance Summary")
        print("Present :", present)
        print("Absent :", absent)

    except FileNotFoundError:
        print("Attendance file not found.")


while True:

    print("\n==============================")
    print(" ATTENDANCE MANAGEMENT SYSTEM ")
    print("==============================")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Search Student")
    print("4. Attendance Summary")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        mark_attendance()

    elif choice == "2":
        view_attendance()

    elif choice == "3":
        search_student()

    elif choice == "4":
        count_attendance()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")