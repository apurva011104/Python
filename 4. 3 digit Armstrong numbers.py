#Program to find the series of all three digits Armstrong number.

for n in range (100,1000):
    t=n
    c=0
    while (n!=0):
        n=int(n/10)
        c=c+1
    n=t
    s=0
    for i in range(c,0,-1):
        n=int(n/(10**(i-1)))
        n=int(n**c)
        s=s+n
        n=t
        n=int(n%(10**(i-1)))
    n=t
    if(s==n):
        print(n)
        
