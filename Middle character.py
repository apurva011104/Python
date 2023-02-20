x=str(input("Enter the string: "))
f=len(x)
c=int(f)
print("Middle character(s): ")
if(c%2==0):
    p=(c-2)/2
    q=(c/2)+1
    n=int(p)
    m=int(q)
    l=x[n:m:1]
    print(l)
if(c%2==1):
    p=(c-1)/2
    q=(c+1)/2
    n=int(p)
    m=int(q)
    l=x[n:m]
    print(l)
    
