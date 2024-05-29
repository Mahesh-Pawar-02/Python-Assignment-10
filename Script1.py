import os
import sys

def rename_files(directory, old_extension, new_extension):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        # Check if the file has the old extension
        if filename.endswith(old_extension):
            # Form the new filename
            new_filename = filename[:-len(old_extension)] + new_extension
            # Get full path of old and new files
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: '{old_file}' to '{new_file}'")
    
    print("Renaming completed.")

if __name__ == "__main__":
    # Check if the user provided the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python DirectoryRename.py <directory> <old_extension> <new_extension>")
        sys.exit(1)
    
    # Get arguments from the user
    directory = sys.argv[1]
    old_extension = sys.argv[2]
    new_extension = sys.argv[3]

    # Call the rename function
    rename_files(directory, old_extension, new_extension)
