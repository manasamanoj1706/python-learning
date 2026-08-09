# Student File Reader

def create_file():
    with open("student.txt", "w") as file:
        file.write("Name : Manasa\n")
        file.write("Department : AI & DS\n")
        file.write("Year : Final Year\n")
        file.write("CGPA : 8.2\n")

    print("Student file created successfully!")


def read_first_line():

    with open("student.txt", "r") as file:
        line = file.readline()

    print("\nFirst Line:")
    print(line.strip())


def read_all_lines():

    with open("student.txt", "r") as file:
        lines = file.readlines()

    print("\nAll Student Details:")

    for line in lines:
        print(line.strip())


def count_lines():

    with open("student.txt", "r") as file:
        count = 0

        for line in file:
            count += 1

    print("\nTotal Lines:", count)


while True:

    print("\n==============================")
    print("     STUDENT FILE READER")
    print("==============================")
    print("1. Create Student File")
    print("2. Read First Line")
    print("3. Read All Lines")
    print("4. Count Lines")
    print("5. Exit")
    print("==============================")

    choice = input("Enter Choice: ")

    if choice == "1":
        create_file()

    elif choice == "2":
        read_first_line()

    elif choice == "3":
        read_all_lines()

    elif choice == "4":
        count_lines()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid Choice")