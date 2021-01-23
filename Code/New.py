import Ultrasonict

#Ultrasonict.Camera()

while True:
	c = Ultrasonict.check_extra()
	print("Arm",c)
	time.sleep(0.2)

#print("Camera",b)
