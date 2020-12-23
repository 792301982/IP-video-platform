# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:29:15 2019
"""

import RPi.GPIO as GPIO 
import time
    
CHANNEL=21

GPIO.setmode(GPIO.BCM)    
GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def action(pin):    
    print('you du!')

GPIO.add_event_detect(CHANNEL, GPIO.RISING) 
GPIO.add_event_callback(CHANNEL, action)

try:    
    while True: 
        print('yi qie zheng chang')
        time.sleep(0.5) 
        
except KeyboardInterrupt:   
    GPIO.cleanup()