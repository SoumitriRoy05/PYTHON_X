#WAP to input principal amount, rate of interest and time then calculate simple interest and cumulative interest

c_amount=int(input("enter amount:"))
rate=float(input("enter the rate:"))
time=int(input("enter time:"))

amount=c_amount*(pow((1+rate/100),time))
c_interest=amount-c_amount
print(f"Compound interest:{c_interest}")
print("simple interest:{(c_amount*rate*time)/100}")
