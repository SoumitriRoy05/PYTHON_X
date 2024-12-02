def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes_in_range(start, end):
    return sum(i for i in range(start, end + 1) if is_prime(i))

# Range 11 to 100
start = 11
end = 100

# Calculating the sum of prime numbers in the range
sum_primes = sum_of_primes_in_range(start, end)

# Output the result
print(f"The sum of prime numbers between {start} and {end} is: {sum_primes}")
