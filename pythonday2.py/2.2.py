num = input("Enter a 6-digit number: ")
if len(num) != 6 or not num.isdigit():
    print("Enter a valid 6-digit number!")
else:
    digits = [int(digit) for digit in num]
    sum = 0
    for i in range(6):
        sum += digits[i] ** (i + 1)
    print(f"Sum of increasing powers:{sum}")




