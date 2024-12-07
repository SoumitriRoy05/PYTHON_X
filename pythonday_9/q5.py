# Write a python program to rename a file to “renamed_by_python.txt”

original_file=open("poems.txt","r")
content = original_file.read()
new_file=open("renamed_by_python.txt","w")
new_file.write(content)
original_file=open("poems.txt","w")
pass  
print("File has been renamed to 'renamed_by_python.txt'")
