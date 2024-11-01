
f=open("Galaxy.txt","w")
f.write("Andromeda\nMilky Way\nTriangulum\nWhirlpool\n...\n")
source=open("Galaxy.txt","r")
content = source.read()
destination=open("Galaxy_copy.txt","w")
destination.write(content)
print("Galaxy.txt copied to Galaxy_copy.txt successfully.")