#Write a program to print the sum of prime numbers in a given range

x=int(input("Enter starting range:"))
y=int(input("Enter ending range:"))
c=0
sumprime=0
for i in range(x,y+1):
    for j in range(1,i+1):
        if(i%j==0):
           c= c+1
    if(c==2):
        sumprime=sumprime+i
    c=0
print("Sum of all prime numbers: {0}".format(sumprime))
