import os
from datetime import datetime

now = datetime.now() #get current date and time
date = now.strftime("%d-%m-%Y") #get date as string
path = "C:/Users/hamza/Downloads/" + date #create directory in downloads with date as name

try:
    os.mkdir(path) #try to make the path
except OSError:
    print("Path could not be created or path already exists.") #error message
else:
    print("Path successfully created.") #success message

def create_file(): #create new txt file with time as name
    with open(now.strftime("%H;%M;%S")+".txt", "w") as file:
        file.write("")

fileName = now.strftime("%H;%M;%S")+".txt" #get file name of txt file

create_file() #create txt file

filepath = os.path.join(path, fileName) #add txt file to directory that was created

file1 = open(filepath, "w") #open txt file

toFile = input("Write what you want into the field") #input data

file1.write(toFile) #write to txt file

file1.close() #close txt file