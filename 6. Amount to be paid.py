#Big Bazaar specifies its customer into three categories as Bronze, Silver and Gold.If the shopping amount is greater than 25000, the category is GOLD. If the shopping amount is between 10000 and 25000, the category is SILVER, otherwise the category is BRONZE. The discount offered for GOLD customers is 20% of the shopping amount, for SILVER customers is 10% of the shopping amount and 5% otherwise. Design a program in python that asks the user to input the total shopping amount, outputs the category and amount to be paid.

x=float(input("Enter the total shopping amount: "))
if (x>=25000):
    dis=(20/100)*x
    total=x-dis
    print("Category: GOLD\nDiscount: {0}\nAmount to be paid: {1}".format(dis,total))
elif(x>=1000 and x<25000):
    dis=(10/100)*x
    total=x-dis
    print("Category: SILVER\nDiscount: {0}\nAmount to be paid: {1}".format(dis,total))
else:
    dis=(5/100)*x
    total=x-dis
    print("Category: BRONZE\nDiscount: {0}\nAmount to be paid: {1}".format(dis,total))
