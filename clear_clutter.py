#This program helps tidy up your files by renaming them numerically within a specified path and file type. You input the path where the files are located and 
#specify the type of files you want to tidy. Then, the program renames those files numerically, starting from 1, while preserving their original file type. 
#If no files of that type are found, it informs you. Once completed, it confirms successful renaming.

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
