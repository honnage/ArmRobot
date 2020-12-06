from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180

#camera.start_preview()
camera.resolution = (640, 480)

for i in range(5):
	sleep(0.7)
	camera.capture('./myimg%s.jpg' % i)
