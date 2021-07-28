import RPi.GPIO as GPIO
import drivers
import time

display = drivers.Lcd()
display.lcd_clear()

def ready():
	display.lcd_clear()
	print("Function: DisplayShow_ready")
	display.lcd_display_string(">>iFeedingBot<<", 1)
	display.lcd_display_string("READY TO USE.", 2)
	
def onClickButtonGreen():
	display.lcd_clear()
	print("Function: ready")
	display.lcd_display_string(">>iFeedingBot<<", 1)
	display.lcd_display_string("START PROCESS", 2)
	
def onClickButtonRed():
	display.lcd_clear()
	print("Function: onClickRuutonRed")
	display.lcd_display_string(">>iFeedingBot<<", 1)
	display.lcd_display_string("CLOSE PROCESS", 2)

def onClickButtonEmergency_on():
	display.lcd_clear()
	print("Function: onClickButtonEmergency_on")
	display.lcd_display_string(">>iFeedingBot<<", 1)
	display.lcd_display_string("EMERGENCY STOP", 2)

def distance_camera(distance):
	display.lcd_clear()
	distance = str(distance)
	print("Function: distance_camera")
	display.lcd_display_string("CAMERA DISTANCE", 1)
	display.lcd_display_string(">>> "+distance+" cm", 2)

def distance_arm(distance):
	display.lcd_clear()
	distance = str(distance)
	print("Function: distance_arm")
	display.lcd_display_string("ARM DISTANCE", 1)
	display.lcd_display_string(">>> "+distance+" cm", 2)

def servoWorking():
	display.lcd_clear()
	print("Function: servoWorking")
	display.lcd_display_string("WORKING ...", 1)
	display.lcd_display_string("SERVO MOTOR", 2)
	
