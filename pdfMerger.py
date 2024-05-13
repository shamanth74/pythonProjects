#This code helps to merge pdfs in a particular folder and can store pdfs in user specified path
#the order to merge is as the name of the files in an alphabetical order


import PyPDF2
import os


class Operations:
    def __init__(self,path):
        self.path=path
        if not os.path.exists(self.path):
            print("Specified path doesn't exists")
            exit()
        files=os.listdir(self.path)
        i=0
        global pdf
        pdf=[]
        for file in files:
            if file.endswith(".pdf"):
                pdf.append(file)
                i=i+1
        if i<2:
            print("Path entered contains no pdf files or Less than 2 files")
            exit()
        else:
            print(f"\nMerging {pdf} files......\n")


    def merge_pdfs(self,input_dir, output_dir):
        merger = PyPDF2.PdfMerger()
        [merger.append(pdf) for pdf in [open(os.path.join(input_dir, file), 'rb') for file in os.listdir(input_dir) if file.endswith('.pdf')]]
        exist=os.listdir(output_dir)
        for exists in exist:
            if exists=="merged.pdf":
                print("\nFile named Merged.pdf already exists\nGive another path to store and Try again\n")
                exit()

        merger.write(os.path.join(output_dir, 'merged.pdf'))
        merger.close()


path_i=(input("Enter path where pdf file lies --> "))
m=Operations(path_i)

path_d=(input("Enter path where Merged pdf file to be stored --> "))
m.merge_pdfs(f"{path_i}",f"{path_d}")

print(f"\nMerged file stored in {path_d}")
