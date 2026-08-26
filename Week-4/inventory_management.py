# Inventory Management System

inventory = {}


def add_product():
    try:
        name = input("Enter product name: ").strip()
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        if not name:
            raise ValueError("Product name cannot be empty.")

        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price cannot be negative.")

        inventory[name] = {
            "quantity": quantity,
            "price": price
        }

        print("Product added successfully!")

    except ValueError as error:
        print("Error:", error)


def view_inventory():

    if not inventory:
        print("\nInventory is empty.")
        return

    print("\n========== INVENTORY ==========")

    for name, details in inventory.items():
        print("\nProduct:", name)
        print("Quantity:", details["quantity"])
        print("Price: ₹", details["price"])


def sell_product():
    try:
        name = input("Enter product name: ").strip()

        if name not in inventory:
            raise ValueError("Product not found.")

        quantity = int(input("Enter quantity to sell: "))

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if quantity > inventory[name]["quantity"]:
            print("Not enough stock.")
            return

        inventory[name]["quantity"] -= quantity

        total = quantity * inventory[name]["price"]

        print("Sale successful!")
        print("Total amount: ₹", total)

    except ValueError as error:
        print("Error:", error)


def restock_product():
    try:
        name = input("Enter product name: ").strip()

        if name not in inventory:
            raise ValueError("Product not found.")

        quantity = int(input("Enter quantity to add: "))

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        inventory[name]["quantity"] += quantity

        print("Stock updated successfully!")

    except ValueError as error:
        print("Error:", error)


def main():

    while True:

        print("\n================================")
        print("      INVENTORY MANAGEMENT")
        print("================================")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Sell Product")
        print("4. Restock Product")
        print("5. Exit")
        print("================================")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_inventory()

        elif choice == "3":
            sell_product()

        elif choice == "4":
            restock_product()

        elif choice == "5":
            print("Inventory system closed.")
            break

        else:
            print("Invalid choice.")


main()