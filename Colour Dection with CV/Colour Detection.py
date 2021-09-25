
"""
Created on Wed May 12 23:00:01 2021

@author: King alagbe
"""

import cv2
import numpy as np
def empty(a):
    pass
path = r"C:\Users\King alagbe\Downloads\teslacar3.jpg"

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars" , 640,240)
cv2.createTrackbar("Hue Min", "TrackBars", 89,179,empty)
cv2.createTrackbar("Hue Max", "TrackBars", 152,179,empty)
cv2.createTrackbar("Sat Min", "TrackBars", 51,255,empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255,255,empty)
cv2.createTrackbar("Val Min", "TrackBars", 41,255,empty)
cv2.createTrackbar("Val Max", "TrackBars", 255,255,empty)

while True:
   img = cv2.imread(path)
   imghue = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

   h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
   h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
   s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
   s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
   v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
   v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
   print(h_min, h_max, s_min, s_max, v_min, v_max)
   lower = np.array([h_min, s_min, v_min])
   upper = np.array([h_max, s_max, v_max])
   mask = cv2.inRange(imghue, lower, upper)
   imgResult = cv2.bitwise_and(img,img,mask=mask)

   cv2.imshow("original", img)
   cv2.imshow("hue image", imghue)
   cv2.imshow("masked", mask)
   cv2.imshow("Result", imgResult)
   cv2.waitKey(1)