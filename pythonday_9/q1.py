
f=open("poems.txt","w")
f.write("Twinkle, twinkle, little star,\nHow I wonder what you are!")
f=open("poems.txt","r")
content = f.read().lower()
if "twinkle" in content and "star" in content:
  print("Both 'twinkle' and 'star' are present in the poem.")
else:
    print("'twinkle' or 'star' is missing.")