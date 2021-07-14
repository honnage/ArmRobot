from __future__ import division
from threading import Thread
import RPi.GPIO as GPIO
import multiprocessing as mp
import math 
import time
import os
#import drivers
print("Start Project ....")
import Ultrasonict
 
isWorking = False

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def runfile_test():
	command = "python runfile_test.py"
	os.system(command)
	print("Run file runfile_test.py ")
	global isWorking 
	isWorking = False
	return isWorking
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GPIO.cleanup()


print("Opening Camera ...")
while True:

	if isWorking == False :
		
		isWorking = True
		print "Run servo armrobot"
		Thread(target=runfile_test).start()
					
	else:
		print "Distance mouth :"
			
		'''
		show message "IS WORK ARM ROBOT ..."
		#else:
		    # print "IS WORKING ARM ROBOT ..."
		'''



	if key == 27:
	    break


