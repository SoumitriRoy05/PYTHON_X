#Write a Python program to enter a 6-digit number (for example 786531) find the sum of their increasing order powers (sum1=71+82+63+54+35+16)  and reverse the summation of digits (sum2=11+32+53+64+85+76) . find subtraction of sum2 from sum1 and print the result

num = input("Enter a 6-digit number: ")
if len(num) != 6 or not num.isdigit():
    print("Enter a valid 6-digit number!")
else:
    digits = [int(digit) for digit in num]
    sum = 0
    for i in range(6):
        sum += digits[i] ** (i + 1)
    print(f"Sum of increasing powers:{sum}")




