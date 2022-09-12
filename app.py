from flask import Flask
import GSM

app = Flask(__name__)

@app.route('/test/<name>')
def test(name):
    print(name)
    return name

@app.route('/SMS')
def send_sms():  # put application's code here
    ser = GSM.createSerial()
    if GSM.openSerialPort(ser):
        GSM.send_sms(ser)
        ser.close()
    return 'Hello World!'


@app.route('/isReady')
def isSIMReady():
    ser = GSM.createSerial()
    if GSM.openSerialPort(ser):
        #GSM.setVerboseErrorRep(ser)
        #GSM.checkATStatus(ser)
        #GSM.isCPIN(ser)
        #GSM.setPIN(ser)
        GSM.isCPIN(ser)
        ser.close()
        return 'Okay'
    else:
        ser.close()
        return 'Can´t open Serial Port'


if __name__ == '__main__':
    app.run()
