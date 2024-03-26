# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 21:50:22 2022

@author: Hp
"""
#TVF  : remove unwanted details while preserving important details such as edge detection etc


import cv2
from skimage import io , img_as_float
from skimage.restoration import denoise_tv_chambolle


img = img_as_float(io.imread("saa.jpeg" ))
denoise_img = denoise_tv_chambolle(img , weight= 0.3, eps=0.0000002 , n_iter_max=100 , multichannel=True)
#es line no 14 main weight 0.5 q k hum ny image float main read ki ha es liye weight 0 sy 1 tk he hoga laki jitn azada wait hoga utni zada denoising hogi or hamari picture blur or cartoonish banti jay gii
#eps ka matlab hota ha error find krna or yeh jitni choti value hogi utna choty sy chota error detect ho saky ga lakin image utni he late load hogi Q k error detection main utna he zada time lagay ga 
#n_iter_max ka matlab k eps ka error 100 iteration main find kry ga agr hogya to saii warna 100 iterna k bad stop ho jay ga error find krna..
#multichannel true es liye ha Q k hum color images k sath kam kr rhy hain es liye...


cv2.imshow("orignal image", img)
cv2.imshow("donoise image",denoise_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


