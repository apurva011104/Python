#Program to find Compound interest compounded annually and the total amount when the Principal, Rate of interest and time entered by the user.

p=int(input("Enter the value of principal: "))
r=int(input("Enter the value of rate of interest: "))
t=int(input("Enter the value of time (in years): "))
amt=p*((1+(r/100))**t)
print("Compund interest: {0}\nTotal amount: {1}".format(amt-p,amt))
