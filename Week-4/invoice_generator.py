print("===== INVOICE GENERATOR =====")

items = []

while True:
    print("\n1. Add item")
    print("2. Generate invoice")
    print("3. Clear invoice")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Item name: ")

        try:
            price = float(input("Price: ₹"))
            quantity = int(input("Quantity: "))

            if price <= 0 or quantity <= 0:
                raise ValueError("Price and quantity must be greater than 0.")

            items.append({
                "name": name,
                "price": price,
                "quantity": quantity
            })

            print("Item added! ✅")

        except ValueError as error:
            print("Error:", error)

    elif choice == "2":
        if not items:
            print("No items in invoice.")

        else:
            print("\n========== INVOICE ==========")

            total = 0

            for item in items:
                amount = item["price"] * item["quantity"]
                total += amount

                print(
                    f"{item['name']} | "
                    f"₹{item['price']:.2f} x {item['quantity']} "
                    f"= ₹{amount:.2f}"
                )

            tax = total * 0.05
            final_amount = total + tax

            print("-----------------------------")
            print(f"Subtotal : ₹{total:.2f}")
            print(f"Tax (5%) : ₹{tax:.2f}")
            print(f"Total    : ₹{final_amount:.2f}")
            print("=============================")

    elif choice == "3":
        items.clear()
        print("Invoice cleared! 🗑️")

    elif choice == "4":
        print("Invoice generator closed! 👋")
        break

    else:
        print("Invalid choice ❌")