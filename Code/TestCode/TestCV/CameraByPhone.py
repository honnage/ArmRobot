import cv2
import numpy as np
import requests

cap = cv2.VideoCapture('rtsp://192.168.144.193:8080/h264_pcm.sdp')

while True:
	_, frame = cap.read()
	cv2.imshow("frame", frame)
	cv2.waitKey(1)
