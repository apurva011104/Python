#Program to input two numbers and print the swapped values of them.

x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
print("Before swapping:\nx={0}\ty={1}".format(x,y))
c=x
x=y
y=c
print("After swapping:\nx={0}\ty={1}".format(x,y))
