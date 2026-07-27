# ===========================================
# Project : Student Information System
# Author  : Manasa Manoj
# Day     : 20
# ===========================================

student = (
    "Manasa Manoj",
    21,
    "Artificial Intelligence & Data Science",
    8.2
)

while True:
    print("\n===== Student Information System =====")
    print("1. View Student Details")
    print("2. Student Name")
    print("3. Student Age")
    print("4. Department")
    print("5. CGPA")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nStudent Details")
        print("Name       :", student[0])
        print("Age        :", student[1])
        print("Department :", student[2])
        print("CGPA       :", student[3])

    elif choice == "2":
        print("Student Name:", student[0])

    elif choice == "3":
        print("Student Age:", student[1])

    elif choice == "4":
        print("Department:", student[2])

    elif choice == "5":
        print("CGPA:", student[3])

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
