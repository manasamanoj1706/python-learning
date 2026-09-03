print("===== SHOPPING CART =====")

cart = []

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Calculate total")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))

        cart.append({"name": item, "price": price})
        print(f"{item} added to cart! 🛒")

    elif choice == "2":
        item = input("Enter item name to remove: ")

        found = False

        for product in cart:
            if product["name"].lower() == item.lower():
                cart.remove(product)
                print(f"{item} removed!")
                found = True
                break

        if not found:
            print("Item not found ❌")

    elif choice == "3":
        if not cart:
            print("Your cart is empty.")

        else:
            print("\n===== YOUR CART =====")

            for product in cart:
                print(f"{product['name']} - ₹{product['price']:.2f}")

    elif choice == "4":
        total = 0

        for product in cart:
            total += product["price"]

        print(f"Total amount: ₹{total:.2f}")

    elif choice == "5":
        print("Thank you for shopping! 🛍️")
        break

    else:
        print("Invalid choice ❌")