print("===== PARCEL TRACKER =====")

parcels = []

while True:
    print("\n1. Add parcel")
    print("2. Update parcel status")
    print("3. Track parcel")
    print("4. View all parcels")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        tracking_id = input("Enter tracking ID: ")
        receiver = input("Enter receiver name: ")

        parcel = {
            "id": tracking_id,
            "receiver": receiver,
            "status": "Order Placed"
        }

        parcels.append(parcel)
        print("Parcel added successfully! 📦")

    elif choice == "2":
        tracking_id = input("Enter tracking ID: ")

        found = False

        for parcel in parcels:
            if parcel["id"] == tracking_id:
                print("\n1. Shipped")
                print("2. Out for Delivery")
                print("3. Delivered")

                status_choice = input("Choose status: ")

                statuses = {
                    "1": "Shipped",
                    "2": "Out for Delivery",
                    "3": "Delivered"
                }

                if status_choice in statuses:
                    parcel["status"] = statuses[status_choice]
                    print("Status updated! ✅")
                else:
                    print("Invalid status ❌")

                found = True
                break

        if not found:
            print("Tracking ID not found ❌")

    elif choice == "3":
        tracking_id = input("Enter tracking ID: ")

        for parcel in parcels:
            if parcel["id"] == tracking_id:
                print("\n===== PARCEL DETAILS =====")
                print("Tracking ID:", parcel["id"])
                print("Receiver:", parcel["receiver"])
                print("Status:", parcel["status"])
                break
        else:
            print("Parcel not found ❌")

    elif choice == "4":
        if not parcels:
            print("No parcels available.")

        else:
            print("\n===== ALL PARCELS =====")

            for parcel in parcels:
                print(
                    f"{parcel['id']} | "
                    f"{parcel['receiver']} | "
                    f"{parcel['status']}"
                )

    elif choice == "5":
        print("Thank you! 👋")
        break

    else:
        print("Invalid choice ❌")