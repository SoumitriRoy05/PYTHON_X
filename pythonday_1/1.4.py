#WAP to input principal amount, rate of interest and interest then calculate time
p_amount=int(input("Enter amount:"))
rate_of_interest=int(input("enter rate of interest:"))
rate=int(input("Enter rate:"))
time=(rate_of_interest*100)/(p_amount*rate)
print("Time period:", time)
