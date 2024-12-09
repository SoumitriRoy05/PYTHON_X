#Write a program in python to demonstrate different types of Exceptions and Errors

print("Example of ZeroDivisionError:")
a = 10
b = 0
if b == 0:
    print("Cannot divide by zero (ZeroDivisionError)")
else:
    print("Result:", a / b)
print("\nExample of ValueError:")
try:
    number = int("not_a_number") 
except ValueError:
    print("Cannot convert a non-numeric string to an integer (ValueError)")

# Example of IndexError
print("\nExample of IndexError:")
my_list = [1, 2, 3]
index = 5
if index >= len(my_list):
    print("Index out of range (IndexError)")
else:
    print(f"Element at index { index} , is:, {my_list[index]}")
print("\nExample of TypeError:")
x = "Hello"
y = 5
try:
    result = x + y  
except TypeError:
    print("Cannot add string and integer (TypeError)")
print("\nExample of KeyError:")
my_dict = {"a": 1, "b": 2}
key = "c"
if key in my_dict:
    print(f"Value:", my_dict[key])
else:
    print("Key not found in dictionary (KeyError)")
print("\nExample of NameError:")
try:
    print(undefined_variable) 
except NameError:
    print("Variable is not defined (NameError)")
