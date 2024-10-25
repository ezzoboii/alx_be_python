# match_case_calculator.py

# Step 1: Prompt user for input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")
except ValueError:
    print("Invalid input. Please enter numeric values for the numbers.")
else:
    # Step 2: Perform the calculation using match case
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")
        
        case '/':
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}.")
            else:
                print("Cannot divide by zero.")
        
        case _:
            print("Invalid operation. Please choose from (+, -, *, /).")

# End of the script

