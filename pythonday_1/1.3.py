#WAP to input principal amount, interest and time then calculate rate of interest.

p_amount=int(input("Enter amount:"))
time=int(input("enter time:"))
rate=float(input("Enter interest:"))
rate_of_interest=(rate*100)/(p_amount*time)
print("Rate of interest:", rate_of_interest)
