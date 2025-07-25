import cv2
import numpy as np

apple = cv2.imread("apple.jpg")
orange = cv2.imread("orange.jpg")

apple = cv2.resize(apple, (400, 400))  
orange = cv2.resize(orange, (400, 400))  
print(apple.shape, orange.shape)

apple_orange = np.hstack((apple[:, :200], orange[:, 200:]))  # Stack images horizontally

### Gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6): 
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

##### Gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):  
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

##### Laplacian pyramid for apple
apple_copy = gp_apple[5] 
lp_apple = [apple_copy]

for i in range(5, 0, -1):  
    gassian_expanded = cv2.pyrUp(gp_apple[i], dstsize=(gp_apple[i - 1].shape[1], gp_apple[i - 1].shape[0]))  
    laplacian = cv2.subtract(gp_apple[i - 1], gassian_expanded)
    lp_apple.append(laplacian)

###### Laplacian pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy] 
for i in range(5, 0, -1):
    gassian_expanded = cv2.pyrUp(gp_orange[i], dstsize=(gp_orange[i - 1].shape[1], gp_orange[i - 1].shape[0]))  
    laplacian = cv2.subtract(gp_orange[i - 1], gassian_expanded)
    lp_orange.append(laplacian)

####### Now join left and right part of both images
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n = n + 1
    cols, rows, ch = apple_lap.shape  
    laplacian = np.hstack((apple_lap[:, :cols // 2], orange_lap[:, cols // 2:]))
    apple_orange_pyramid.append(laplacian)

## Now reconstruct the images
apple_orange_reconstructed = apple_orange_pyramid[0]
for i in range(1, 6): 
    apple_orange_reconstructed = cv2.pyrUp(
        apple_orange_reconstructed,
        dstsize=(apple_orange_pyramid[i].shape[1], apple_orange_pyramid[i].shape[0]))
    apple_orange_reconstructed = cv2.add(apple_orange_pyramid[i], apple_orange_reconstructed)

cv2.imshow("apple", apple)
cv2.imshow("orange", orange)
cv2.imshow("apple_orange", apple_orange)  # Display the horizontally stacked image
cv2.imshow("apple_orange_reconstructed", apple_orange_reconstructed)

cv2.waitKey(0)
cv2.destroyAllWindows()
