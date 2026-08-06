# Inventory Management System

def add_product():

    try:

        with open("inventory.txt", "a") as file:

            product_id = input("Enter Product ID: ")
            product_name = input("Enter Product Name: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))

            file.write(f"{product_id},{product_name},{quantity},{price}\n")

            print("Product Added Successfully!")

    except ValueError:
        print("Invalid Quantity or Price!")


def view_products():

    try:

        with open("inventory.txt", "r") as file:

            print("\n========== INVENTORY ==========")

            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("Inventory file not found.")


def search_product():

    try:

        product_id = input("Enter Product ID: ")

        found = False

        with open("inventory.txt", "r") as file:

            for line in file:

                if line.startswith(product_id + ","):
                    print("\nProduct Found")
                    print(line.strip())
                    found = True
                    break

        if not found:
            print("Product Not Found")

    except FileNotFoundError:
        print("Inventory file not found.")


def total_products():

    try:

        count = 0

        with open("inventory.txt", "r") as file:

            for line in file:
                count += 1

        print("Total Products :", count)

    except FileNotFoundError:
        print("Inventory file not found.")


while True:

    print("\n===================================")
    print(" INVENTORY MANAGEMENT SYSTEM ")
    print("===================================")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Total Products")
    print("5. Exit")
    print("===================================")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        total_products()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")