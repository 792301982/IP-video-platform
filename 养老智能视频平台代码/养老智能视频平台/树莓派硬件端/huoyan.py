import RPi.GPIO as GPIO
import time
import requests
channel=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)


try:
    while True:
        print(GPIO.input(channel))
        if GPIO.input(channel)==0:
            print('fashenghuozai!!')
        else:
            print('zhengchang!!')
        time.sleep(1)
#        r=requests.post('http://134.175.156.189:80/Light',data={
#            'Light':GPIO.input(channel)
#            })
except KeyboardInterrupt:
    GPIO.cleanup()