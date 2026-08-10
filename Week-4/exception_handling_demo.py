# Exception Handling Demo

print("Simple Calculator")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Calculation completed successfully.")

finally:
    print("Program ended.")