# create a calculator that takes two numbers and an operator (+, -, *, /) and
# performs the operation.
# Handle division by zero and invalid input errors.

try:
    num1 = float(input("Enter the first number:"))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == '+':
        result = num1 + num2
        print("Result: ", result)
    elif operator == '-':
        result = num1 - num2
        print("Result: ", result)
    elif operator == '*':
        result = num1 * num2
        print("Result: ", result)
    elif operator == '/':
        if num2 ==0:
            print("Error: Division by zero is not allowed")
        else:
            result = num1 / num2
            print("Result:", result)
    else:
        print("Error: Invalid operator. Please use +, -, *, or /. ")

except ValueError:
    print("Error: Please enter valid numeric values. ")