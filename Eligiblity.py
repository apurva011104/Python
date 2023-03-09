"""
Write a python program to find the eligiblity of admission for a professinal course based on the following criteria:
1. Marks in Maths >=65
2. Marks in Physics >=55
3. Marks in Chemistry >= 50
"""
x=int(input("Enter marks of Maths:"))
y=int(input("Enter marks of Physics:"))
z=int(input("Enter marks of Chemistry:"))
if(x>=65 and y>=55 and z>=50):
    print("Eligible")
else:
    print("Not eligible")
