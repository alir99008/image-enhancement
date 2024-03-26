# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 18:49:30 2022

@author: Hp
"""

#bilteral :   A bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing filter for images. It replaces the intensity of each pixel with a weighted average of intensity values from nearby pixels.
import cv2
#we use cv2 for biletrals and not use sk image because cv2 in much better then for biletrals
img = cv2.imread("saa.jpeg" , 0)

biletral_img = cv2.bilateralFilter(img,20, 50, 100 , borderType = cv2.BORDER_CONSTANT)    #20 is the diameter of each pixel neighbourhood use during filtering , 50 is the sigma value hum you want to blur other cases use sigma=50 , 100 is the sigma line space
cv2.imshow("orignal image",img)
cv2.imshow("Biletral image",biletral_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
