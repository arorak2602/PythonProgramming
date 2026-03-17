print("Welcome to the terminal calculator")


def calculate(a, op, b):
    # Performs basic arithmetic operations
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            print("Cannot divide by zero!")
            return None
        return a / b
    else:
        print("Wrong operation input!")
        return None


num1 = float(input("Enter the first number:\n"))

while True:
    # Main calculation loop
    op = input("Enter the operation (+, -, *, /):\n")
    num2 = float(input("Enter the second number:\n"))

    result = calculate(num1, op, num2)
    print("Result:", result)

    choice = input("Do you wish to continue with the result (y/n):\n").lower()

    if choice == "y":
        num1 = result
    else:
        print("See ya!")
        break