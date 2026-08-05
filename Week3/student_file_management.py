# Student File Management System

def add_student():
    with open("students.txt", "a") as file:
        name = input("Enter Student Name: ")
        department = input("Enter Department: ")
        cgpa = input("Enter CGPA: ")

        file.write(f"Name: {name}\n")
        file.write(f"Department: {department}\n")
        file.write(f"CGPA: {cgpa}\n")
        file.write("-" * 30 + "\n")

        print("Student record added successfully!")


def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.read()

            if data:
                print("\n===== STUDENT RECORDS =====")
                print(data)
            else:
                print("No records found.")

    except FileNotFoundError:
        print("No student file found.")


while True:

    print("\n========== STUDENT FILE MANAGEMENT ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
