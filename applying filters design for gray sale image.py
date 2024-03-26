# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:41:16 2022

@author: Hp
"""

from skimage.color.adapt_rgb import adapt_rgb ,each_channel , hsv_value
from skimage import io ,filters
import cv2
from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from skimage import exposure

img = io.imread("monalisa.jpg")
apply_sobel = filters.sobel(img)


@adapt_rgb(each_channel)    #yeh decorators hoty hain jo hamary pas built in pehly sy factonalize kiye hory hain hum ny  each_channel ka matlab k yeh rgb k k 3no channel py sobel filter apply kr dy ga
def sobel_each(image):     #function which accept image
    return filters.sobel(image)       #yeh sobel ka filter apply kry ga RGB 3no channel py..

@adapt_rgb(each_channel)   #yeh decorators hoty hain jo hamary pas built in pehly sy factonalize kiye hory hain hum ny  each_channel ka matlab k yeh rgb k k 3no channel py mediun blur filter apply kr dy ga
def median_each(image , k):     #function which accept image and k=kernal e.g k=3 to yeh 3*3 k metrix ko use krty howy image ki values change kry ga median ka filter use kr k
    return cv2.medianBlur(image,k) 

@adapt_rgb(hsv_value)  #yeh decorators hoty hain jo hamary pas built in pehly sy factonalize kiye hory hain hum ny  hsv k sirf v means value waly function py sobel filter apply kr dy ga
def sobel_hsv(image):
    return filters.sobel(image)
    

each_channel_image = sobel_each(img)     #function ko call kr k return hoe image accpt kr k variable main store kr dain gy
hsv_value_image = sobel_hsv(img)
median_blur_image = median_each(img , 3)

#plt.imshow(apply_sobel)
#plt.imshow(each_channel_image)
#plt.imshow(hsv_value_image)
#plt.imshow(median_blur_image)


@adapt_rgb(each_channel)  #yeh decorators hoty hain jo hamary pas built in pehly sy factonalize kiye hory hain hum ny  each_channel ka matlab k yeh rgb k k 3no channel py sobel filter apply kr dy ga
def equalize_each(image):
    return exposure.equalize_hist(image)   #yeh histogram equalization ka built in function ha jo k r,g,b 3no color ko equalize kr kr 0-255 colors ko merge kr k image return kr dy ga  lakin r g b 3no py apply krny sy image zada bright ho jay gii

@adapt_rgb(hsv_value)     # #yeh decorators hoty hain jo hamary pas built in pehly sy factonalize kiye hory hain hum ny  hsv k sirf v means value waly function py sobel filter apply kr dy ga
def equalize_hsv(image):
    return exposure.equalize_hist(image)     ##yeh histogram equalization ka built in function ha jo hsv k sirf value wali value ko ko equalize kr kr 0-255 colors ko merge kr k image return kr dy ga    

equ_rgb = equalize_each(img)
equ_hsv = equalize_hsv(img)


fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(3,3,1)
ax.imshow(img)
ax.title.set_text("orignal image")



ax1 = fig.add_subplot(3,3,2)
ax1.imshow(each_channel_image)
ax1.title.set_text("Each RGB CHANNEL")

ax2 = fig.add_subplot(3,3,3)
ax2.imshow(hsv_value_image)
ax2.title.set_text("HSV VALue image")


ax3 = fig.add_subplot(3,3,4)
ax3.imshow(median_blur_image)
ax3.title.set_text("Median blur image")


ax4 = fig.add_subplot(3,3,5)
ax4.imshow(equ_rgb)
ax4.title.set_text("Histogram on each RGB")

ax5 = fig.add_subplot(3,3,6)
ax5.imshow(equ_hsv)   #yeh wala function sub sy zada img show kry ga Q k na es main image zada bright hoti ha na dark rehti ha 
ax5.title.set_text("histogram on hsv value")

plt.show()
