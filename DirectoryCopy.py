# Problem Statement : Design automation script which accept two directory names. Copy all files from first directory into second
# directory. Second directory should be created at run time. 

# Usage : DirectoryCopy.py Test Temp 

# Demo is name of directory which is existing and contains files in it. 
# We have to create new Directory as Temp and copy all files from Demo to Temp. 

import os
import shutil
import time
import sys

def DirectoryCopy(SrcDir, DestDir):
    if not os.path.exists(SrcDir):
        print("Source directory "+SrcDir+ "does not exist.")
        return
    
    if not os.path.exists(DestDir):
        os.makedirs(DestDir)
        print("Destination directory " + DestDir+ " created.\n")
    else:
        print("Destination directory "+ DestDir + " already exists.\n")
    
    Files = os.listdir(SrcDir)
    
    for File in Files:
        SrcPath = os.path.join(SrcDir, File)
        DestPath = os.path.join(DestDir, File)
        shutil.copy(SrcPath, DestPath)
        print("Copying "+ File+ "to"+ DestDir)

def main():
    print("\n---------------- Directory Copy -------------------\n")
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "-h" or sys.argv[1] == "-H"):
            print("This script is used for perform Directory file Copy")
            exit()

        if(sys.argv[1] == "-u" or sys.argv[1] == "-U"):
            print("Usage of The script : ")
            print("DirectoryFileSearch.py  First_Directory  Second_Directoy")
            exit()
    
    if(len(sys.argv) == 3):
        try:
            starttime = time.time()
            DirectoryCopy(sys.argv[1],sys.argv[2])
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

# ---------------- Directory Copy -------------------

# Destination directory Temp created.

# Copying Program1.pytoTemp
# Copying Program2.pytoTemp
# Copying Program3.pytoTemp
# Copying Program4.pytoTemp
# Copying Program5.pytoTemp

# Time required to execute the script is :  0.00700068473815918

# --------- Thank you for using our script -------------
# ------------- Created by Mahesh Pawar ----------------