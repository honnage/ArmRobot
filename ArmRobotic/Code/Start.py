from __future__ import division
from threading import Thread
import RPi.GPIO as GPIO
import time
import os
import sys
import drivers

#import FaceCV

print ("Run File Start.py")
display = drivers.Lcd()


while True:
    print("Writing to display")
    display.lcd_display_string("Start on", 1)  
    display.lcd_display_string("This is Project", 2)  
    time.sleep(0.5)                                           
    display.lcd_clear()

    display.lcd_display_string("Arm roboot", 1)   
    time.sleep(0.5)                                          
    display.lcd_clear()                           
         
    display.lcd_display_string("Open Camera", 1)   
    print ("run file Servo.py")
    command = "python Servo.py"
    time.sleep(0.5)                                          
    display.lcd_clear() 
    os.system(command)

    command = "aplay Sound_EndDetect.wav"
    os.system(command)
    print ("Sound on")





    
