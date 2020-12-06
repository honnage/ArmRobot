import RPi.GPIO as GPIO
import time

BaseServoPIN = 17
ArmDownPIN = 18
ArmUpPIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup(BaseServoPIN, GPIO.OUT)
GPIO.setup(ArmDownPIN, GPIO.OUT)
GPIO.setup(ArmUpPIN, GPIO.OUT)

p0 = GPIO.PWM(BaseServoPIN, 50) # GPIO 17 for PWM with 50Hz
p1 = GPIO.PWM(ArmDownPIN, 50) # GPIO 18 for PWM with 50Hz
p2 = GPIO.PWM(ArmUpPIN, 50)

p0.start(0) # Base
p1.start(0) # ArmDown
p2.start(0) # ArmUp

try:
   while True: 
      p1.ChangeDutyCycle(8)
      time.sleep(0.25)
      
      p1.ChangeDutyCycle(9)
      time.sleep(0.25)
      
      p1.ChangeDutyCycle(10)
      time.sleep(0.25)
      
      p1.ChangeDutyCycle(11)
      time.sleep(0.25)
      
      p1.ChangeDutyCycle(12)
      time.sleep(0.25)
      
      p1.ChangeDutyCycle(11)
      time.sleep(0.25)
      
      p1.ChangeDutyCycle(10)
      time.sleep(0.25)
      
      p1.ChangeDutyCycle(9)
      time.sleep(0.25)

   # p0.ChangeDutyCycle(1) # 0 degree
   # p1.ChangeDutyCycle(1)
   # print("degree 0")
   # time.sleep(1)
    
   # p0.ChangeDutyCycle(8) # 90 degree
   # p1.ChangeDutyCycle(8)
   # print("degree 90")
   # time.sleep(1)
    
   # p0.ChangeDutyCycle(13) # 180 degree
   # p1.ChangeDutyCycle(13)
   # print("degree 180")
   # time.sleep(1)
    
   # p0.ChangeDutyCycle(8) # 90 degree
   # p1.ChangeDutyCycle(8)
   # print("degree 90")
   # time.sleep(1)
    
   
except KeyboardInterrupt:
  p0.stop()
  p1.stop()
  p2.stop()
  GPIO.cleanup()
