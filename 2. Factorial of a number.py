#Program to find the factorial of an entered number.

n=int(input("Enter a number whose factorial you want to find: "))
p=1
for i in range (1,n+1):
    p=p*i
print("Factorial: ",p)
