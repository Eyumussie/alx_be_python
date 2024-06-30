def perform_calculation():
    try:
        num1 = float(input("Enter the first number: ").strip())
        num2 = float(input("Enter the second number: ").strip())
    except ValueError:
        print("Please enter valid numbers.")
        return
    operation = input("Choose the operation (+, -, *, /): ").strip()
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}")
        case "-":
            result = num1 - num2
            print(f"The result is {result}")
        case "*":
            result = num1 * num2
            print(f"The result is {result}")
        case "/":
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}")
            else:
                print("Cannot divide by zero.")
        case _:
            print("Invalid operation. Please choose from +, -, *, or /.")
if __name__ == "__main__":
    perform_calculation()
