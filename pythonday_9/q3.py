#Write a program to make a copy of a text file “Galaxy.txt”. [Galaxy.txt contains minimum 25 galaxies name those are discover by NASA Hubble space telescope]

f=open("Galaxy.txt","w")
f.write("Andromeda\nMilky Way\nTriangulum\nWhirlpool\n...\n")
source=open("Galaxy.txt","r")
content = source.read()
destination=open("Galaxy_copy.txt","w")
destination.write(content)
print("Galaxy.txt copied to Galaxy_copy.txt successfully.")
