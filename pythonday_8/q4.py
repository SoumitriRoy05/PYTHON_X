#WAP in python to read an entire text file

file=open("example.txt","r")
content = ""
while True:
        char = file.read(1)
        if char == "":
            break
        content += char
print(content)
