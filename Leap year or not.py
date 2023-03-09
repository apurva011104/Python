#Write a python program to check wheter an entered year is an leap year or not

x=int(input("Enter a year: "))
if(x%100==0):
    if(x%400==0):
        print("Leap year")
    else:
        print("Not a leap year")
else:
    if(x%4==0):
        print("Leap year")
    else:
        print("Not a leap year")
