# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 10:12:36 2022

@author: Hp
"""

# Unsharo image  

#unsharp image = orignal_image + amount *(orignal - blured)  #yeh formula ha image ko unsharo bnany ka

from skimage import io , img_as_float
from skimage.filters import unsharp_mask
from skimage.filters import gaussian
from matplotlib import pyplot as plt
import cv2

# first way to solve 

img = img_as_float(io.imread("saa.jpeg" , as_gray=True))        #filter jo hain wo zada tar floating pint image pr he apply hoty hain es liye hum float main image ko read krain gy..
gaussian_img = gaussian(img , sigma=4 , mode="constant" , cval=0.0)          #phr hum imgae ko blur krain gy es liye gaussain use kiya ha Q k yeh image ko blur krny ka kam krta ha 

img2 = (img - gaussian_img)*1     #phr yeh formula apply kiya ha  " amount *(orignal - blured)  "    amount means = k kitna hum apni picture to dark krain gy to clear hogi..1,2,3,4,5,sub try kr sakty hain
img3 = img + img2           #again apply to complte formula    orignal_image + amount *(orignal - blured)


fig = plt.figure(figsize=(8,8))
a1 = fig.add_subplot(2 ,2 ,1)
a1.imshow(img , cmap="gray")


a2 = fig.add_subplot(2 ,2 ,2)
a2.imshow(img2 , cmap="gray")

a3 = fig.add_subplot(2 ,2 ,3)
a3.imshow(img3 , cmap="gray")

plt.show()




#second way to solve both are the same but in this wway we solve formula in one line

unsharp_img = unsharp_mask(img , radius = 3 , amount =3)    #es main radius btata ha kitna hum ny blur krna ha pic ko "sigma wala func ha"  , amount btata ha multiplication factor  
#same to uper tha yeh B wohi ha

fig = plt.figure(figsize=(8,8))
a1 = fig.add_subplot(2 ,2 ,1)
a1.imshow(img , cmap="gray")
a1.title.set_text("orignal image")


a2 = fig.add_subplot(2 ,2 ,2)
a2.imshow(unsharp_img , cmap="gray")
a2.title.set_text("unsharp image")

plt.show()