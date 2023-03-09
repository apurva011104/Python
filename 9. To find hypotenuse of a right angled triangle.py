#Program to find the hypotenuse of a right angled triangle, when the base and height are entered by the user

b=int(input("Enter the value of base: "))
h=int(input("Enter the value of height: "))
x=(b**2)+(h**2)
print("Hypotenuse: {0} units".format(x**(1/2)))
