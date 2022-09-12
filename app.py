from flask import Flask, request, jsonify
import GSM

app = Flask(__name__)


@app.route('/test', methods=['Post'])
def test():
    phoneNumber = request.json['phone']
    msg = request.json['msg']
    return request.json['mytext'];


@app.route('/SMS', methods=['Post'])
def send_sms():
    ser = GSM.createSerial()
    if GSM.openSerialPort(ser):
        GSM.test_sms(ser, request.json['phone'], request.json['msg'])
        #GSM.send_sms(ser)
        ser.close()
    return 'Hello World!'


@app.route('/isReady')
def isSIMReady():
    ser = GSM.createSerial()
    if GSM.openSerialPort(ser):
        # GSM.setVerboseErrorRep(ser)
        # GSM.checkATStatus(ser)
        # GSM.isCPIN(ser)
        # GSM.setPIN(ser)
        GSM.isCPIN(ser)
        ser.close()
        return 'Okay'
    else:
        ser.close()
        return 'Can´t open Serial Port'


if __name__ == '__main__':
    app.run()
