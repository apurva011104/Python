#write a program to print even numbers in a given range

x=int(input("Enter starting range:"))
y=int(input("Enter ending range:"))
print("Even numbers:")
for i in range(x,y+1):
    if(i%2==0):
        print(i)
print("Odd numbers:")
for i in range(x,y+1):
    if(i%2==1):
        print(i)
