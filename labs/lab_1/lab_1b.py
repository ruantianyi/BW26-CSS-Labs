"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

valid = True

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """


    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'")

def main():
    global valid

    print(f"===== Simple Calculator =====")

    valid = False

    # Ask the user for sample input   
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
            result = simple_calculator(operation, num1, num2)
        except (ZeroDivisionError, ValueError) as e:
            print(f"Error: {e}. Please retry.\n")
        else:
            break


    print(f"The result of {operation}ing {num1} and {num2} is: {result}") # type: ignore


if __name__ == "__main__":
    main()
