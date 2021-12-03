#programación detección de frutas
import cv2
import numpy as np

im1= cv2.imread('./Frutas/pera.jpg',0)
im1lsm=cv2.imread('./Frutas/pera-lsm.png',255)

#reescalamiento
res1=cv2.resize(im1,(550,530),interpolation=cv2.INTER_CUBIC)
res1lsm=cv2.resize(im1lsm,(550,530),interpolation=cv2.INTER_CUBIC)
#filtro por gausiano 
blur1 = cv2.GaussianBlur(res1,(5,5),0)

#método por umbral 
_,bin1 =cv2.threshold(blur1,200,255,cv2.THRESH_BINARY)

cv2.imshow('imagen 1',bin1)
cv2.imshow('imagen lsm',res1lsm)

cv2.waitKey(0)
cv2.destroyAllWindows