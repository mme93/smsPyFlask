import sys
import time

import serial
from serial import Serial


def isReady(ser):
    if not ser.is_open:
        ser.open()
        print("Status: ", ser.is_open)
    return ser.is_open

def sendPin(ser):
    ser.write(b'AT\r')
    time.sleep(1)
    myline = ser.readline()
    while myline:
        print(myline)
        myline = ser.readline()
    """
    ser.write(b'AT+CPIN?\r')
    time.sleep(1)
    myline = ser.readline()
    while myline:
        print(myline)
        myline = ser.readline()
    """
    ser.write(b'AT+CPIN=5511\r')
    time.sleep(1)
    myline = ser.readline()
    while myline:
        print(myline)
        myline = ser.readline()

    ser.write(b'AT+CREG?\r')
    time.sleep(1)
    myline = ser.readline()
    while myline:
        print(myline)
        myline = ser.readline()

    ser.write(b'AT+CMGF=1\r')
    time.sleep(1)
    myline = ser.readline()
    while myline:
        print(myline)
        myline = ser.readline()

    ser.write(b'AT+CMGS="+4917684582550"\r')
    #ser.write(b'AT+CMGS="+4915734696774"\r')
    time.sleep(1)
    myline = ser.readline()
    while myline:
        print(myline)
        myline = ser.readline()

    ser.write(b'Ich bin ein Text\r')
    # ser.write(b'AT+CMGS="+4915734696774"\r')
    time.sleep(1)
    myline = ser.readline()
    while myline:
        print(myline)
        myline = ser.readline()

    ser.write(chr(26))
    time.sleep(1)
    myline = ser.readline()
    while myline:
        print(myline)
        myline = ser.readline()
    #+4915734696774


ser = serial.Serial()
ser.baudrate = 115200
ser.timeout = 5
ser.port = "/dev/ttyS0"

if not isReady(ser):
    print("Serial is not open")
    sys.exit(0)

print("Serial is open")
sendPin(ser)