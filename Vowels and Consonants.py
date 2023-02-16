x=str(input())
if(x>="A" and x<="Z" or x>="a" and x<="z"):
    if(x=="A" or x=="E" or x=="I" or x=="O" or x=="U" or x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):
        print("Vowel.")
    else:
        print("Consonant.")
else:
    print("Not an alphabet.")
