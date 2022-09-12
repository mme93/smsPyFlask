from flask import Flask
import GSM

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/isReady')
def isSIMReady():
    ser = GSM.createSerial()
    print(ser.is_open)
    if GSM.openSerialPort(ser):
        print(ser.is_open)
        return 'Is Ready'
    else:
        return 'Can´t open Serial Port'


if __name__ == '__main__':
    app.run()
