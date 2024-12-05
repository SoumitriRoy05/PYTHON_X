def tuples(tuples):
    addition = sum(tuples)
    multiplication = 1
    for num in tuples:
        multiplication *= num
    return addition, multiplication

user_input = input("Enter numbers separated by commas: ")
tuple_of_numbers = tuple(map(int, user_input.split(',')))

addition, multiplication = tuples(tuple_of_numbers)
print(f"Addition: {addition}, Multiplication: {multiplication}")
