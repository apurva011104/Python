#Write a program to swap two values.

x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
print("Values before swapping:\nx={0}\ty={1}".format(x,y))
x=x+y
y=x-y
x=x-y
print("Values after swapping:\nx={0}\ty={1}".format(x,y))
