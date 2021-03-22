import RPi.GPIO as GPIO
import time
import lcdlib
import drivers

# Ultrasonict Canera
TRIG_1 = 24 #Purple     
ECHO_1 = 23 #Yellow

# Ultrasonict Arm Robot
TRIG_2 = 27 #Blue
ECHO_2 = 22 #Green

GPIO.setmode(GPIO.BCM) # BCM is Number GPIO
GPIO.setwarnings(False)

lcd = lcdlib.lcd()

print("Run file Ultrasonict.py")

try:
        #Camera
        distance_Camera = 0
        sum_Camera = 0
        
        def Camera():
                print("distance measurement in progress 1 is Camera")
                sum_Camera = 0
                for i in range(5):
                        print "Ultrasonic 1 is Camera i = ",i+1
                        GPIO.setup(TRIG_1, GPIO.OUT)
                        GPIO.setup(ECHO_1, GPIO.IN)
                        GPIO.output(TRIG_1,False)
                        
                        time.sleep(0.2) # Origin is 0.2
                        GPIO.output(TRIG_1, True)
                        time.sleep(0.00001)
                        GPIO.output(TRIG_1, False)
                        
                        while GPIO.input(ECHO_1) == 0:
                            pulse_start = time.time()
                        while GPIO.input(ECHO_1) == 1:
                            pulse_end = time.time()
                            
                        pulse_duration = pulse_end-pulse_start
                        distance_Camera = pulse_duration*17000
                        distance_Camera = round(distance_Camera,2)
                
                        sum_Camera += distance_Camera 

                        print "Ultrasonic 1 is Camera distance:",distance_Camera,"cm"
                        print 'Ultrasonic 1 is Camera sum = ', sum_Camera  
                        print('')
                        
                        time.sleep(0.01)
                     
                # Outside the loop       
                print ("---------------")
                print "Ultrasonic 1 is Camera sum = ", sum_Camera
                print "Ultrasonic 1 is Camera num = ", i+1
                
                average_Camera = round( sum_Camera / (i + 1) , 2 )
               
                print "Ultrasonic 1 is average =", average_Camera
                print ("---------------")

                dist = str(average_Camera)
                lcd.lcd_display_string("Distance Camera",1)
                lcd.lcd_display_string(">>> "+dist+" cm",2)
                print "Ultrasonic 1 is Camera Distance is >>> "+dist+" cm"
                time.sleep(0.1)
                
                lcd.lcd_clear()
                print("\n \n")
                return average_Camera
        
        # ==============================================================
        
        #Arm
        distance_Arm = 0
        sum_Arm = 0
        
        def Arm():
                print("distance measurement in progress 2 is Arm")
                sum_Arm = 0
                for i in range(5):
                        #print "Ultrasonict 2 is i = ",i+1
                        GPIO.setup(TRIG_2, GPIO.OUT)
                        GPIO.setup(ECHO_2, GPIO.IN)
                        GPIO.output(TRIG_2,False)
                        
                        time.sleep(0.2) # Origin is 0.2
                        GPIO.output(TRIG_2, True)
                        time.sleep(0.00001)
                        GPIO.output(TRIG_2, False)
                        
                        while GPIO.input(ECHO_2) == 0:
                            pulse_start = time.time()
                        while GPIO.input(ECHO_2) == 1:
                            pulse_end = time.time()
                            
                        pulse_duration = pulse_end-pulse_start
                        distance_Arm = pulse_duration*17000
                        distance_Arm = round(distance_Arm,2)
                        
                
                        sum_Arm += distance_Arm 

                        print "Ultrasonict 2 is distance:",distance_Arm,"cm"
                        print 'Ultrasonict 2 is sum = ', sum_Arm 
                        print('')
                        
                        time.sleep(0.01)
                     
                # Outside the loop       
                print ("---------------")
                print "Ultrasonict 2 is sum = ", sum_Arm
                print "Ultrasonict 2 is num = ", i+1
                
                average_Arm = round( sum_Arm / (i + 1) , 2 )
               
                print "Ultrasonict 2 is average =", average_Arm
                #print ("---------------")

                dist = str(average_Arm)
                lcd.lcd_display_string("Distance Arm",1)
                lcd.lcd_display_string(">>> "+dist+" cm",2)
                #print "Ultrasonic 2 is Camera Distance is >>> "+dist+" cm"
                time.sleep(0.1)
                
                lcd.lcd_clear()
                print("\n \n")
                #return average_Arm
                
        # ==============================================================
                 
        def extra_arm():
                GPIO.setup(TRIG_2, GPIO.OUT)
                GPIO.setup(ECHO_2, GPIO.IN)
                GPIO.output(TRIG_2,False)
                        
                time.sleep(0.1) # Origin is 0.2
                GPIO.output(TRIG_2, True)
                time.sleep(0.00001)
                GPIO.output(TRIG_2, False)
                
                while GPIO.input(ECHO_2) == 0:
                    pulse_start = time.time()
                while GPIO.input(ECHO_2) == 1:
                    pulse_end = time.time()
                    
                pulse_duration = pulse_end-pulse_start
                distance_extra = pulse_duration*17000
                distance_extra = round(distance_extra,2)
                
                lcd.lcd_clear()
                return distance_extra
        
        def check_extra():
                a = extra_arm()
                print(a)
                while a<=2 or a>=500:
                        a = extra_arm()
                        print(a)
                return a
                        
                
        # ==============================================================
        
        #Arm()
        #Camera()
        #check_extra()

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Cleaning up!")
    lcd.lcd_clear()

