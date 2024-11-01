
char_count = 0
word_count = 0
line_count = 0
file=open("example.txt","r")
for line in file:
        line_count += 1
        in_word = False
        for char in line:
            char_count += 1
            if char not in (' ', '\t', '\n'):
                if not in_word:
                    word_count += 1
                    in_word = True
            else:
                in_word = False
print(f"Characters: {char_count}")
print(f"Words: {word_count}")
print(f"Lines:{line_count}")
