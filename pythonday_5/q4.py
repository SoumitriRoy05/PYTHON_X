lst_1 = []
n_1 = int(input("Enter elements for the first list: "))
for i in range(n_1):
 lst_1.append(int(input(f"Enter element {i+1}: ")))
lst_2 = []
n_2 = int(input("Enter elements for the second list: "))
for i in range(n_2):
 lst_2.append(int(input(f"Enter element {i+1}: ")))
common_elements = []
for element in lst_1:
 if element in lst_2 and element not in common_elements:
  common_elements.append(element)
print("Common elements are:", common_elements)
