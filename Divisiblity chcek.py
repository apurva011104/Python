#Write a program to check wheter a number 1 is divisible by number 2

x=int(input("Enter the dividend: "))
y=int(input("Enter the divisior:"))
z=x%y
if(z==0):
    print("{0} is divisible by {1}".format(x,y))
else:
    print("{0} is dividible by {1}".format(x,y))
