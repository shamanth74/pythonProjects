#This is a simple HealthManagment system which creates a new file for every user where the data of food and workout can be stored 
#This stored data can be viewed at any pint of time
#This was made to practise file operations in python


def getdate():
        import datetime
        return datetime.datetime.now()   

def entry(user,time,type):
    f=open(user+"_"+type+".txt","a")
    entry=input("Enter your "+type+" details >> ")
    f.write("["+time+"]"+"  "+entry+"\n")
    print("\nSucessfully entered your "+type+" details")
    f.close()
     
def view(user,type):
    f=open(user+"_"+type+".txt","r")
    content=f.read()
    print(content)
    f.close()


t=getdate()
date=str(t)
name=input("Enter your name >> ")

print("1.Entry\n2.View")
x=input("Enter your choice >> ")

print("1.Food\n2.Exercise")
y=input("Enter your choice >> ")

try:
    choice=int(y)
    task=int(x)
    if(choice==1 and task==1):
        entry(name,date,"Food")
    elif(choice==1 and task==2):
        view(name,"Food")

    elif(choice==2 and task==1):
        entry(name,date,"Exercise")

    elif(choice==2 and task==2):
        view(name,"Exercise")
    else:
     print("Invalid entry")

except Exception as e:
     print("Invalid entry")
