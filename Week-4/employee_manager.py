print("===== EMPLOYEE MANAGER =====")

employees = []

while True:
    print("\n1. Add employee")
    print("2. View employees")
    print("3. Search employee")
    print("4. Update salary")
    print("5. Remove employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Employee name: ")
        department = input("Department: ")

        try:
            salary = float(input("Monthly salary: ₹"))

            if salary <= 0:
                raise ValueError("Salary must be greater than 0.")

            employees.append({
                "name": name,
                "department": department,
                "salary": salary
            })

            print("Employee added successfully! ✅")

        except ValueError as error:
            print("Error:", error)

    elif choice == "2":
        if not employees:
            print("No employees found.")

        else:
            print("\n===== EMPLOYEE LIST =====")

            for number, employee in enumerate(employees, start=1):
                print(
                    f"{number}. {employee['name']} | "
                    f"{employee['department']} | "
                    f"₹{employee['salary']:.2f}"
                )

    elif choice == "3":
        search = input("Enter employee name: ")
        found = False

        for employee in employees:
            if employee["name"].lower() == search.lower():
                print("\n===== EMPLOYEE DETAILS =====")
                print("Name:", employee["name"])
                print("Department:", employee["department"])
                print(f"Salary: ₹{employee['salary']:.2f}")

                found = True
                break

        if not found:
            print("Employee not found ❌")

    elif choice == "4":
        search = input("Enter employee name: ")

        for employee in employees:
            if employee["name"].lower() == search.lower():

                try:
                    new_salary = float(input("Enter new salary: ₹"))

                    if new_salary <= 0:
                        raise ValueError("Salary must be greater than 0.")

                    employee["salary"] = new_salary
                    print("Salary updated successfully! ✅")

                except ValueError as error:
                    print("Error:", error)

                break

        else:
            print("Employee not found ❌")

    elif choice == "5":
        search = input("Enter employee name to remove: ")

        for employee in employees:
            if employee["name"].lower() == search.lower():
                employees.remove(employee)
                print("Employee removed successfully! 🗑️")
                break

        else:
            print("Employee not found ❌")

    elif choice == "6":
        print("Employee manager closed! 👋")
        break

    else:
        print("Invalid choice ❌")