# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:09:40 2022

@author: Hp
"""

import cv2
from skimage import io


img = cv2.imread("image.jpg",1)
B, G ,R  = cv2.split(img)




img1 = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
l , a, b=cv2.split(img1)



img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h ,s, v = cv2.split(img)



cv2.imshow("B" , B)
cv2.imshow("G" , G)
cv2.imshow("R" , R)

cv2.imshow("L" , l)
cv2.imshow("A" , a)
cv2.imshow("BB" , b)


cv2.imshow("H" , h)
cv2.imshow("S" , s)
cv2.imshow("V" , v)


cv2.waitKey(0)
cv2.destroyAllWindows()