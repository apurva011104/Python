#Program to find whether  an entered number is prime or not.

n=int(input("Enter a number: "))
c=0
if (n>1):
    for i in range (1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        print("Prime")
    else:
        print("Composite")
else:
    print("Neither prime nor composite")
