#A file contains a word “donkey” multiple times. You need to write a program which replaces this word with $$$$$ by updating the same file

f=open("animals.txt","w")
f.write("The donkey is a domesticated animal. Donkey can carry loads.")
f=open("animals.txt","r")
content = f.read()
content = content.replace("donkey", "$$$$$")
f=open("animals.txt","w")
f.write(content)
print("The word 'donkey' has been replaced with '$$$$$'.")
