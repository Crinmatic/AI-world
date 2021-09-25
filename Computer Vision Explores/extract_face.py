# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 08:34:03 2020

@author: King alagbe
"""

from keras.models import load_model


from os import listdir
from PIL import Image
from numpy import asarray
import matplotlib.pyplot as plt
from mtcnn.mtcnn import MTCNN
import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from glob import glob
from os.path import isdir
import os
import cv2
    #create detector using default weights
    #EXTRACT FACE FROM SINGLE PHOTO
f1 = r'C:\Users\King alagbe\.spyder-py3\facedata\train\anu\anu (2).jpg'
img = cv2.imread(f1)
resiz = cv2.resize(img, ((160,160)))
print(resiz.shape)
im = asarray(resiz)
print(im)
    
detector =  MTCNN()
faces = detector.detect_faces(im)
for face in faces:
    print(face)
print('done')
   

 
