# list of files in each folder  using module
# using for for loop process file
# handle exceptions 
import os
folders = input("enter folder names separated by space\t").split()

try:
    for folder in folders:
        fol=os.listdir(folder)
        print("files present in folder", folder)
        for file in fol:
            print(file)
except FileNotFoundError:
    print ("provide valide folder names")
