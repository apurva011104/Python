"""
A teacher enters a classroom of 500 students. All the students were having their mobile phones in ON mode. The teacher asked the students to do the following tasks in the given order:
 Roll Number 1 shall toggle the mobile phones (ON to OFF and OFF to ON) of all students.
 Roll Number 2 shall toggle mobile phones (ON to OFF and OFF to ON) of all students whose Roll Number is a multiple of 2.
 Roll Number 3 shall toggle mobile phones (ON to OFF and OFF to ON) of all students whose Roll Number is a multiple of 3.
 Roll Number 4 shall toggle mobile phones (ON to OFF and OFF to ON) of all students whose Roll Number is a multiple of 4.
 And so on
 Roll Number 49 shall toggle mobile phones (ON to OFF and OFF to ON) of all students whose Roll Number is a multiple of 49.
 Roll Number 50 shall toggle mobile phones (ON to OFF and OFF to ON) of all students whose Roll Number is a multiple of 50.
Design a program that outputs the Roll number of students whose mobile phone is still in OFF mode.
"""

for n in range (1,501):
    x=0                 
    r=1                        
    if(r==1):
        x=1
    while (r<=50):
        for z in range (2,51):
            if(r==z):
                if(n%z==0):
                    if(x==1):
                        x=0
                    else:
                        x=1
        r=r+1
    if(x==1):
        print(n)
