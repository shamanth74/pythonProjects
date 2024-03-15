# It is a simple python program of a simple calculator which can perform with only 1 operator and n number of operands
# This progam is built without the use of functions and by only using if-else condition and for loop


ls=[]
num=int(input("Enter the number of operands >> "))
ans=0

if num>1:
    for i in range(0,num):                          #storing operands as list
        val=str(i+1)
        ele=int(input("Enter the element number "+val+" >>"))
        ls.append(ele)

    operator=str(input("Enter + , - , * , /  >>"))     

    if operator=='+':                                #addition  
        for j in ls:
            ans=ans+j
        print("The answer is >> ",ans)
        

    elif operator=='-':                              #subtraction
        for j in ls:
            ans=j-ans
        print("The answer is >> ",(-ans))


    elif operator=='*':                             #multiplication
        ans=1
        for j in ls:
            ans=ans*j
        print("The answer is >> ",ans)


    elif operator=='/' and len(ls)==2:              #division
        for j in ls:
            ans=(ls[0]/ls[1])
        print("The answer is >> ",ans)


    elif operator=='/' and len(ls)>2:
        print("You should use only 2 operands for division ")


    else:
        print("Please select a valid operator")
        

else:
    print("You should select more than 1 operand")              #error


    



