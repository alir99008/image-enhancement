# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 12:05:13 2022

@author: Hp
"""

#sk image median filter in better then cv2 median filter

from skimage.filters import median
from skimage.morphology import disk
import cv2

img_as_gaussian_noise = cv2.imread("gaussian noisy.png",0)   #es main hum gaussain noise wali image ko read krain gy yahi jo blur wagara hoo usko clear krain gyyy
img_as_salted_paper = cv2.imread("saa.jpeg",0)     #es main hum salted background wali image ko read krain gy matlb jis image main doted spots wagara hoo

img = img_as_salted_paper #agr hum ny gaussian noise ka median check krna ha to hum uska idhr copy krain gy other wise  agr salted paper ka check krna ha to hum uska idhr likh dain gy

median_using_cv2 = cv2.medianBlur(img, 3)  #this three main matrix of 3*3 from the whole matrix       # [[2,5,1],        values of matric =  112235578       ,,, and the median of this matrix is =3      
                                                                                                      #  [5,7,3],
                                                                                                      #  [8,2,1]]



#disk(3) = [0, 0, 0, 1, 0, 0, 0],
#          [0, 1, 1, 1, 1, 1, 0],
#          [0, 1, 1, 1, 1, 1, 0],
#          [1, 1, 1, 1, 1, 1, 1],
#          [0, 1, 1, 1, 1, 1, 0],
#          [0, 1, 1, 1, 1, 1, 0],
#          [0, 0, 0, 1, 0, 0, 0]]
median_using_skimage = median(img, disk(3) , mode = "constant"  , cval = 0.0)



cv2.imshow("orignal image", img)
cv2.imshow("using cv2 gaussian image ",median_using_cv2)
cv2.imshow("using sk image gaussian" , median_using_skimage)
cv2.waitKey(0)
cv2.destroyAllWindows()