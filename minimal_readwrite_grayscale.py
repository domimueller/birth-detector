import numpy as np
import cv2 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

## CONSTANTS

# input image
INPUT_IMAGE_PATH = 'C:/Users/domim/OneDrive/Desktop/bilder/normale/'
INPUT_IMAGE_FILENAME= 'test.jpg'
INPUT_IMAGE_PATH_FILENAME = INPUT_IMAGE_PATH + INPUT_IMAGE_FILENAME

#output image
OUTPUT_IMAGE_PATH = 'C:/Users/domim/OneDrive/Desktop/bilder/neu/'
OUTPUT_IMAGE_FILENAME = 'transformed2.jpg'
OUTPUT_IMAGE_PATH_FILENAME = OUTPUT_IMAGE_PATH + OUTPUT_IMAGE_FILENAME

## READ FILE ##
img = cv2.imread(INPUT_IMAGE_PATH_FILENAME)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY ) 
img2 = cv2.GaussianBlur(img, (9  ,9), 0)

#img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 9, 3)
#img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 5, 3) 
#rect, img = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY) 
rect, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)


## DISPLAY IMAGE WITH MATLLIB ##
# Create the dimensions of the figure and set title:
fig = plt.figure(figsize=(12, 5))
plt.suptitle("Contours introduction", fontsize=14, fontweight='bold')
fig.patch.set_facecolor('silver')

ax = plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('title')


ax = plt.subplot(1, 2, 2)
plt.imshow(img2, cmap='gray')
plt.title('title2')
plt.axis('off')

plt.show()
#SAVE THE IMAGE#
cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME, img)

print('fertig')