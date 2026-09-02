print("===== BILL SPLITTER =====")

try:
    bill = float(input("Enter total bill amount: ₹"))
    people = int(input("Enter number of people: "))
    tip = float(input("Enter tip percentage: "))

    if bill <= 0:
        raise ValueError("Bill must be greater than 0")

    if people <= 0:
        raise ValueError("Number of people must be greater than 0")

    if tip < 0:
        raise ValueError("Tip percentage cannot be negative")

    tip_amount = bill * tip / 100
    total_bill = bill + tip_amount
    each_person = total_bill / people

except ValueError as error:
    print("Error:", error)

else:
    print("\n===== BILL SUMMARY =====")
    print(f"Original Bill : ₹{bill:.2f}")
    print(f"Tip Amount    : ₹{tip_amount:.2f}")
    print(f"Total Bill    : ₹{total_bill:.2f}")
    print(f"People        : {people}")
    print(f"Each Person   : ₹{each_person:.2f}")

finally:
    print("\nThank you for using Bill Splitter! 💰")