file = open("myfile1.txt", "r")
text = file.read()
file.close()
char_frequency = {}
for char in text:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
for char, frequency in char_frequency.items():
    print(f"CHARECTER FREQUENCY->'{char}': {frequency}")
