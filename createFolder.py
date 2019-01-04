import os, shutil, sys

# Path of base directory 
from_path = ""
# Path of new directory
to_path = "" + sys.argv[1]
# Used for renaming the files in new directory
placeholder = "placeholder"

# Get all files from base directory
files = os.listdir(from_path)

# Create new directory, if directory doesn't exist
if os.path.isdir(to_path):
    print("%s exists" % to_path)
    exit()

try:  
    os.mkdir(to_path)
except OSError:  
    print ("Creation of the directory %s failed" % to_path)
else:  
    print ("Successfully created the directory %s " % to_path)

# Copy all files from base directory to new directory 
for file in files:
    shutil.copy(from_path + "/" + file, to_path)

print("Succesfully copied files into new directory")

# Rename files in new directory
for file in os.listdir(to_path):
        os.rename(to_path + "/" + file, to_path + "/" + file.replace(placeholder, sys.argv[1]))

print("Succesfully renamed files in new directory")