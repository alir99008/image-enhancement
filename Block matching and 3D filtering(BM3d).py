# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 22:47:48 2022

@author: Hp
"""

from skimage import io , img_as_float
import bm3d
import cv2

img = img_as_float(io.imread("saa.jpeg",as_gray=True))

denoise_img = bm3d.bm3d(img , sigma_psd = 0.2 , stage_arg = bm3d.BM3DStages.HARD_THRESHOLDING)    #sigma_psd is the amount of blurring or smoothing but we can set values from 0 to 1 because of reading floating pint image   , stage_arg = bm3d_hard_threshholding this is the filter we can set..

denoise_img1 = bm3d.bm3d(img , sigma_psd = 0.4, stage_arg = bm3d.BM3DStages.ALL_STAGES)   #BM3D ALL stages mean that we can set all stages this is more power full but slow.....

#denoise_img2 = bm3d.bm3d(img , sigma_psd = 0.2 , stage_argl = bm3d.BM3DStages.WIENER_FILTERING)

cv2.imshow("orignal image ", img)
cv2.imshow("denoise image ",denoise_img)
cv2.imshow("All Stages ",denoise_img1)
#cv2.imshow("Wiener Filtering ",denoise_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()