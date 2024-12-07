#Write a program to wipe out the contents of a file using python. [Create that text file named as planets.txt that contains list of planets in the solar system]

f=open("planets.txt","w")
f.write("Mercury\nVenus\nEarth\nMars\nJupiter\nSaturn\nUranus\nNeptune")
f=open("planets.txt","w")
f.truncate(0) 
print("Contents of planets.txt have been wiped out.")
