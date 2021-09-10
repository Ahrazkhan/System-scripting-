# Make folders/files
import os
# helps in automating process of copying and removal of files and directories
import shutil


# Define function that accept one parameter and creating folders, files, subfolders.
def create(name: str):
    if not os.path.exists(name):  # checking directory already created or not
        print(f"Directory  {name} Created ")
        os.mkdir(name)
    else:
        print(f"Directory {folder_name}  already exists")
        shutil.rmtree(folder_name)
        print(f'Removing {folder_name} Directory')
        os.mkdir(folder_name)
        print(f"Directory  {folder_name} Created ")
    os.mkdir(f'{name}/working')
    os.mkdir(f'{name}/backup')
    os.mkdir(f'{name}/working/pics')
    os.mkdir(f'{name}/working/docs')
    os.mkdir(f'{name}/working/movie')
    os.mkdir(f'{name}/working/docs/school')
    os.mkdir(f'{name}/working/docs/party')
    coronavirus = open(f'{name}/working/docs/CORONAVIRUS.txt', 'w')
    coronavirus.write('This document is about CORONAVIRUS')  # adding some text in file
    coronavirus.close()
    dangerous = open(f'{name}/working/docs/DANGEROUS.txt', 'w')
    dangerous.write('This document is about DANGEROUS')
    dangerous.close()
    keepsafe = open(f'{name}/working/docs/KEEPSAFE.txt', 'w')
    keepsafe.write('This document is about KEEPSAFE')
    stayhome = open(f'{name}/working/docs/STAYHOME.txt', 'w')
    stayhome.write('This document is about STAYHOME')
    stayhome.close()
    hygiene = open(f'{name}/working/docs/HYGIENE.txt', 'w')
    hygiene.write('This document is about HYGIENE')
    hygiene.close()


# Request for inputs what will be name of folder
folder_name = input('Please enter folder name: ')
# Run the function to create folders/files
create(folder_name)


# Define function that accepts one parameter which renames files lower to upper
def rename(path: str):
    for filename in os.listdir(path):
        file_path = path + f'/{filename}'
        os.rename(file_path, file_path.lower())
        if '.txt' in filename:  # .txt should be renamed to uppercase.
            os.rename(file_path, file_path.upper())


#  Ensure that the folder exist
try:
    rename(f'{folder_name}/working/docs')
except FileNotFoundError:
    print("the folder doesn't exists")


# Define a function which archives zip files for backup.
def make_archive():
    for i in range(5):
        shutil.make_archive(f'{folder_name}/backup/{i}-backup', 'zip', 'abc/working/docs')
        print(f'Archived {i}-backup.zip file')


# Run the function to make backup.
make_archive()
