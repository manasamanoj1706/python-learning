# Shopping Billing System

cart = []


def add_item():
    try:
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))

        if price <= 0 or quantity <= 0:
            raise ValueError("Price and quantity must be greater than zero.")

        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        cart.append(item)

        print("Product added to cart!")

    except ValueError as error:
        print("Error:", error)


def view_cart():

    if len(cart) == 0:
        print("\nCart is empty.")
        return

    print("\n========== YOUR CART ==========")

    total = 0

    for item in cart:

        item_total = item["price"] * item["quantity"]
        total += item_total

        print(
            item["name"],
            "- ₹", item["price"],
            "x", item["quantity"],
            "= ₹", item_total
        )

    print("-------------------------------")
    print("Total: ₹", total)


def generate_bill():

    if len(cart) == 0:
        print("Cart is empty.")
        return

    total = 0

    print("\n========== FINAL BILL ==========")

    for item in cart:

        item_total = item["price"] * item["quantity"]
        total += item_total

        print(item["name"], "₹", item_total)

    try:

        discount = float(input("\nEnter discount percentage: "))

        if discount < 0 or discount > 100:
            raise ValueError("Discount must be between 0 and 100.")

        discount_amount = total * discount / 100
        final_amount = total - discount_amount

        print("-------------------------------")
        print("Subtotal       : ₹", total)
        print("Discount       : ₹", discount_amount)
        print("Final Amount   : ₹", final_amount)
        print("-------------------------------")

    except ValueError as error:
        print("Error:", error)


def remove_item():

    if len(cart) == 0:
        print("Cart is empty.")
        return

    name = input("Enter product name to remove: ")

    found = False

    for item in cart:

        if item["name"].lower() == name.lower():

            cart.remove(item)
            found = True

            print("Product removed successfully!")
            break

    if not found:
        print("Product not found.")


while True:

    print("\n================================")
    print("       SHOPPING BILLING SYSTEM")
    print("================================")
    print("1. Add Product")
    print("2. View Cart")
    print("3. Remove Product")
    print("4. Generate Bill")
    print("5. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":
            add_item()

        elif choice == "2":
            view_cart()

        elif choice == "3":
            remove_item()

        elif choice == "4":
            generate_bill()

        elif choice == "5":
            print("Thank you for shopping!")
            break

        else:
            raise ValueError("Invalid menu choice.")

    except ValueError as error:
        print("Error:", error)