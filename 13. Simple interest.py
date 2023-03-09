#Program to find the Simple Interest and the total amount when the Principal, Rate of interest and Time are entered by the user

p=int(input("Enter the value of principal: "))
r=int(input("Enter the value of rate of interest: "))
t=int(input("Enter the value of time (in years): "))
si=(p*r*t)/100
total=p+si
print("Simple interest: {0}\nTotal amount: {1}".format(si,total))
