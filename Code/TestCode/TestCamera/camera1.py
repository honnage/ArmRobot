from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(0.5)
camera.capture('./myimg.jpg')
camera.stop_preview()
