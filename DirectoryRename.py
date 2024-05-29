# Problem Statement : Design automation script which accept directory name and two file extensions from user. Rename all files with 
# first file extension with the second file extenntion. 
# Usage : DirectoryRename.py “Demo” “.txt” “.doc” 


import os
import sys
import time

#  for filename in os.listdir(directory):
#         if filename.endswith(old_extension):
#             new_filename = filename[:-len(old_extension)] + new_extension
#             old_file = os.path.join(directory, filename)
#             new_file = os.path.join(directory, new_filename)
#             os.rename(old_file, new_file)

def DirectoryRename(DirName, Extention1,Extention2):
    flag = os.path.isabs(DirName)

    if (flag == False):
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)
    if(exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for name in filename:
                if name.endswith(Extention1):
                    NewFileName = filename[:-len(Extention1)] + Extention2
                    OldFile = os.path.join(DirName, filename)
                    NewFile = os.path.join(DirName,NewFileName)
                    os.rename(OldFile, NewFile)
    else:
        print("There is no such directory")

def main():
    print("---------------- Directory Rename -------------------")
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "-h" or sys.argv[1] == "-H"):
            print("This script is used for perform Directory file rename")
            exit()

        if(sys.argv[1] == "-u" or sys.argv[1] == "-U"):
            print("Usage of The script : ")
            print("DirectoryRename.py  Name_Of_Directory  Extention_Of_File Extention_Of_File")
            exit()
    
    if(len(sys.argv) == 3):
        try:
            starttime = time.time()
            DirectoryRename(sys.argv[1],sys.argv[2],sys.argv[3])
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