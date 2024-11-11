# exception_handling.py

try:
    # Ask the user to enter two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Try dividing the two numbers
    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Error: Please enter a valid integer.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# This block will execute regardless of an error
finally:
    print("Execution complete.")
