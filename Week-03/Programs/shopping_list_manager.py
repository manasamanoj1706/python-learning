# ===========================================
# Project : Shopping List Manager
# Author  : Manasa Manoj
# Day     : 18
# ===========================================

shopping_list = []

while True:
    print("\n===== Shopping List Manager =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Shopping List")
    print("4. Count Items")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        shopping_list.append(item)
        print(item, "added successfully!")

    elif choice == "2":
        item = input("Enter item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed successfully!")
        else:
            print("Item not found.")

    elif choice == "3":
        if len(shopping_list) == 0:
            print("Shopping list is empty.")
        else:
            print("\nShopping List:")
            for item in shopping_list:
                print("-", item)

    elif choice == "4":
        print("Total Items:", len(shopping_list))

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
