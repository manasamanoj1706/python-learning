# Employee Record Management System

def add_employee():
    with open("employees.txt", "a") as file:

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        designation = input("Enter Designation: ")
        salary = input("Enter Salary: ")

        file.write(f"Employee ID : {emp_id}\n")
        file.write(f"Name        : {name}\n")
        file.write(f"Department  : {department}\n")
        file.write(f"Designation : {designation}\n")
        file.write(f"Salary      : {salary}\n")
        file.write("=" * 40 + "\n")

        print("Employee added successfully!")


def view_employees():

    try:

        with open("employees.txt", "r") as file:

            data = file.read()

            if data:
                print("\n========== EMPLOYEE RECORDS ==========\n")
                print(data)
            else:
                print("No employee records found.")

    except FileNotFoundError:
        print("Employee file does not exist.")


def search_employee():

    try:

        emp_id = input("Enter Employee ID to Search: ")

        with open("employees.txt", "r") as file:

            lines = file.readlines()

            found = False

            for line in lines:

                if emp_id in line:
                    found = True

                if found:
                    print(line, end="")

                    if "========================================" in line:
                        break

            if not found:
                print("Employee Not Found.")

    except FileNotFoundError:
        print("Employee file not found.")


while True:

    print("\n===================================")
    print(" EMPLOYEE RECORD MANAGEMENT SYSTEM ")
    print("===================================")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Exit")
    print("===================================")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
