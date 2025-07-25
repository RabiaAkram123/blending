###########contour.py###########

import cv2
img=cv2.imread('logo.png')
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(grayimg,127,255,0)
contours,hirarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #using method to get countours list and hirarchy data
print('number of contours:'+str(len(contours)))
print(contours[0])

cv2.drawContours(img,contours,-1,(0,255,0),3)


cv2.imshow('image',img)
cv2.imshow('gray image',grayimg)
cv2.waitKey(0)          
cv2.destroyAllWindows()

