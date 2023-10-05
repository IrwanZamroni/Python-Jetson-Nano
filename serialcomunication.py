import time
import serial
def initConnection (portNo, baudRate):
    try:
         ser = serial.Serial(portNo, baudRate)
         print ("Device Connected")
         return ser
    except:
         print ("Not Connected")

def senData(se, data, digits):
    myString = "$"
    for d in data :
        myString += str(d).zfill(digits)
        
    try:
        se.write(myString.encode())
        print(myString)
    except:
        print("data transmision failed")

if _name=="main_":
    ser = initConnection ("/dev/ttyACM0", 9600) 
    while True:
        senData(ser, [0,0,0],3)
        time.sleep(1)
        #senData(ser,[0,0],3)
        #time.sleep(1)