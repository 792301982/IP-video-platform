import RPi.GPIO as GPIO
import dht11
import time
import datetime
import requests
import cv2 as cv
import base64
import bujin
#import guangmin
#import duqi2.py
#

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=23)


url='http://134.175.156.189:80/jpg'
cap=cv.VideoCapture(0)

try:
    while True:
        result = instance.read()
        ret,frame=cap.read()
        if result.is_valid():
            DataTime=str(datetime.datetime.now())
            Temperature=result.temperature
            Humidity=result.humidity
        print(Temperature)
        print(Humidity)
        
        ret, jpeg = cv.imencode('.jpg', frame)
        r=requests.post(url,data={
            'jpg':base64.b64encode(jpeg.tobytes())
            })
        turn_flag=r.text
        
        r=requests.post('http://134.175.156.189:80/wendu',data={
            'wendu':Temperature
            })
        
        r=requests.post('http://134.175.156.189:80/shidu',data={
            'shidu':Humidity
            })
       # Light = guangmin.GPIO.input(channel)
        #r=requests.post('http://134.175.156.189:80/Light',data={
          #  'Light':GPIO.input(channel)
          #  })
        #print(r.text)
        #1.4 r/du
        if(turn_flag=='左转'):
            bujin.backward(0.005,85)
        elif(turn_flag=='右转'):
            bujin.forward(0.005,85)
except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
