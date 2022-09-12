from flask import Flask, request
import GSM

app = Flask(__name__)


@app.route('/SMS', methods=['Post'])
def send_sms():
    ser = GSM.createSerial()
    if GSM.openSerialPort(ser):
        GSM.send_sms(ser, request.json['phone'], request.json['msg'])
        ser.close()
    return 'SMS was sent'


@app.route('/init')
def initGSM():
    ser = GSM.createSerial()
    if GSM.openSerialPort(ser):
        GSM.setVerboseErrorRep(ser)
        GSM.setPIN(ser)
        ser.close()
        return 'Okay'
    else:
        ser.close()
        return 'Can´t open Serial Port and init GSM'

@app.route('/at/status')
def check_at_status():
    ser = GSM.createSerial()
    if GSM.openSerialPort(ser):
        GSM.checkATStatus(ser)
        ser.close()
        return 'Okay'
    else:
        ser.close()
        return 'Can´t open Serial Port'

@app.route('/isSIMReady')
def isSIMReady():
    ser = GSM.createSerial()
    if GSM.openSerialPort(ser):
        GSM.isCPIN(ser)
        ser.close()
        return 'Okay'
    else:
        ser.close()
        return 'Can´t open Serial Port'


# Need to get public Network
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
