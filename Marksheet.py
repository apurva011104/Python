#Write a program to make a marksheet of a student

name=str(input("Enter the name of student: "))
rollnumber=str(input("Enter roll number: "))
classno=str(input("Enter class: "))
maths=float(input("Enter marks of Maths: "))
science=float(input("Enter marks of Science: "))
social=float(input("Enter marks of Social Science: "))
english=float(input("Enter marks of English: "))
hindi=float(input("Enter marks of Hindi: "))
computer=float(input("Enter marks of Computer: "))
total=maths+science+social+hindi+english+computer
average=total/6
percentage=(total/600)*100
print("Name: {0}         \t \t \t \t Class: {1} \nRoll Number: {2}".format(name,classno,rollnumber))
print("Subject           \t \t   Marks obtained \t \t Maximum marks")
print("Maths             \t \t             {0} \t \t           100".format(maths))
print("Science           \t \t             {0} \t \t           100".format(science))
print("Social Science    \t \t             {0} \t \t           100".format(social))
print("Hindi             \t \t             {0} \t \t           100".format(hindi))
print("English           \t \t             {0} \t \t           100".format(english))
print("Computer          \t \t             {0} \t \t           100".format(computer))
print("Total marks       \t \t             {0} \t \t           600".format(total))
print("Average: {0} \t \t \t  Percentage: {1}%".format(average,percentage))
