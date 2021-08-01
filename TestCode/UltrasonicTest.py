import RPi.GPIO as GPIO
import time
import DisplayLCD  as dp
#import drivers

# Ultrasonict Canera
TRIG_1 = 18 #Purple     
ECHO_1 = 17 #Yellow

# Ultrasonict Arm Robot
TRIG_2 = 15 #Blue
ECHO_2 = 14 #Purple

GPIO.setmode(GPIO.BCM) # BCM is Number GPIO
GPIO.setwarnings(False)


print("Import file Ultrasonict.py")

try:
	#Camera
	distance_Camera = 0
	sum_Camera = 0
	
	def Camera():
			print("distance measurement in progress 1 is Camera")
			
			
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
			
			return distance_Camera
			
	def checkCamera():
			a = Camera()
			while a<1 or a> 150:
				a = Camera()
				print("loopCheckCamera =",a)
				time.sleep(1)
			print "check arm =",a
			
			return a
			
			
			
	def sumCamera():
		sum_Camera = 0
		for i in range(5):
			
			distance_Camera = checkCamera()
			sum_Camera += distance_Camera 

			print "Ultrasonic 1 is Camera distance:",distance_Camera,"cm"
			print 'Ultrasonic 1 is Camera sum = ', sum_Camera  
			print('')
			dp.distance_camera(distance_Camera)
			time.sleep(0.01)
			 
				
				 
		# Outside the loop       
		print ("---------------")
		print "Ultrasonic 1 is Camera sum = ", sum_Camera
		print "Ultrasonic 1 is Camera num = ", i+1
			
		average_Camera = round( sum_Camera / (i + 1) , 2 )
		   
		print "Ultrasonic 1 is average =", average_Camera
		print ("---------------")

		dist = str(average_Camera)
		print "Ultrasonic 1 is Camera Distance is >>> "+dist+" cm"
		time.sleep(0.1)
			
		print("\n \n")
		return average_Camera
	
   
	# ==============================================================        
	def Arm():
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
			
			dis = str(distance_extra)
			print("arm distance =",dis)
			dp.distance_arm(dis)
			#lcd.lcd_clear()
			#time.sleep(0.5)
			return distance_extra
			
	def checkArm():
			a = Arm()
			while a<1 or a> 150:
					a = Arm()
					print "loopCheckArm =",a
					time.sleep(1)
			print "check arm =",a
	# ==============================================================


	sumCamera()
	#Camera()
   
 
       
        
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Cleaning up!")
    #lcd.lcd_clear()

