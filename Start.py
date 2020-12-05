from __future__ import division
from threading import Thread
import RPi.GPIO as GPIO
import time
import os
import drivers

print("Hello")
command = "python testtext.py" #command run testtext.py for show message
os.system(command)

print("run file demo_lcd.py")
command = "python demo_lcd.py" #command run demo_lcd.py for show message LCD
os.system(command)

    
