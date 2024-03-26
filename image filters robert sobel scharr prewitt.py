# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 23:26:20 2022

@author: Hp
"""

#yeh sub filters hain lakin in  main sub sy acha or popular filter sobel ha

import cv2 
from skimage.filters import roberts , sobel , scharr , prewitt


img = cv2.imread("saa.jpeg" , 0)

robert_img = roberts(img)
sobel_img = sobel(img)
scharr_img = scharr(img)
prewitt_img = prewitt(img)


cv2.imshow("Robert",robert_img)
cv2.imshow("sobel", sobel_img)
scharr_img("scharr",scharr_img)
prewitt("prewitt",prewitt_img)


cv2.waitKey(0)
cv2.destroyAllWindows()



