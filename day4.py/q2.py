#WAP to input a number through user and check whether the number is:

#a. Armstrong number
#b. Perfect number
#c. Adam number
#d. Palindrome number

n=int(input("Enter a number:"))
def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    sum_of_powers = sum(int(digit) ** num_len for digit in num_str)
    return sum_of_powers == n

def is_perfect_number(n):
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_of_divisors == n

def is_adam_number(n):
    def reverse_num(num):
        return int(str(num)[::-1])

    def square(num):
        return num * num

    return square(reverse_num(n)) == reverse_num(square(n))

def is_palindrome_number(n):
    num_str = str(n)
    return num_str == num_str[::-1]

# Check and print the results
print(f"{n} is an Armstrong number: {is_armstrong_number(n)}")
print(f"{n} is a Perfect number: {is_perfect_number(n)}")
print(f"{n} is an Adam number: {is_adam_number(n)}")
print(f"{n} is a Palindrome number: {is_palindrome_number(n)}")

