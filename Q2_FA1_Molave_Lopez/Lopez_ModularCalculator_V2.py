# Lopez_ModularCalculator_V2.py
# Version 2: Improved modular calculator
# Author: Ronn Gabriel O. Lopez


# Function for addition
def add_numbers(num1, num2):
    return num1 + num2


# Function for subtraction
def subtract_numbers(num1, num2):
    return num1 - num2


# Function for multiplication
def multiply_numbers(num1, num2):
    return num1 * num2


# Function for division
def divide_numbers(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2


# Display the calculator title
print("=== MODULAR CALCULATOR ===")

# Get the first number
try:
    num1 = float(input("Enter first number: "))

    # Get the second number
    num2 = float(input("Enter second number: "))

    # Display available operations
    print("\nChoose operation:")
    print("1 - Addition (+)")
    print("2 - Subtraction (-)")
    print("3 - Multiplication (*)")
    print("4 - Division (/)")

    choice = input("\nEnter choice (1-4): ")

    # Select and perform the operation
    if choice == "1":
        result = add_numbers(num1, num2)
        symbol = "+"

    elif choice == "2":
        result = subtract_numbers(num1, num2)
        symbol = "-"

    elif choice == "3":
        result = multiply_numbers(num1, num2)
        symbol = "*"

    elif choice == "4":
        result = divide_numbers(num1, num2)
        symbol = "/"

    else:
        result = None
        print("\nError: Invalid operation choice.")

    # Display the answer if the operation was valid
    if choice in ("1", "2", "3", "4"):
        if result is None:
            print("\nError: Cannot divide by zero.")
        else:
            print("\n=== CALCULATION RESULT ===")
            print(f"{num1:g} {symbol} {num2:g} = {result:g}")

except ValueError:
    print("\nError: Please enter valid numbers.")
