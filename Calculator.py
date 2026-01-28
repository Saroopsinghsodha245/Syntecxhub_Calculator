def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

def calculate(num1, num2, operator):
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    else:
        return "Invalid operator"

def calculator():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Perform Calculation")
        print("2. Clear")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            try:
                num1 = float(input("Enter first number: "))
                operator = input("Enter operator (+, -, *, /): ")
                num2 = float(input("Enter second number: "))

                result = calculate(num1, num2, operator)
                print("Result:", result)

            except ValueError:
                print("Error: Please enter valid numbers.")

        elif choice == '2':
            print("Calculator cleared.")

        elif choice == '3':
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

calculator()
