#This is a random Number guessing game...
#Made with the use of functions 


import random as r

# a=max_count,  b=sol  max=highest chance

def guess(a,b,max):
    c=r.randint(0,max)
    count=1
    while count<=a and b!=c:
        attempt=str(count+1)
        
        if b>c:
            print("Lower number ")
            b=int(input("Take your guess >> "))
        elif b<c:
            print("Higher number")
            b=int(input("Take your guess >> "))
        
        count+=1
    if b==c and count<=a:
        print("You Won..!\nYou guessed in "+attempt+" attempts")
    elif count>a:
        actual=str(c)
        print("\nThe number was "+actual+" ")
        print("\nYou Lost..Exceeded maximum attempts\nBetter Luck next time")



print("Number Game \n")
print("1.Easy (b/w 0 & 200) 30-Chances\n2.Medium (b/w 0 & 700) 25-Chances\n3.Difficult (b/w 0 & 1000) 20-Chances\n4.Hard (b/w 0 & 3000) 15-Chances")
num=int(input("Enter your choice >> "))

if num>=1 and num<=4:
    print("\nGame starts.. Enjoy it ....\n")

if num==1:
   sol=int(input("Take your guess >> "))
    guess(30,sol,200)


elif num==2:
    sol=int(input("Take your guess >> "))
    guess(25,sol,700)


elif num==3:
    sol=int(input("Take your guess >> "))
    guess(20,sol,1000)


elif num==4:
    sol=int(input("Take your guess >> "))
    guess(15,sol,3000)
        


else:
    print("Invalid choice..Restart the game")


