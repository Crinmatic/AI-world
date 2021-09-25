# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:40:13 2021

@author: King alagbe
"""
import cv2
import numpy as np

framewidth = 320
frameheight = 480
cap = cv2.VideoCapture(1)
cap.open(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10,150)
def empty(a):
    pass
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars" , 640,240)
cv2.createTrackbar("Hue Min", "TrackBars", 0,179,empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179,179,empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0,255,empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255,255,empty)
cv2.createTrackbar("Val Min", "TrackBars", 0,255,empty)
cv2.createTrackbar("Val Max", "TrackBars", 255,255,empty)

while True:
    success, img = cap.read()
    imgHSV =cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img,img,mask=mask)
    
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    horizstack = np.hstack([img, mask, result])
    
    cv2.imshow("Horizontal stacking", horizstack)
    cv2.imshow("Result", result)
    if cv2.waitKey(1) & 0xff == ord('q'):
       break
cap.release()
cv2.destroyAllWindows()