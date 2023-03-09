#Write a program to print table of any number in theis format.

x=int(input("Enter a number whose table you want to print:"))
for i in range(10):
    p=x*(i+1)
    print("{0}*{1}={2}".format(x,i+1,p))
