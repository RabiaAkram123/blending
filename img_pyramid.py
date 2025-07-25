# ##############pyramid downsampling##############
# ##############gussian pyramid##############
# import cv2
# import numpy as np
# img=cv2.imread("hadi.jpg")
# resized_img=cv2.resize(img,(800,600))  # Resize the image to 800x600 pixels
# lr1=cv2.pyrDown(resized_img)  # Downsample the image
# lr2=cv2.pyrDown(lr1)  # Downsample the image
# hr=cv2.pyrUp(lr2)
# hr2=cv2.resize(hr,(800,600))


# cv2.imshow('image',resized_img)
# cv2.imshow('pyrDown1',lr1)
# cv2.imshow('pyrDown2',lr2)
# cv2.imshow('pyrup1',hr2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
##############gusian multiple  pyramid###############
import cv2
import numpy as np
img=cv2.imread("hadi.jpg")
resized_img=cv2.resize(img,(800,600))# Resize the image to 800x600 pixels
layer=resized_img.copy()  # Create a copy of the resized image
gp=[layer]

for i in range(6):
    layer=cv2.pyrDown(layer)  # Downsample the image
    gp.append(layer)  # Append the downsampled image to the list
    cv2.imshow(str(i),layer)  # Display each layer
cv2.imshow('image',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()