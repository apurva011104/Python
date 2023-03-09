#Write a Python program to accept a co-ordinate point in a x-y co-ordinate system and determine in which quadrant the co-orinate point lies

x=int(input("Enter x co-ordinate:"))
y=int(input("Enter y co-ordinate:"))
if(x>0):
    if(y>0):
        print("First quadrant")
    elif(y<0):
        print("Fourth quadrant")
    else:
        print("On x-axis")
elif(x<0):
    if(y>0):
        print("Second quadrant")
    elif(y<0):
        print("Third quadrant")
    else:
        print("On x-axis")
else:
    if(y<0 or y>0):
        print("On y-axis")
    else:
        print("On origin")
