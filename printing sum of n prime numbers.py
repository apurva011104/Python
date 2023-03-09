 #Write a program to print sum of n numbers

n=int(input("Enter number of prime numbers you want to find sum of: "))
i=1
sumprime=0
c=0
while(i<=n+1):
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
    if(c==2):
        sumprime=sumprime+i
    c=0
    i=i+1
print("Sum of {0} prime numbers: {1}".format(n,sumprime))   
