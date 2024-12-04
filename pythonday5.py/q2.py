#WAP to find the odd numbers and even numbers from the entered list and display them in two lists.

numbers=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(n):
    num=int(input(f"Enter element {i+1}: "))
numbers.append(num)
odd_num = []
even_num = []
for num in numbers:
 if num % 2 == 0:
  even_num.append(num)
 else:
  odd_num.append(num)
print(f"Even numbers:{even_num}")
print(f"Odd numbers:{odd_num}")
