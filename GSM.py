import time

import serial

recipient = "+4915734696774"
message = "Ich liebe mein Schatz!"

def send_sms(ser,phone, msg):
    ser.write(b'AT+CMGF=1\r')
    time.sleep(0.5)
    ser.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
    time.sleep(0.5)
    ser.write(message.encode() + b"\r")
    time.sleep(0.5)
    ser.write(bytes([26]))
    myline = ser.readline()
    while myline:
        print(myline)
        myline = ser.readline()


# Create a Serial Port for GSM-Module
def createSerial():
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.timeout = 5
    ser.port = "/dev/ttyS0"
    return ser


def openSerialPort(ser):
    if not ser.is_open:
        ser.open()
        print("Status: ", ser.is_open)
    return ser.is_open


# Check AT Status from GSM-Module
def checkATStatus(ser):
    ser.write(b'AT\r')
    time.sleep(1)
    myline = ser.readline()
    while myline:
        print(myline)
        myline = ser.readline()


# Set Verbose Error Reporting
def setVerboseErrorRep(ser):
    ser.write(b'AT+CMEE=2\r')
    time.sleep(1)
    myline = ser.readline()
    while myline:
        print(myline)
        myline = ser.readline()


# Check is PIN activated
def isCPIN(ser):
    ser.write(b'AT+CPIN?\r')
    time.sleep(1)
    myline = ser.readline()
    while myline:
        print(myline)
        myline = ser.readline()

def setPIN(ser):
    ser.write(b'AT+CPIN=5511\r')
    time.sleep(1)
    myline = ser.readline()
    while myline:
        print(myline)
        myline = ser.readline()