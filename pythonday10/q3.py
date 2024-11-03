
a = int(input("Enter the numerator (a): "))
b = int(input("Enter the denominator (b): "))
try:
    result = a / b
    print(f"Result:{result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero (ZeroDivisionError)")
finally:
    print("Execution completed, whether there was an error or not.")

