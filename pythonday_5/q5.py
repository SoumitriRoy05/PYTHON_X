n = int(input("Enter the number of elements in the list: "))
number = []
for i in range(n):
 num = int(input(f"Enter element {i+1}: "))
 number.append(num)
maximum = max(number)
minimum = min(number)
average = (maximum + minimum) / 2
print(f"Maximum element:{maximum}")
print(f"Minimum element:{minimum}")
print(f"Average of maximum and minimum elements is:{average}")