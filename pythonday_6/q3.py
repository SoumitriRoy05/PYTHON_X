#Write a Python programme to do the addition and multiplication of numbers inputted from user in the form of tuple (use function).
#[Collect the values of tuples from user then convert it into list and run function to do the addition and multiplication.]

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
