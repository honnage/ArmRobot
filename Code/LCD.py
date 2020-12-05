import drivers
from time import sleep
import RPi.GPIO as GPIO
import os

display = drivers.Lcd()

# Main body of code
try:
    while True:
        # Remember that your sentences can only be 16 characters long!
		# print("Writing to display")
        display.lcd_display_string("Hello World!", 1)  
        display.lcd_display_string("This is project", 2)  
        sleep(1)                                           
        display.lcd_clear()
	display.lcd_display_string("Arm roboot", 1)   
        sleep(1)                                          
        display.lcd_clear()                                
        sleep(1)                                          
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
