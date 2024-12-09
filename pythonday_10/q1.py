a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
try:
    result = a / b
    print(f"Result of a/b:,{ result}")
except ZeroDivisionError:
    print("Result of a/b: infinite")