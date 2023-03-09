#Program that calculates the number of rectangle tiles required to cover a rectangular floor if the dimensions of the floor and the dimensions of a tile are entered by the floor.

l1=int(input("Enter the value of length of floor: "))
b1=int(input("Enter the value of breadth of floor: "))
l2=int(input("Enter the value of length of tile: "))
b2=int(input("Enter the value of breadth of tile: "))
n=(l1*b1)/(l2*b2)
print("No. of rectangular tiles required: ",n)
