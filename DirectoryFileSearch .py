# Problem Statement : Design automation script which accept directory name and file extension from user. Display all files with that extension. 
# Usage : DirectoryFileSearch.py “Demo” “.txt” 

import os
import sys
import time

def DirectoryFileSearch(DirName, Extention):
    flag = os.path.isabs(DirName)

    if (flag == False):
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)
    if(exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for name in filename:
                if name.endswith(Extention):
                    print(name)
    else:
        print("There is no such directory")

def main():
    print("---------------- Directory Saerch -------------------")
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "-h" or sys.argv[1] == "-H"):
            print("This script is used for perform Directory file Search")
            exit()

        if(sys.argv[1] == "-u" or sys.argv[1] == "-U"):
            print("Usage of The script : ")
            print("DirectoryFileSearch.py  Name_Of_Directory  Extention_Of_File")
            exit()
    
    if(len(sys.argv) == 3):
        try:
            starttime = time.time()
            DirectoryFileSearch(sys.argv[1],sys.argv[2])
            endtime = time.time()

            print("Time required to execute the script is : ",endtime-starttime)

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