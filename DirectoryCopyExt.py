
# Problem Statement : Design automation script which accept two directory names and one file extension. Copy all files with the 
# specified extension from first directory into second directory. Second directory should be created at run time. 

# Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy 
# all files with extension .exe from Demo to Temp. 

import os
import shutil
import sys
import time

def DirectoryCopyExt(source_dir, dest_dir, file_extension):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(file_extension):
                source_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, file)
                shutil.copy2(source_file_path, dest_file_path)  

def main():
    print("\n---------------- Directory File Copy -------------------\n")
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "-h" or sys.argv[1] == "-H"):
            print("This script is used for perform Directory file Copy")
            exit()

        if(sys.argv[1] == "-u" or sys.argv[1] == "-U"):
            print("Usage of The script : ")
            print("DirectoryCopyExt.py  First_Directory  Second_Directory Extention_Of_File")
            exit()
    
    if(len(sys.argv) == 4):
        try:
            starttime = time.time()
            DirectoryCopyExt(sys.argv[1],sys.argv[2],sys.argv[3])
            print("Files with extension copied successfully")
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

# ---------------- Directory File Copy -------------------

# Files with extension copied successfully

# Time required to execute the script is :  0.00600743293762207

# --------- Thank you for using our script -------------
# ------------- Created by Mahesh Pawar ----------------