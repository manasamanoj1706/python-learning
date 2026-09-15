print("===== PACKAGE DELIVERY MANAGER =====")

packages = []

while True:
    print("\n1. Add package")
    print("2. Update delivery status")
    print("3. View packages")
    print("4. Search package")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        package_id = input("Enter package ID: ")
        receiver = input("Enter receiver name: ")
        address = input("Enter delivery address: ")

        if not package_id or not receiver or not address:
            print("All details are required ❌")
        else:
            packages.append({
                "id": package_id,
                "receiver": receiver,
                "address": address,
                "status": "Processing"
            })

            print("Package added successfully! 📦")

    elif choice == "2":
        package_id = input("Enter package ID: ")

        for package in packages:
            if package["id"] == package_id:
                print("\n1. Shipped")
                print("2. Out for Delivery")
                print("3. Delivered")

                status = input("Choose status: ")

                status_list = {
                    "1": "Shipped",
                    "2": "Out for Delivery",
                    "3": "Delivered"
                }

                if status in status_list:
                    package["status"] = status_list[status]
                    print("Status updated! ✅")
                else:
                    print("Invalid status ❌")

                break
        else:
            print("Package not found ❌")

    elif choice == "3":
        if not packages:
            print("No packages available.")

        else:
            print("\n===== PACKAGE LIST =====")

            for package in packages:
                print(
                    f"ID: {package['id']} | "
                    f"Receiver: {package['receiver']} | "
                    f"Status: {package['status']}"
                )

    elif choice == "4":
        package_id = input("Enter package ID: ")
        found = False

        for package in packages:
            if package["id"] == package_id:
                print("\n===== PACKAGE DETAILS =====")
                print("ID:", package["id"])
                print("Receiver:", package["receiver"])
                print("Address:", package["address"])
                print("Status:", package["status"])
                found = True
                break

        if not found:
            print("Package not found ❌")

    elif choice == "5":
        print("Delivery manager closed! 👋")
        break

    else:
        print("Invalid choice ❌")