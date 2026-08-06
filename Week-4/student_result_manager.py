# Student Result Manager

def add_result():

    try:
        with open("results.txt", "a") as file:

            roll = input("Enter Roll Number: ")
            name = input("Enter Student Name: ")

            python = int(input("Python Marks: "))
            java = int(input("Java Marks: "))
            dbms = int(input("DBMS Marks: "))

            total = python + java + dbms
            percentage = total / 3

            file.write(f"{roll},{name},{python},{java},{dbms},{total},{percentage:.2f}\n")

            print("Result Added Successfully!")

    except ValueError:
        print("Marks should be numbers only.")


def view_results():

    try:
        with open("results.txt", "r") as file:

            print("\n========== STUDENT RESULTS ==========")

            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("No result file found.")


def search_result():

    try:

        roll = input("Enter Roll Number: ")

        found = False

        with open("results.txt", "r") as file:

            for line in file:

                if line.startswith(roll + ","):
                    print("\nStudent Found")
                    print(line.strip())
                    found = True
                    break

        if not found:
            print("Student Not Found.")

    except FileNotFoundError:
        print("No result file found.")


while True:

    print("\n========== RESULT MANAGEMENT ==========")
    print("1. Add Result")
    print("2. View Results")
    print("3. Search Result")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_result()

    elif choice == "2":
        view_results()

    elif choice == "3":
        search_result()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")