#Design a program in python to display the number of days left in the current year (2023), when today's date is entered by the user in format of your choice.


d=int(input("Enter date: "))
m=int(input("Enter month: "))
if(m==1):
    print("No. of days left: ",365-d)
elif(m==2):
    print("No. of days left: ",365-d-31)
elif(m==3):
    print("No. of days left: ",365-d-31-28)
elif(m==4):
    print("No. of days left: ",365-d-31-28-31)
elif(m==5):
    print("No. of days left: ",365-d-31-28-31-30)
elif(m==6):
    print("No. of days left: ",365-d-31-28-31-30-31)
elif(m==7):
    print("No. of days left: ",365-d-31-28-31-30-31-30)
elif(m==8):
    print("No. of days left: ",365-d-31-28-31-30-31-30-31)
elif(m==9):
    print("No. of days left: ",365-d-31-28-31-30-31-30-31-31)
elif(m==10):
    print("No. of days left: ",365-d-31-28-31-30-31-30-31-31-30)
elif(m==11):
    print("No. of days left: ",365-d-31-28-31-30-31-30-31-31-30-31)
elif(m==12):
    print("No. of days left: ",365-d-31-28-31-30-31-30-31-31-30-31-30)
