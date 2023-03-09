#Program to find wheter a triangle is scalene, isosceles, equilateral, right angled triangle or invalid when the sides of the triangle are entered by the user.

x=int(input("Enter value of one side: "))
y=int(input("Enter value of second side: "))
z=int(input("Enter value of third side: "))
if((x+y)>z and (y+z)>x and (z+x)>y):
    if(x==y and y==z and z==x):
        print("Equilateral triangle")
    elif(x==y or y==z or z==x):
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
    a=x**2
    b=y**2
    c=z**2
    if((a+b)==c or (b+c)==a or (c+a)==b):
        print("Right angled triangle")
else:
    print("Invalid")
