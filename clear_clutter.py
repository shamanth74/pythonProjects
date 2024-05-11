#This is an simple python program to rename all the files of particular format in an directory with a sequence of numbers 
#This is built while learning concept of OOP'S and by using OS module in python

import os
class ClearClutter:
    def __init__(self,path,type):
        self.path=path
        self.type=type
        if os.path.exists(f"{self.path}"):
            pass
        else:
            print("Invalid path")
            exit()

    def rename(self):
        files=os.listdir(self.path)
        i=1
        count=0
        for file in files:
            if file.endswith(f".{self.type}"):
                count=1
                os.rename(f"{self.path}/{file}",f"{self.path}/{i}.{self.type}")
                i=i+1
        if count==0:
            print(f"Type specified doesn't exists in {self.path}")
        else:
            print(f"Renamed Sucessfully")

path=input("Enter the path where file exists --> ")
type=input("The type of the file --> ")
f1=ClearClutter(path,type)
f1.rename()