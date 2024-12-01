#Write a Python program to input 2 strings and insert side-by-side one character from string 2 in string1. (For Ex: String1="Amar", String1="Peter", result= "APmeatrr")

def merge_strings(string1, string2):
    result = ""
    for i in range(max(len(string1), len(string2))):
        if i < len(string1):
            result += string1[i]
        if i < len(string2):
            result += string2[i]
    return result


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


merged_string = merge_strings(string1, string2)
print("RESULT:", merged_string)
