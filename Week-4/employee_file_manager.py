# Employee File Manager

def create_employee_file():
    with open("employees.txt", "w") as file:
        file.write("Employee ID : 101\n")
        file.write("Name : Rahul\n")
        file.write("Department : Development\n")
        file.write("Salary : 50000\n")
        file.write("--------------------\n")

    print("Employee file created!")


def read_first_employee_detail():

    with open("employees.txt", "r") as file:
        first_line = file.readline()

    print("\nFirst Employee Detail:")
    print(first_line.strip())


def read_all_details():

    with open("employees.txt", "r") as file:
        details = file.readlines()

    print("\nAll Employee Details:")

    for detail in details:
        print(detail.strip())


def count_details():

    with open("employees.txt", "r") as file:
        count = 0

        for line in file:
            count += 1

    print("\nTotal Lines:", count)


while True:

    print("\n==============================")
    print("    EMPLOYEE FILE MANAGER")
    print("==============================")
    print("1. Create Employee File")
    print("2. Read First Line")
    print("3. Read All Details")
    print("4. Count Lines")
    print("5. Exit")
    print("==============================")

    choice = input("Enter Choice: ")

    if choice == "1":
        create_employee_file()

    elif choice == "2":
        read_first_employee_detail()

    elif choice == "3":
        read_all_details()

    elif choice == "4":
        count_details()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")