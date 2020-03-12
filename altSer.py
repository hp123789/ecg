import os
from datetime import datetime
import serial
import time
from time import sleep
from threading import Thread
import io

def writeFile():
    now = datetime.now() #get current date and time
    date = now.strftime("%d-%m-%Y") #get date as string
    path = "C:/Users/hamza/Downloads/" + date #create directory in downloads with date as name
    ser = serial.Serial('COM3', 9600)
    t_end = time.time() + 5

    try:
        os.mkdir(path) #try to make the path
    except OSError:
        print("") #error message
    else:
        print("") #success message

    def create_file(): #create new txt file with time as name
        with open(now.strftime("%H;%M;%S")+".txt", "w") as file:
            file.write("")

    fileName = now.strftime("%H;%M;%S")+".txt" #get file name of txt file

    create_file() #create txt file

    filepath = os.path.join(path, fileName) #add txt file to directory that was created

    file1 = open(filepath, "w") #open txt file

    #toFile = input("Write what you want into the field") #input data
    while time.time() < t_end:
        readd = ser.readline().decode('ascii')
        #print(readd)
        file1.write(str(readd))

    file1.close() #close txt file

def altOne():
    while 1:
        writeFile()

def altTwo():
    sleep(2.5)
    altOne()


if __name__ == '__main__':
    Thread(target = altOne()).start()
    Thread(target = altTwo()).start()