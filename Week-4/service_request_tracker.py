print("===== SERVICE REQUEST TRACKER =====")

requests = []
request_id = 1001

while True:
    print("\n1. Create request")
    print("2. Update request")
    print("3. View all requests")
    print("4. Search request")
    print("5. Delete request")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        customer = input("Customer name: ")
        issue = input("Describe the issue: ")

        if not customer.strip() or not issue.strip():
            print("Details cannot be empty ❌")
        else:
            requests.append({
                "id": request_id,
                "customer": customer,
                "issue": issue,
                "status": "Pending"
            })

            print(f"Request created successfully! ID: {request_id} ✅")
            request_id += 1

    elif choice == "2":
        try:
            search_id = int(input("Enter request ID: "))

            for request in requests:
                if request["id"] == search_id:
                    print("\n1. Pending")
                    print("2. In Progress")
                    print("3. Completed")

                    status_choice = input("Choose status: ")

                    statuses = {
                        "1": "Pending",
                        "2": "In Progress",
                        "3": "Completed"
                    }

                    if status_choice in statuses:
                        request["status"] = statuses[status_choice]
                        print("Request updated! ✅")
                    else:
                        print("Invalid status ❌")

                    break
            else:
                print("Request not found ❌")

        except ValueError:
            print("Enter a valid request ID.")

    elif choice == "3":
        if not requests:
            print("No service requests available.")

        else:
            print("\n===== ALL REQUESTS =====")

            for request in requests:
                print(
                    f"ID: {request['id']} | "
                    f"{request['customer']} | "
                    f"{request['status']}"
                )

    elif choice == "4":
        try:
            search_id = int(input("Enter request ID: "))

            for request in requests:
                if request["id"] == search_id:
                    print("\n===== REQUEST DETAILS =====")
                    print("ID:", request["id"])
                    print("Customer:", request["customer"])
                    print("Issue:", request["issue"])
                    print("Status:", request["status"])
                    break
            else:
                print("Request not found ❌")

        except ValueError:
            print("Invalid request ID.")

    elif choice == "5":
        try:
            search_id = int(input("Enter request ID: "))

            for request in requests:
                if request["id"] == search_id:
                    requests.remove(request)
                    print("Request deleted! 🗑️")
                    break
            else:
                print("Request not found ❌")

        except ValueError:
            print("Invalid request ID.")

    elif choice == "6":
        print("Service tracker closed! 👋")
        break

    else:
        print("Invalid choice ❌")