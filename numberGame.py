#This is a random Number guessing game...
#Made without the use of functions 
#Used only conditional and looping statments

import random as r
count=1
print("Number Game \n")
print("1.Easy (b/w 0 & 200) 30-Chances\n2.Medium (b/w 0 & 700) 25-Chances\n3.Difficult (b/w 0 & 1000) 20-Chances\n4.Hard (b/w 0 & 3000) 15-Chances")
num=int(input("Enter your choice >> "))
print("\nGame starts.. Enjoy it ....\n")
sol=int(input("Take your guess >> "))
if num==1:
    x=r.randint(0,200)
    # count=30
    while count<=30 and sol!=x:
        attempt=str(count+1)
        
        if sol>x:
            print("Lower number ")
            sol=int(input("Take your guess >> "))
        elif sol<x:
            print("Higher number")
            sol=int(input("Take your guess >> "))
        
        count+=1
    if sol==x and count<=30:
        print("You Won..!\nYou guessed in "+attempt+" attempts")
    elif count>30:
        actual=str(x)
        print("\nThe number was "+actual+" ")
        print("\nYou Lost..Exceeded maximum attempts\nBetter Luck next time")


elif num==2:
    x=r.randint(0,700)
    # count=25
    while count<=25 and sol!=x:
        attempt=str(count+1)
        
        if sol>x:
            print("Lower number ")
            sol=int(input("Take your guess >> "))
        elif sol<x:
            print("Higher number")
            sol=int(input("Take your guess >> "))
        
        count+=1
    if sol==x and count<=25:
        print("You Won..!\nYou guessed in "+attempt+" attempts")
    elif count>25:
        actual=str(x)
        print("\nThe number was "+actual+" ")
        print("\nYou Lost..Exceeded maximum attempts\nBetter Luck next time")


elif num==3:
    x=r.randint(0,1000)
    # count=20
    while count<=20 and sol!=x:
        attempt=str(count+1)
        
        if sol>x:
            print("Lower number ")
            sol=int(input("Take your guess >> "))
        elif sol<x:
            print("Higher number")
            sol=int(input("Take your guess >> "))
        
        count+=1
    if sol==x and count<=20:
        print("You Won..!\nYou guessed in "+attempt+" attempts")
    elif count>20:
        actual=str(x)
        print("\nThe number was "+actual+" ")
        print("\nYou Lost..Exceeded maximum attempts\nBetter Luck next time")


elif num==4:
    x=r.randint(0,3000)
    # count=15
    while count<=15 and sol!=x:
        attempt=str(count+1)
        
        if sol>x:
            print("Lower number ")
            sol=int(input("Take your guess >> "))
        elif sol<x:
            print("Higher number")
            sol=int(input("Take your guess >> "))
        
        count+=1
    if sol==x and count<=15:
        print("You Won..!\nYou guessed in "+attempt+" attempts")
    elif count>15:
        actual=str(x)
        print("\nThe number was "+actual+" ")
        print("\nYou Lost..Exceeded maximum attempts\nBetter Luck next time")
        


else:
    print("Invalid choice..Restart the game")


