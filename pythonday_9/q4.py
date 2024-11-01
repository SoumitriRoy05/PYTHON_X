
f=open("planets.txt","w")
f.write("Mercury\nVenus\nEarth\nMars\nJupiter\nSaturn\nUranus\nNeptune")
f=open("planets.txt","w")
f.truncate(0) 
print("Contents of planets.txt have been wiped out.")