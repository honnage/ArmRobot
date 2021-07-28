import RPi.GPIO as GPIO
import time
import os
import drivers
display = drivers.Lcd()
display.lcd_clear()
print(GPIO.VERSION)
	
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# --- Set GPIO ---
LED_Green = 27 #Green
LED_Yello = 22 #Yello

OnClick_ButtonGreen = 23 #Orange
OnClick_ButtonRed = 24 #Yello
Onclick_ButtonEmergent = 4 #Broen 

GPIO.setup(LED_Green, GPIO.OUT)
GPIO.setup(LED_Yello, GPIO.OUT)


GPIO.setup(OnClick_ButtonGreen, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(OnClick_ButtonRed, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Onclick_ButtonEmergent, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

statusWorking_LEDGreen = 0
statusWorking_LEDYello = 0

statusButton_Green = 0
statusButton_Red = 0
statusButton_Emergent = 0


while 1:
	GPIO.output(LED_Green, True)
	time.sleep(1)
	GPIO.output(LED_Green, False)
	time.sleep(1)
	
	if GPIO.input(OnClick_ButtonGreen) == 1:
		print("OnClick_ButtonGreen")
		print("Function: DisplayShow_ready")
		display.lcd_display_string(">>iFeedingBot<<", 1)
		display.lcd_display_string("READY TO USE.", 2)
		print ("Sound on")
		command = "aplay Sound_EndDetect.wav"
		os.system(command)
		command = "python StartProject.py"
		os.system(command)
		
	#onClick Button Emergent: ON 
	if GPIO.input(Onclick_ButtonEmergent) == 0:
		statusWorking_LEDGreen = 0
		statusWorking_LEDYello = 1
		statusButton_Green = 0
		statusButton_Red = 0
		statusButton_Emergent = 1
				
		GPIO.output(LED_Green, GPIO.LOW)
		GPIO.output(LED_Yello, GPIO.LOW)
		if statusButton_Emergent == 1:
			GPIO.output(LED_Yello, GPIO.HIGH)
			print("\Yello LED Working... ON")
			time.sleep(0.1)
											
			GPIO.output(LED_Yello, GPIO.LOW)
			print("Yello LED Working... OFF")
			time.sleep(0.1)
	# ==========================================================
	if statusButton_Emergent == 1 and statusWorking_LEDYello == 1:
		pass
	# ==========================================================
	if GPIO.input(OnClick_ButtonGreen) == 1 and  statusButton_Emergent == 1:
		pass	
	# ==========================================================
					
	#onClick Button Emergent: OFF	
	if GPIO.input(Onclick_ButtonEmergent) == 1 and  statusButton_Emergent == 1:
		statusWorking_LEDGreen = 0
		statusWorking_LEDYello = 0
		statusButton_Green = 0
		statusButton_Red = 0
		statusButton_Emergent = 0
		GPIO.output(LED_Green, GPIO.LOW)
		GPIO.output(LED_Yello, GPIO.LOW)
				
		print("\nOnClick Button Emergent: OFF\n")
		print("="*30)

GPIO.cleanup
