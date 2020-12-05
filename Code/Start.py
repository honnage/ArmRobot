from __future__ import division
from threading import Thread
import RPi.GPIO as GPIO
import time
import os
import drivers

display = drivers.Lcd()

display.lcd_display_string("Hello World!", 1)  
display.lcd_display_string("This is project", 2)  
print("Hello World!")
print("This is project")
time.sleep(1)                                           
display.lcd_clear()


command = "python testtext.py" #command run testtext.py for show message
os.system(command)

print("run file Ultrasonict.py")
command = "python Ultrasonict.py" #command run demo_lcd.py for show message LCD
os.system(command)

    
