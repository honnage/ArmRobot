import dlib 
import cv2 
import math 

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
cap = cv2.VideoCapture(0) 
cap.set(3,320) 
cap.set(4,188) 
while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = detector(gray)
	for face in faces:
		x1 = face.left()
		y1 = face.top()
		x2 = face.right()
		y2 = face.bottom()
		landmarks = predictor(gray, face)
		
		xTOP = landmarks.part(62).x 
		yTOP = landmarks.part(62).y 
		xBOTTOM = landmarks.part(66).x 
		yBOTTOM = landmarks.part(66).y 
		cv2.circle(frame, (xTOP, yTOP),2,(0,255,0),-1)
		cv2.circle(frame, (xBOTTOM,yBOTTOM),2,(255,0,0),-1)
		p1 = [xTOP,yTOP] 
		p2 = [xBOTTOM,yBOTTOM] 
		distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) ) 
	
		print(distance)
		if distance >= 20 : 
			print("IFeedingBOT is Working !!!") 
		
		cv2.imshow("Ifeedingbot", frame)
