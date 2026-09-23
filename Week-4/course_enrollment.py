print("===== COURSE ENROLLMENT SYSTEM =====")

courses = {
    "Python": [],
    "Java": [],
    "Data Science": [],
    "Web Development": []
}

while True:
    print("\n1. Enroll student")
    print("2. View courses")
    print("3. Search student")
    print("4. Drop course")
    print("5. Show course count")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student = input("Enter student name: ")
        course = input("Enter course name: ")

        if course not in courses:
            print("Course not available ❌")

        elif student in courses[course]:
            print("Student is already enrolled ❌")

        else:
            courses[course].append(student)
            print(f"{student} enrolled in {course}! ✅")

    elif choice == "2":
        print("\n===== AVAILABLE COURSES =====")

        for course, students in courses.items():
            print(f"\n{course}")

            if students:
                for student in students:
                    print(f"  - {student}")
            else:
                print("  No students enrolled.")

    elif choice == "3":
        name = input("Enter student name: ")
        found = False

        for course, students in courses.items():
            if name in students:
                print(f"{name} is enrolled in {course}.")
                found = True

        if not found:
            print("Student not found ❌")

    elif choice == "4":
        student = input("Enter student name: ")
        course = input("Enter course name: ")

        if course in courses and student in courses[course]:
            courses[course].remove(student)
            print("Student dropped from course! ✅")
        else:
            print("Enrollment not found ❌")

    elif choice == "5":
        print("\n===== COURSE COUNTS =====")

        for course, students in courses.items():
            print(f"{course}: {len(students)} student(s)")

    elif choice == "6":
        print("Course enrollment system closed! 👋")
        break

    else:
        print("Invalid choice ❌")