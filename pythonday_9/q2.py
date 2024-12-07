#Write a python program to open three files planets1.txt, planets2.txt and planets3.txt. If any of these files are not present, a message without exiting the program must be printed promoting the same

files = ["planets1.txt", "planets2.txt", "planets3.txt"]

for file in files:
    try:
        with open(file, "r") as f:
            print(f"{file} opened successfully.")
    except FileNotFoundError:
        print(f"{file} is missing. Please create the file.")
