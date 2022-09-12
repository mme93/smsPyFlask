from flask import Flask
import GSM

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/isReady')
def isSIMReady():
    ser = GSM.createSerial()
    if GSM.openSerialPort(ser):
        #GSM.setVerboseErrorRep(ser)
        #GSM.checkATStatus(ser)
        GSM.isCPIN(ser)
        GSM.setPIN(ser)
        GSM.isCPIN(ser)
        return 'Okay'
    else:
        return 'Can´t open Serial Port'


if __name__ == '__main__':
    app.run()
