#This program helps organize files by moving them into folders based on their type. You provide a path where the files are located and specify the type 
#of files you want to organize. Then, the program checks if there are files of that type in the specified path. If yes, it creates a folder for that type 
#and moves those files into it. If the folder already exists, it moves the files into it. If no files of that type are found, it informs you.

import os
class Organize:
    def __init__(self,path,type):
        self.path=path
        self.type=type
        if os.path.exists(f"{self.path}"):
            pass
        else:
            print("Invalid path")
            exit()
    
    def group(self):
        files=os.listdir(f"{self.path}")
        i=0
        for file in files:
            if file.endswith(f".{self.type}") and (not os.path.exists(f"{self.path}/{self.type}")):
                os.mkdir(f"{self.path}/{self.type}")
                break
        for file in files:
            if os.path.exists(f"{self.path}/{self.type}") and file.endswith(f".{self.type}"):
                i=1
                try:
                    os.rename(f"{self.path}/{file}",f"{self.path}/{self.type}/{file}")
                except Exception as e:
                    print("File Already exists")

        if i==0:
            print(f"{self.type} files doesn't exists in {self.path}")


path=input("Enter the path where file exists --> ")
type=input("The type of the file --> ")
o1=Organize(path,type)
o1.group()
