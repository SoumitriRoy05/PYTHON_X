#WAP in python to print each line of a file in reverse order

file=open("example.txt","r")
lines = file.readlines()
for line in lines:
        line = line.strip()
        reversed_line = ""
        for i in range(len(line) - 1, -1, -1):
            reversed_line += line[i]
        print(reversed_line)
