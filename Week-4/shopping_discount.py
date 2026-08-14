# Shopping Discount Calculator

def calculate_discount():

    try:
        name = input("Enter customer name: ")
        amount = float(input("Enter shopping amount: "))

        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        if amount >= 5000:
            discount = 20
        elif amount >= 3000:
            discount = 15
        elif amount >= 1000:
            discount = 10
        else:
            discount = 5

        discount_amount = amount * discount / 100
        final_amount = amount - discount_amount

        print("\n========== SHOPPING BILL ==========")
        print("Customer       :", name)
        print("Original Amount: ₹", amount)
        print("Discount       :", discount, "%")
        print("Discount Amount : ₹", discount_amount)
        print("Final Amount   : ₹", final_amount)

    except ValueError as error:
        print("Error:", error)

    except Exception:
        print("Something unexpected happened.")

    finally:
        print("Thank you for shopping!")


calculate_discount()