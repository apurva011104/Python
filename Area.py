#Write a program to find the area of circle, rectangle, triangle, rhombus and cylinder

r=float(input("Enter the radius of circle: "))
areacircle=(22/7)*r*r
print("Area of circle= {0)",format(areacircle))

l=float(input("Enter the length of rectangle: "))
b=float(input("Enter the breadth of rectangle: "))
arearectangle=l*b
print("Area of rectangle= {0}",format(arearectangle))

base=float(input("Enter the base of triangle: "))
height=float(input("Enter the height of triangle: "))
areatriangle=(1/2)*base*height
print("Area of triangle= {0}",format(areatriangle))

d1=float(input("Enter the length of one diagonal of rhombus: "))
d2=float(input("Enter the length of another diagonal of rhombus: "))
arearhombus=(1/2)*d1*d2
print("Area of rhombus= {0}",format(arearhombus))

radius=float(input("Enter the radius of cylinder: "))
height2=float(input("Enter the height of cylinder: "))
areacylinder=2*(22/7)*radius*height2
print("Area of cylinder= {0}",format(areacylinder))
