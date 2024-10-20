def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Division by zero is undefined!"
    else:
        return "Invalid operation!"
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operation (add/subtract/multiply/divide): ").lower()

result = calculator(a, b, operation)
print(f"Result:{result}")
