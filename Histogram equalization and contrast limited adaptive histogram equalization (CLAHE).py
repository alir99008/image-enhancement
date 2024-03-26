# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:57:21 2022

@author: Hp
"""

import cv2 
from skimage import io
from matplotlib import pyplot as plt


img = cv2.imread("fog.jpg" , 1)  #hum fog wali 1 color image read krain gy


lab_img = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)      #jo image hum read krain gy wo BGR main hogi lakin hum usko LAB Color main conver krain gy

#plt.hist(img.flat , bins=100 , range=(0,255))          #jo hamri orignal image ha uska histogram

#plt.hist(lab_img.flat , bins=100 , range=(0,255))   #jo image hum ny LAB color main convert ki uska histogram

l , a , b =cv2.split(lab_img)        #HUM l a b color ko split kr k apny apny variables main show krwa dain gy   l (lightness ko store krta ha)   a (ki range green to mahnita tk hoti ha uski range main colors ko store krta ha) or    b (ki range blue to yellow hoti ha us main yeh colors ko store krta ha)

plt.hist(l.flat , bins = 100 , range=(0,255) )
plt.show()
plt.hist(a.flat , bins = 100 , range=(0,255) )
plt.show()
plt.hist(b.flat , bins = 100 , range=(0,255) )
plt.show()

equ = cv2.equalizeHist(l)    #Q k hamary pas jo L ka histrogram graph tha us main pixel zada white ki traf show ho rhy thy es liye hamari picture main light zada thi phr hum ny us l k graph ko equalize kiya jis k 0 - 255 equally distribute ho gay or picture main light kam hogai
update_lab_img_1 = cv2.merge((equ , a , b))   #wo jab hum ny L ko equalize kr liye to dusry colors k sath dubara merge kr liye
plt.hist(update_lab_img_1.flat , bins = 100 , range=(0,255) )

hist_eq_img = cv2.cvtColor(update_lab_img_1, cv2.COLOR_LAB2BGR)     #Q k hum ny apni imge ko LAB main CONvert kiya tha histogram graph equalized krny k liye to es liye hum apni image ko dubara BGR main convert krain gy
#plt.hist(hist_eq_img.flat , bins = 100 , range=(0,255) )
plt.show()


#Clahe img
# YEH B HISToGRAM graph ki trah graph ko equalized kr k image k color ko set krti ha
#Q k jab hum histogram main image change krty hain to hamari image k corner dark ho jaty hain es liye hum chaly use krty hain ta k edge K color dark na ho zada

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #Clahe tab he kam kry ga jab hamari image ko hum gray main read krain gy
clahe = cv2.createCLAHE(clipLimit=20.0, tileGridSize=(8, 8))   #cliplimit jitni zada krty jain gy hamari picture  fake lagna shoro ho jay gii yeh humm alag alag value enter kr k try kr sakty hain   , tileGridSize by default 8,8 hota ha es ka matlab shahid picture ka size hoo    
equalized = clahe.apply(gray)     #es main hum apni gray image pr clay apply krain gy

update_lab_img_2 = cv2.merge((equalized , a ,b))   # es main hum apni equalized hoe image or a b colors ko merge kraingy

CLAHE_img = cv2.cvtColor(update_lab_img_2,cv2.COLOR_LAB2BGR)     #es main hum apni image k color dubara LAB sy BGR main convert krain gy

cv2.imshow("orignalimage",img)
cv2.imshow("hist equized image",hist_eq_img)
cv2.imshow("CLAHE image",CLAHE_img)


cv2.waitKey(0)
cv2.destroyAllWindows()