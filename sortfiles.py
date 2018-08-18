
# Adam Burke
# 29 May 2018
# sortfiles.py

# Import things that are needed
import string
import shutil
import os, sys


##############
#verify_file_exists(directory_name) ensures that the directory in which the user wants the photos
#to be moved to exists and that it will not overwrite an existing directory. It asks the user to
#confirm that they want to move the files to an existing directory with the same name.
##############
def verify_file_exists(directory_name):
    if os.path.isdir(directory_name) == False:     #Checks to see if directory exits
        print("Creating Directory " + directory_name)
        os.mkdir(directory_name)                   #If it doesn't exist -> create it
        if os.path.isdir(directory_name) == False: #verifies that it was created -> Else exit program
            print("File Creation Failed. Program Terminated")
            exit()
    else:
        print("The directory 'raw' already exists.")
                #If it does exist, confirm user wants to continue with the existing directory
        verify = str(input("Do you want to continue? (Yes/No)")).strip()
        if verify == "No" or verify == "no":
            print("Not Continueing")
            exit()
        elif verify == "Yes" or verify == "yes":
            print("Continueing")
        else:
            print("Invalid Input. Program Terminated")
            exit()
##############
#
##############
def move_files(directory_name, file_type):
    file_list = os.listdir()
    length_List = len(file_list)
    length_File_ex = len(file_type)
    print("\nMoving Files:")
    i=0
    while i < length_List:
        file = file_list[i]
        if(file[-length_File_ex:] == file_type):
            if os.path.isdir(directory_name) == False:
                print("ERROR. DIRECTORY DOES NOT EXIST")
                exit()
            print(file)
            shutil.move(file, directory_name)
        i = i+1
    print("\nFile move complete!")


def main():
    directory_name = str(input("Directory Name: ")).strip() #What the user wants the direcotry to be called where files are moved
    file_type = str(input("File Type (with dot): ")).strip()
    verify_file_exists(directory_name) #Verifies that the folder: raw exists
    move_files(directory_name, file_type)

main()

# print("moving file")
# print("move complete")

#Working Notes:
#Use this
#print(os.listdir())


