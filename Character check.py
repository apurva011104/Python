#Write a program to print wheter a given character is upper case, lower case or a digit

x=str(input("Enter a character:"))
if(x>='a' and x<='z'):
    print("Lower case")
elif(x>='A' and x<='Z'):
    print("Upper case")
elif(x>='0' and x<='9'):
    print("Digit")
else:
    print("Character invalid")
