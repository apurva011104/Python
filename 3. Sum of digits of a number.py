#Program to find sum of digits of an entered number.

n=int(input("Enter a number: "))
c=0
t=n
while(n!=0):
    n=int(n/10)
    c=c+1
n=t
s=0
for i in range (c,0,-1):
    n=int(n/(10**(i-1)))
    s=s+n
    n=t
    n=int(n%(10**(i-1)))
print("Sum of digits: ",s)
