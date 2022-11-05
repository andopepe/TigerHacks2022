import cv2
import numpy as np

def findFace(img):
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)
cap = cv2.VideoCapture(0)


while True:
    _, img - cap.read()
    cvs.imshow("Output", img)
    cv2.waitKey(1)