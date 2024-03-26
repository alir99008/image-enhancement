# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 12:03:15 2022

@author: Hp
"""


#gaussian denoising : es main hum apni apni picture ki noise wagara khatm kr k apni picture ko samooth krty hain hain jis sy hum gaussain smoothing kehty hain....


from skimage import io , img_as_float
from skimage.filters import gaussian
import cv2
from matplotlib import pyplot as plt


#jub hum filters apply krty hain to es k liye lazmi ha k hum apni picture ko float main read krain or gray main read krain tab he hmarai picture pr filters ka asar hoga

img_as_gaussian_noise = img_as_float(io.imread("gaussian noisy.png",as_gray=True))   #es main hum gaussain noise wali image ko read krain gy yahi jo blur wagara hoo usko clear krain gyyy
img_as_salted_paper = img_as_float(io.imread("saa.jpeg",as_gray=True))     #es main hum salted background wali image ko read krain gy matlb jis image main doted spots wagara hoo


 
gaussian_using_cv2 = cv2.GaussianBlur(img_as_gaussian_noise, (3,3),7 , borderType = cv2.BORDER_CONSTANT)
gaussian_using_skimage = gaussian(img_as_gaussian_noise , sigma=1 , mode = "constant" , cval=0.0)


#es main hum apni gaussian sy read ki hoe orignal image ko  cv2 sy change ki pic or skimage sy change ki hoe pic ko cv2 libaray ki zariye show krawain gy...  
cv2.imshow("orignal image", img_as_gaussian_noise)
cv2.imshow("using cv2 gaussian image ",gaussian_using_cv2)
cv2.imshow("using sk image gaussian" , gaussian_using_skimage)
cv2.waitKey(0)
cv2.destroyAllWindows()


#es main hum cv2 library or skimage dono tareeky sy salted paper wali images sy background main dot spoted remove krain gy or dekahin gy konsi libaray zada achi ha gauusain noise ko remove krny main..
salted_using_cv2 = cv2.GaussianBlur(img_as_salted_paper, (3,3),0 , borderType = cv2.BORDER_CONSTANT)     #this three main matrix of 3*3 from the whole matrix multiply by kernal      # [[2,5,1],       [4,2,6]    = 2*4+5*2+1*6+5*2+7*8+3*3+8*7+2*3+1*1 = 162   this values put in the middle  in the spot of 7   or border constant ka matlb k har border k sath 0 aajay ga        
                                                                                                                                                                                      #  [5,7,3],    *  [2,8,3]
                                                                                                                                                                                      #  [8,2,1]]       [7,3,1]
salted_using_skimage = gaussian(img_as_salted_paper , sigma=1 , mode = "constant" , cval=0.0)


#or matplotlib sy show krain gy.... salted paper wali pictures.....
fig = plt.figure(figsize = (10,10))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img_as_salted_paper , cmap = "gray")
ax1.title.set_text("Orignal image")


ax2 = fig.add_subplot(2,2,2)
ax2.imshow(salted_using_cv2 , cmap = "gray")
ax2.title.set_text("Salted using cv2 image")



ax3 = fig.add_subplot(2,2,3)
ax3.imshow(salted_using_skimage , cmap = "gray")
ax3.title.set_text("Salted using skimage image")

plt.show()

