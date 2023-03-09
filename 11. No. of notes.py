n=int(input("Enter the amount to be withdrawn: "))
if(n>=2100):
    x=(n-100)%2000
    y=(n-100)/2000
    y=int(y)
    if(x>=500):
        z=x%500
        z1=x/500
        z1=int(z1)
        if(z>=100):
            h=z/100
            h=int(h)
            print("Type of note\t\t\tNo. of notes")
            print("Rs. 2000       \t\t\t {0}".format(y))
            print("Rs. 500         \t\t\t {0}".format(z1))
            print("Rs. 100         \t\t\t {0}".format(h+1))
        else:
            print("Type of note\t\t\tNo. of notes")
            print("Rs. 2000       \t\t\t {0}".format(y))
            print("Rs. 500         \t\t\t {0}".format(z1))
            print("Rs. 100         \t\t\t 1")
    else:
        h=x/100
        h=int(h)
        print("Type of note\t\t\tNo. of notes")
        print("Rs. 2000       \t\t\t {0}".format(y))
        print("Rs. 500         \t\t\t 0")
        print("Rs. 100         \t\t\t {0}".format(h+1))
else:
    if(n>=100):
        x=(n-100)%500
        x1=(n-100)/500
        x1=int(x1)
        if(x>100):
            h=x/100
            h=int(h)
            print("Type of note\t\t\tNo. of notes")
            print("Rs. 2000       \t\t\t 0")
            print("Rs. 500         \t\t\t {0}".format(x1))
            print("Rs. 100         \t\t\t {0}".format(h+1))
        else:
            print("Type of note\t\t\tNo. of notes")
            print("Rs. 2000       \t\t\t 0")
            print("Rs. 500         \t\t\t {0}".format(x1))
            print("Rs. 100         \t\t\t 1")
    else:
            print("Type of note\t\t\tNo. of notes")
            print("Rs. 2000       \t\t\t 0")
            print("Rs. 500         \t\t\t 0")
            print("Rs. 100         \t\t\t 0")
