n = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(n):
 num = int(input(f"Enter number {i+1}: "))
 numbers.append(num)
positive_count = 0
negative_count = 0
zero_count = 0
for num in numbers:
 if num > 0:
  positive_count += 1
 elif num < 0:
  negative_count += 1
 else:
  zero_count += 1
print(f"Number of positive numbers:{positive_count}")
print(f"Number of negative numbers:{negative_count}")
print(f"Number of zeros:{zero_count}")