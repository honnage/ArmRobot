import cv2
import numpy as np
import dlib
import math

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,188)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        #cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        landmarks = predictor(gray, face)

        TOP_X = landmarks.part(62).x
        TOP_Y = landmarks.part(62).y
        BOTTOM_X = landmarks.part(66).x
        BOTTOM_Y = landmarks.part(66).y
        cv2.circle(frame, (TOP_X, TOP_Y), 2, (255,0,0), -1)
        cv2.circle(frame, (BOTTOM_X, BOTTOM_Y), 2, (0,0,255), -1)
        
        p1 = [TOP_X,TOP_Y]
        p2 = [BOTTOM_X,BOTTOM_Y]
        distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
        print(distance)
        
      

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
