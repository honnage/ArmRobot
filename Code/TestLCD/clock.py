
import drivers
from time import sleep
from datetime import datetime


display = drivers.Lcd()

try:
    print("Writing to display")
    display.lcd_display_string("No time to waste", 1)  
    while True:
        
        display.lcd_display_string(str(datetime.now().time()), 2)
        # Uncomment the following line to loop with 1 sec delay
        # sleep(1)
except KeyboardInterrupt:

    print("Cleaning up!")
    display.lcd_clear()
