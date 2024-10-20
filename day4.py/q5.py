#String Conversion
def convert_to_uppercase(string):
    """Converts a lowercase string to uppercase without using built-in functions.
    Args:
        string (str): The lowercase string to convert.
    Returns:
        str: The converted uppercase string.
    """
    uppercase_string = ""
    for char in string:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            uppercase_string += chr(ascii_value - 32)
        else:
            uppercase_string += char
    return uppercase_string
string = input("Enter a lowercase string: ")
uppercase_string = convert_to_uppercase(string)
print("Uppercase string:", uppercase_string)