"""
A man has certain number of apples.
If he picks them in a group of 7, he can pick all of them.
If he picks them in a group of 6, 1 apple is left behind.
If he picks them in a group of 5, 1 apple is left behind.
If he picks them in a group of 4, 1 apple is left behind.
If he picks them in a group of 3, 1 apple is left behind.
If he picks them in a group of 2, 1 apple is left behind.
Write a program that identifies the minimum number of apples he has:
"""

n=7
while(n):
    if (n%7==0):
        if(n%6==1):
            if(n%5==1):
                if(n%4==1):
                    if(n%3==1):
                        if(n%2==1):
                            print("Number of apples: {0}".format(n))
                            break
    n=n+1
