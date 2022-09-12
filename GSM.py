import time

import serial

def send_sms(ser):
    ser.write(b'AT+CMGF=1\r')
    time.sleep(1)
    myline = ser.readline()
    while myline:
        print(myline)
        myline = ser.readline()
    ser.write(b'AT+CMGS="+4917684582550"\r')
    ser.write(chr(26))
    ser.write(b'Ich bin eine SMS\r')
    ser.write(chr(26))
    time.sleep(1)
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