from __future__ import division
from threading import Thread
import RPi.GPIO as GPIO
import time
import os
import drivers
import Ultrasonict as ult

display = drivers.Lcd()
#ultrasonict_camera = ultrasonict.Camera()
#ultrasonict_camera = ultrasonict.ArmRobot()

display.lcd_display_string("Hello World!", 1)  
display.lcd_display_string("This is project", 2)  
print("Hello World!")
print("This is project")
time.sleep(1)                                           
display.lcd_clear()


print("run file Ultrasonict.py")
# command = "python Ultrasonict.py" #command run demo_lcd.py for show message LCD
# os.system(command)

    
