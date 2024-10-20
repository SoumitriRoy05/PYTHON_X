#arithmetic calculatore

def arithmetic_calculator():
    
    print("Addition:+")
    print("Subtraction:-")
    print("Multiplication:*")
    print(" Division:/")
    print("Modulo:%")
    print("Left Shift:<<")
    print("Right Shift:>>")

    
    num1 = float(input("Enter the  number: "))
    num2 = float(input("Enter the  number: "))
    operation = input("Enter the operator (+, -, *, /, %, <<, >>): ")

    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    elif operation == "%":
        result = num1 % num2
    elif operation == "<<":
        result = num1 << num2
    elif operation == ">>":
        result = num1 >> num2
    else:
        result = "Invalid operation!"

    print(f"Result: {result}")


arithmetic_calculator()
