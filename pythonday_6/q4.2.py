#Write a programme in Python to check a user inputted string is palindrome
#without function

str_input = input("Enter a string: ")  
revstr = ""
for i in str_input:
    revstr = i + revstr
print(f"The Reversed string: {revstr}")
if str_input == revstr:
    print(f"{revstr} is a palindrome")
else:
    print(f"{revstr} is not a palindrome")
