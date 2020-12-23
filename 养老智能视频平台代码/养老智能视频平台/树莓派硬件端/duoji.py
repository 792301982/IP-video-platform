'''import RPi.GPIO as GPIO
import time
import signal
import atexit
 
atexit.register(GPIO.cleanup)  
 
servopin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT, initial=False)
p = GPIO.PWM(servopin,50) #50HZ
p.start(0)
time.sleep(2)
 
while(True):
  for i in range(0,181,1):
    p.ChangeDutyCycle(2.5 + 10 * i / 180) #设置转动角度
    time.sleep(0.02)                      #等该20ms周期结束
    p.ChangeDutyCycle(0)                  #归零信号
    time.sleep(0.2)
  
  for i in range(180,-1,-1):
    p.ChangeDutyCycle(2.5 + 10 * i / 180)
    time.sleep(0.02)
    p.ChangeDutyCycle(0)
    time.sleep(0.2)
'''

import sys
import RPi.GPIO as GPIO
import time

#mid :115du  70du

GPIO.setwarnings(False)
def duoji(i):
    if(i>170 or i<1):
        return
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.0001*float(i/180*20+5))#5--25
    GPIO.output(26, GPIO.LOW)
'''for i in range(1,181,10):
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(18, GPIO.OUT)
  GPIO.output(18, GPIO.HIGH)
  time.sleep(0.0001*float(i/180*20+5))#5--25
  GPIO.output(18, GPIO.LOW)
  GPIO.cleanup()
  #print(i)
  time.sleep(1)'''
if __name__ == "__main__":
    for i in range(1,170,10):
        duoji(i)
        print(i)
        time.sleep(1)
