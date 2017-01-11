#!/usr/bin/python

## import the serial library
import serial, sys, datetime
import time

## Boolean variable that will represent 
## whether or not the arduino is connected
connected = False

## establish connection to the serial port that your arduino 
## is connected to.

serial_file = sys.argv[1]

if not serial_file:
    raise "No file specified. " 

def connect(device):
    try:
        print("Trying...",device)
        return serial.Serial(device, 115200)
    except:
        print("Failed to connect on",device)

## loop until the arduino tells us it is ready
#while not connected:
#    serin = ser.read()
#    connected = True

#utcnow = str(datetime.datetime.utcnow())

#text_pth = "/root/data-collection/data-batch-%s.txt"%utcnow
#text_file = open(text_pth, 'w+')

#print("Test path: %s"%text_pth)

while True:
    try:
        ser = connect(serial_file)
        while True:
#            try:
                if ser.inWaiting():
                    sys.stdout.write(ser.read()) 
                    sys.stdout.flush()
#            except IOError as err:
#                print("Caught io exception, retrying connection")
#                print(err)
    except Exception as err:
        print("Caught exception, retrying")
        print(err)
        time.sleep(1)

## close the serial connection and text file
#text_file.close()
ser.close()


