def calculator():
    # Get user input for the two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Display the operations
    print("Select the operation you want to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input for the operation
    operation = input("Enter the operation (1/2/3/4): ")

    # Perform the operation based on user input
    if operation == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation selected.")

# Run the calculator function
calculator()
