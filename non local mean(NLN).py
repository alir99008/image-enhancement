# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 19:39:54 2022

@author: Hp
"""

#non-local-mean(NLN) : Unlike "local mean" filters, which take the mean value of a group of pixels surrounding a target pixel to smooth the image, non-local means filtering takes a mean of all pixels in the image, weighted by how similar these pixels are to the target pixel.

import cv2
import numpy as np
from skimage import io , img_as_float , img_as_ubyte
from skimage.restoration import denoise_nl_means , estimate_sigma



img  = img_as_float(io.imread("saa.jpeg", as_gray=True))

est_sigma = np.mean(estimate_sigma(img , multichannel=True))  #yeh estimate sigma hum es liye nikalty hain Q k denoise_nl_mean nikalny k liye yeh requirment ha.......

denoise_img = denoise_nl_means(img , h=10*est_sigma , fast_mode=True , patch_size = 5 , patch_distance = 3 , multichannel=True)   #es main h jitna zada hoga image utni smooth hogi , fasetmode = True ka matlab hum apni image ko fast mode main run krna chahty hain , pathsize = 3 ka matlab wo 3*3 k matrix ko dekhy ga , multichannel = True ka matlab k color image pr kam hoga


denoise_img_as_8_bit = img_as_ubyte(denoise_img)   #es main hm ny floating main jo image read ki thi usko dubara int main convert kiya q k hum ny int values main image ko show krwana tha 
real_img_as_8_bit = img_as_ubyte(img)   

cv2_real_denoise_image = cv2.cvtColor(denoise_img_as_8_bit, cv2.COLOR_BGR2RGB)    #Q k hum ny sk image use kiya tha int main image ko convert krny k liye es liye hum q k cv2 BGR main image leta ha es liye hum es k color ko dubara RGB main convert krain gy....
cv2_real_image = cv2.cvtColor(real_img_as_8_bit, cv2.COLOR_BGR2RGB)    ##Q k hum ny sk image use kiya tha int main image ko convert krny k liye es liye hum q k cv2 BGR main image leta ha es liye hum es k color ko dubara RGB main convert krain gy....

cv2.imshow("denoise image",denoise_img_as_8_bit)       #hum ny socha k without RGB main convert kiye image ko show krwaty hain jo denoise image usko
cv2.imshow("real image",real_img_as_8_bit)    # #hum ny socha k without RGB main convert kiye image ko show krwaty hain jo real image usko
cv2.imshow("cv2 real image",cv2_real_image)    #es main hum ny pehly RGB main convert kiya phr show krai real image
cv2.imshow("cv2 real denoise image",cv2_real_denoise_image)   #es main hum ny pehly RGB main convert kiya phr show krai real image

cv2.waitKey(0)
cv2.destroyAllWindows()