import RPi.GPIO as GPIO
import dht11
import time
import datetime
import requests
import cv2 as cv
import base64
import bujin
import duoji

channel_Light=16
GPIO.setup(channel_Light,GPIO.IN)

channel_huoyan=21
GPIO.setup(channel_huoyan,GPIO.IN)

channel_duqi=20
GPIO.setup(channel_duqi,GPIO.IN)

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance1 = dht11.DHT11(pin=18)


url='http://134.175.156.189:80/jpg'
cap=cv.VideoCapture(0)

try:
    while True:
        try:
            result = instance1.read()
            ret,frame=cap.read()
    #Light && huoyan && duqi
            Light=GPIO.input(channel_Light)
            huoyan=GPIO.input(channel_huoyan)
            duqi=GPIO.input(channel_duqi)
    #duoji
            r=requests.post('http://134.175.156.189:80/Getduoji')
            duoji.duoji(int(r.text))
            
    #wenshidu
            if result.is_valid():
                DataTime=str(datetime.datetime.now())
                Temperature=result.temperature
                Humidity=result.humidity
            #print(Temperature)
            #print(Humidity)           
            time.sleep(1)
            
            ret, jpeg = cv.imencode('.jpg', frame)
            r=requests.post(url,data={
                'jpg':base64.b64encode(jpeg.tobytes())
                })
            turn_flag=r.text
            
            
            r=requests.post('http://134.175.156.189:80/wendu',data={
                'wendu':Temperature
                })
    #        time.sleep(0.5)
            r=requests.post('http://134.175.156.189:80/shidu',data={
                'shidu':Humidity
                })
    #        time.sleep(0.5)
            r=requests.post('http://134.175.156.189:80/Light',data={
               'Light':Light
                })
    #        time.sleep(0.5)
            r=requests.post('http://134.175.156.189:80/huoyan',data={
               'huoyan':huoyan
                })
    #        time.sleep(0.5)
            r=requests.post('http://134.175.156.189:80/duqi',data={
               'duqi':duqi
                })
            #print(r.text)
            #1.4 r/du
            if(turn_flag=='左转'):
                bujin.backward(0.005,85)
            elif(turn_flag=='右转'):
                bujin.forward(0.005,85)
        except:
            print('error')
except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()



