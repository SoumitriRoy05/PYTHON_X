#WAP to sort the following list.
#list1 = [25, 47, -23, 0, -50, 24, 8, 1, 9, 10]

list1 = [25, 47, -23, 0, -50, 24, 8, 1, 9, 10]
n = len(list1)
for i in range(n):
 for j in range(0, n-i-1):
  if list1[j] > list1[j+1]:
   list1[j], list1[j+1] = list1[j+1], list1[j]
print(f"The Sorted list is:{list1}")
