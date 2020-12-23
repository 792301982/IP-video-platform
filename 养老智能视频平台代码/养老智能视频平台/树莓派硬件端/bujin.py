
#!/usr/bin/env python
#########################################################
import RPi.GPIO as GPIO
import time
 
IN1 = 4
IN2 = 17
IN3 = 27
IN4 = 22
 
def setStep(w1, w2, w3, w4):
    GPIO.output(IN1, w1)
    GPIO.output(IN2, w2)
    GPIO.output(IN3, w3)
    GPIO.output(IN4, w4)
 
def stop():
    setStep(0, 0, 0, 0)
 
def forward(delay, steps):  
    for i in range(0, steps):
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)
 
def backward(delay, steps):  
    for i in range(0, steps):
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(1, 0, 0, 0)
        time.sleep(delay)
 
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
    GPIO.setup(IN1, GPIO.OUT)      # Set pin's mode is output
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
 
def loop():
    while True:
        print ("backward...")
        backward(0.005, 512)  # 512 steps --- 360 angle
        print ("forward...")
        forward(0.005, 512)

 
def destroy():
    GPIO.cleanup()             # Release resource
    
setup()

if __name__ == '__main__':     # Program start from here
    
    '''while(1):
        time.sleep(1)
        if(str(GPIO.input(7))=='1'):
            forward(0.005,10)
        else:
            backward(0.005,10)'''
    while(1):
        forward(0.005,256)
        backward(0.005,256)
                

