

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
