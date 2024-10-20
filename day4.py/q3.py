n=int(input("Enter a number:"))
m=int(input("Enter a number:"))
HCF=1
for i in range(2,n+1):
    if(n%i==0 and m%i==0):
        HCF=i
LCM=int((n*m)/(HCF))
print(f"HCF={HCF}")
print(f"LCM={LCM}")