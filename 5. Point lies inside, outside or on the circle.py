#Program to input the centre of a circle, radius of the circle and an arbitrary point P(x,y) and determine whether the point is inside the circle, on the circle or outside the circle,

xg=int(input("Enter the x-coordinate of centre of circle: "))
xf=int(input("Enter the y-coordinate of centre of circle: "))
rd=int(input("Enter the radius of circle: "))
x=int(input("Enter x-coordinate of arbitrary point: "))
y=int(input("Enter y-coordinate of arbitrary point: "))
a=(x-xg)**2
b=(y-xf)**2
r=rd**2
if((a+b)<r):
    print("Point P({0},{1}) lies inside the circle.".format(x,y))
elif((a+b)>r):
    print("Point P({0},{1}) lies outside the circle.".format(x,y))
else:
    print("Point P({0},{1}) lies on the circle.".format(x,y))
