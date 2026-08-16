# Student Management System

students = []


def add_student():
    try:
        name = input("Enter student name: ")
        department = input("Enter department: ")
        year = input("Enter year: ")
        cgpa = float(input("Enter CGPA: "))

        if name == "" or department == "":
            raise ValueError("Name and department cannot be empty.")

        if cgpa < 0 or cgpa > 10:
            raise ValueError("CGPA must be between 0 and 10.")

        student = {
            "name": name,
            "department": department,
            "year": year,
            "cgpa": cgpa
        }

        students.append(student)

        print("\nStudent added successfully!")

    except ValueError as error:
        print("Error:", error)


def view_students():

    if len(students) == 0:
        print("\nNo students available.")
        return

    print("\n========== STUDENT LIST ==========")

    for index, student in enumerate(students, start=1):

        print("\nStudent", index)
        print("Name       :", student["name"])
        print("Department :", student["department"])
        print("Year       :", student["year"])
        print("CGPA       :", student["cgpa"])


def search_student():

    name = input("Enter student name to search: ").lower()

    found = False

    for student in students:

        if student["name"].lower() == name:

            print("\n========== STUDENT FOUND ==========")
            print("Name       :", student["name"])
            print("Department :", student["department"])
            print("Year       :", student["year"])
            print("CGPA       :", student["cgpa"])

            found = True
            break

    if not found:
        print("Student not found.")


def update_cgpa():

    try:

        name = input("Enter student name: ").lower()

        for student in students:

            if student["name"].lower() == name:

                new_cgpa = float(input("Enter new CGPA: "))

                if new_cgpa < 0 or new_cgpa > 10:
                    raise ValueError("CGPA must be between 0 and 10.")

                student["cgpa"] = new_cgpa

                print("CGPA updated successfully!")
                return

        print("Student not found.")

    except ValueError as error:
        print("Error:", error)


def delete_student():

    name = input("Enter student name to delete: ").lower()

    for student in students:

        if student["name"].lower() == name:

            students.remove(student)

            print("Student deleted successfully!")
            return

    print("Student not found.")


def show_topper():

    if len(students) == 0:
        print("No students available.")
        return

    topper = students[0]

    for student in students:

        if student["cgpa"] > topper["cgpa"]:
            topper = student

    print("\n========== TOPPER ==========")
    print("Name       :", topper["name"])
    print("Department :", topper["department"])
    print("CGPA       :", topper["cgpa"])


def main():

    try:

        while True:

            print("\n====================================")
            print("       STUDENT MANAGEMENT SYSTEM")
            print("====================================")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update CGPA")
            print("5. Delete Student")
            print("6. Show Topper")
            print("7. Exit")
            print("====================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                add_student()

            elif choice == "2":
                view_students()

            elif choice == "3":
                search_student()

            elif choice == "4":
                update_cgpa()

            elif choice == "5":
                delete_student()

            elif choice == "6":
                show_topper()

            elif choice == "7":
                print("Thank you!")
                break

            else:
                raise ValueError("Invalid menu choice.")

    except ValueError as error:
        print("Error:", error)

    finally:
        print("\nStudent Management System closed.")


main()