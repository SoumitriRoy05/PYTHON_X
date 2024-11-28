#WAP to calculate the following equation by inputting the value of x, y and n in the range [2 to 8]


x = int(input("Enter the value of x (between 2 and 8): ")) 
y = int(input("Enter the value of y (between 2 and 8): ")) 
n = int(input("Enter the value of n (between 2 and 8): ")) 
if 2 <= x <= 8 and 2 <= y <= 8 and 2 <= n <= 8: 
    numerator = x**2 + x**3 
    denominator = (y / 4) + (y / 3) + (y**8) 
    first_part = (numerator / denominator) ** (2 * n) 
     
    second_numerator = y**6 + y**2 
    second_denominator = x**9 
    second_part = second_numerator / second_denominator 
     
    result = first_part * second_part 
 
    print("The result of the expression is:",result) 
else: 
    print("Values of x, y, and n must be within the range [2, 8].") 
