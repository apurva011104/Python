#Program to find the maximum of the three entered numbers.

x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
z=int(input("Enter another number: "))
if (x>y and x>z):
    print("Greatest number: ",x)
elif (y>z and y>x):
    print("Greatest number: ",y)
else:
    print("Greatest number: ",z)
