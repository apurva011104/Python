"""
Program to display the table of an entered number in the format:
2*1=2
2*2=4
.............
2*10=20
"""

n=int(input("Enter the number whose table you want to print: "))
for i in range (10):
    print("{0}*{1}={2}".format(n,i+1,n*(i+1)))
