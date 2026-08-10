# Student Marks Calculator

def calculate_result():

    try:
        name = input("Enter Student Name: ")

        mark1 = float(input("Enter Python Mark: "))
        mark2 = float(input("Enter Java Mark: "))
        mark3 = float(input("Enter DBMS Mark: "))

        if mark1 < 0 or mark1 > 100:
            raise ValueError("Python mark must be between 0 and 100.")

        if mark2 < 0 or mark2 > 100:
            raise ValueError("Java mark must be between 0 and 100.")

        if mark3 < 0 or mark3 > 100:
            raise ValueError("DBMS mark must be between 0 and 100.")

        total = mark1 + mark2 + mark3
        average = total / 3

        print("\n========== RESULT ==========")
        print("Student:", name)
        print("Total:", total)
        print("Average:", round(average, 2))

        if average >= 90:
            print("Grade: A+")
        elif average >= 80:
            print("Grade: A")
        elif average >= 70:
            print("Grade: B")
        elif average >= 60:
            print("Grade: C")
        elif average >= 50:
            print("Grade: D")
        else:
            print("Grade: F")

    except ValueError as error:
        print("Error:", error)

    finally:
        print("\nResult processing completed.")


calculate_result()