import lcdlib
import time
import drivers

display = drivers.Lcd()
display.lcd_display_string("No time to wastedd ", 1)  

print("Cleaning up!")   
display.lcd_clear()
