amount=float(input("Enter the required amount:"))
if amount in range (0<amount<=5000):
  discount_val=(amount*5)/100
elif amount in range (5000<amount<=15000):
   discount_val=(amount*12)/100
elif amount in range (15000<amount<=25000):
  discount_val=amount*(20/100)
else:
 discount_val=amount*(30/100)
print(f"AMOUNT:{amount}")
print(f"DISCOUNT RATE:{discount_val}")
print(f"FINAL PRICE:{amount-discount_val}")