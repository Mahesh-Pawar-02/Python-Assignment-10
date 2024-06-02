# Problem Statement : Design automation script which accept directory name and two file extensions from user. Rename all files with 
# first file extension with the second file extenntion. 
# Usage : DirectoryRename.py "Test" ".c" ".doc"
# Demo is name of directory and .txt is the extension that we want to search and rename with .doc. 
# After execution this script each .txt file gets renamed as .doc. 

import os
import sys
import time

def DirectoryRename(DirName, Extention1, Extension2):
    flag = os.path.isabs(DirName)

    if (flag == False):
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    if(exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for name in filename:
                if name.endswith(Extention1):
                    NewFileName = name.replace(Extention1,Extension2, 1)
                    OldFile = os.path.join(DirName, name)
                    NewFile = os.path.join(DirName,NewFileName)
                    os.rename(OldFile,NewFile)
                    print("Renamed successfully to "+os.path.basename(OldFile) + " with "+os.path.basename(NewFile))    
    else:
        print("There is no such directory")

def main():
    print("\n---------------- Directory File Rename -------------------\n")
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "-h" or sys.argv[1] == "-H"):
            print("This script is used for perform Directory file rename")
            exit()

        if(sys.argv[1] == "-u" or sys.argv[1] == "-U"):
            print("Usage of The script : ")
            print("DirectoryFileSearch.py  Name_Of_Directory  Extention_Of_File Extention_Of_File")
            exit()
    
    if(len(sys.argv) == 4):
        try:
            starttime = time.time()
            DirectoryRename(sys.argv[1],sys.argv[2],sys.argv[3])
            endtime = time.time()

            print("\nTime required to execute the script is : ",endtime-starttime,"\n")

        except Exception as obj2:
            print("Unable to perform the task due to ", obj2)
            
    else:
        print("Invalid option")
        print("Use --h option to get the help and use --u option to get the usage of application")
        exit()
    
    print("--------- Thank you for using our script -------------")
    print("------------- Created by Mahesh Pawar ----------------")

if __name__ == "__main__":
    main()

# Test Case :

# python DirectoryRename.py Test .c .py

# ---------------- Directory File Rename -------------------

# Renamed successfully to Program1.pdf with Program1.c
# Renamed successfully to Program2.pdf with Program2.c
# Renamed successfully to Program3.pdf with Program3.c
# Renamed successfully to Program4.pdf with Program4.c
# Renamed successfully to Program5.pdf with Program5.c

# Time required to execute the script is :  0.006002902984619141

# --------- Thank you for using our script -------------
# ------------- Created by Mahesh Pawar ----------------