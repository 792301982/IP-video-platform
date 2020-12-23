import RPi.GPIO as GPIO
import time
import requests
channel=20
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)


try:
    while True:
        print(GPIO.input(channel))
        if GPIO.input(channel)==0:
            print('do qi yi chang!!')
        else:
            print('yi qie zheng chang!!')
        time.sleep(1)
#        r=requests.post('http://134.175.156.189:80/Light',data={
#            'Light':GPIO.input(channel)
#            })
except KeyboardInterrupt:
    GPIO.cleanup()