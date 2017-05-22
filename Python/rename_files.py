import os

def rename_files():
    # (1) Get the file names from a folder
    file_list = os.listdir("/Users/alexboley/Downloads/Prank")
    os.chdir("/Users/alexboley/Downloads/Prank")
    
    # (2) for each file, rename the file
    for file_name in file_list:
        os.rename(file_name, file_name.translate(str.maketrans('','','1234567890')))
        
rename_files()
