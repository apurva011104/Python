"""
Write a program to input  electricity unit charges and calculate total bill according to following conditions:
1. For first 50 units: charges 0.5Rs per unit
2. For next 100 units: charges 0.75 Rs per unit
3. For next 100 units: charges 0.12 Rs per unit
4. For units above 250 units: charges 1.5Rs per unit
5. Add additional sub charge of 20% is added to the bills
"""
x=int(input("Enter number of units:"))
if(x>250):
    c=(0.5*50)+(0.75*100)+(0.12*100)+(1.5*(x-250))
    sc=(0.2*c)+c
    print("Total: {0}".format(sc))
elif(x>150 and x<=250):
    c=(0.5*50)+(0.75*100)+(0.12*(x-150))
    sc=(0.2*c)+c
    print("Total: {0}".format(sc))
elif(x>50 and x<=150):
    c=(0.5*50)+(0.75*(x-50))
    sc=(0.2*c)+c
    print("Total: {0}".format(sc))
else:
    c=0.5*x
    sc=(0.2*c)+c
    print("Total: {0}".format(sc))
