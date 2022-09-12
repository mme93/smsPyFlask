# SMS-Service

# Docker

docker build -t smsservice:1.0 .      

docker run --publish=5000:5000 smsservice:1.0  

# Links

https://www.diafaan.com/sms-tutorials/gsm-modem-tutorial/at-cmgs-text-mode/

https://m2msupport.net/m2msupport/atcmgs-send-sms-message/

https://forum-raspberrypi.de/attachment/22327-sim7600e-h-4g-hat-manual-en-pdf/

https://www.waveshare.com/wiki/GSM/GPRS/GPS_Shield_(B)


#Minicom

minicom -D /dev/ttyS0

Strg+A danach Z

# AT Commands

AT
- Check Status

AT+CMEE=2
- Verbose Error Reporting

AT+CFUN=1,1
- Restart now
# AT PIN

AT+CPIN?
- Check SIM-Pin Status

AT+CPIN=5511
- PIN eingeben

# AT-COPS Network Registration

COPS Examples: https://m2msupport.net/m2msupport/atcops-plmn-selection/

AT+COPS=?
- List of supported responses

AT+COPS?
- Check Registration Status of SIM

AT+COPS=X,X,"XXXX",X
- Regestration to Network

# AT Send SMS

AT+CMGF=1
- Set to Text-Mode

AT+CMGS="+4917684582550"
'Ich bin ein Text'
-> STRG+Z
- Send a SMS Text
