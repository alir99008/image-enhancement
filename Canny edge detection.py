# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 09:08:58 2022

@author: Hp
"""
#Canny  :  The Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images. 
#Canny edge detection is a technique to extract useful structural information from different vision objects and dramatically reduce the amount of data to be processed. It has been widely applied in various computer vision systems.
#Find the intensity gradients of the image. Apply non-maximum suppression to get rid of spurious response to edge detection. Apply double threshold to determine potential edges.


import cv2
import numpy as np


img = cv2.imread("image.jpg" , 0)

# Way 1
#canny
#when we use canny we set the value of the threshhold 1 and threshold 2 sometime it sets to find the best edge detection but sometimes its create extra edge becuse of the values not fit you can see in the image when you run.
canny_edge = cv2.Canny(img, 30, 40)    #50 is threshhold 1 and 80 is treshhold 2

#Way 2
# Auto Canny
# In Auto canny it adjest the edges automatically and extract good and extra useful imformation so we use auto canny more to find edge detection.
sigma =  0.4   #sigma is the value k apni kitni imformation extract krna chahty hain 0.4 ka matlab ha 40 %
median = np.median(img)  # we take the median of the image usin numpy array
lower = int(max(0,(1.0-sigma)+median))    # yeh threshhold 1 ki value hogi pehly yeh 1.0 - sigma ko minus kry ga phr us k bad  plus kry ga median k sath phr  max find kry ga jonsa  number hamary pas max hoga to usko choose kry ga agr floating point number agr hamary pas maximum howa to usko int main conert kry Q k hum integer main apni image ko read krain gy es liye
upper = int(max(255,(1.0+sigma)+median))   #yeh threshhold 2 ki value hogi or baki sary procedure uper wali lines k he hongay


auto_canny = cv2.Canny(img, lower,upper)  #dubara canny ka function call hoga lakin es time hamary pas jo values hamary pas formula sy nikli thi thi lower or uper bound ki wo hum use krain gy Q k esi sy hamara cannny auto bany ga
cv2.imshow("orignal imgae", img)
cv2.imshow("canny image" , canny_edge)
cv2.imshow(" auto canny image" , auto_canny)

cv2.waitKey(0)
cv2.destroyAllWindows()