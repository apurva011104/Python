#Write a program to calculate the sum of even numbers and odd numbers between the given range.

x=int(input("Enter starting range:"))
y=int(input("Enter ending range:"))
sumeven=0
sumodd=0
for i in range(x+1,y):
    if(i%2==0):
        sumeven=sumeven+i
    if(i%2==1):
        sumodd=sumodd+i
print("Sum of even numbers: {0} \n Sum of odd numbers: {1}".format(sumeven,sumodd))
