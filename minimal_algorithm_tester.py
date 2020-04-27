# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 18:34:02 2020

@author: dom
"""

import numpy as np
import cv2 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg


# input image
INPUT_IMAGE_PATH = 'C:/Users/domim/OneDrive/Desktop/bilder/normale/'
INPUT_IMAGE_PATH = 'C:/Users/domim/OneDrive/Desktop/bilder/seitlich/'
INPUT_IMAGE_FILENAME= '1.jpg'
INPUT_IMAGE_PATH_FILENAME = INPUT_IMAGE_PATH + INPUT_IMAGE_FILENAME

#output images
OUTPUT_IMAGE_PATH = 'C:/Users/domim/OneDrive/Desktop/bilder/neu/'
OUTPUT_IMAGE_FILENAME_1 = 'ffffff.jpg'
OUTPUT_IMAGE_PATH_FILENAME_1 = OUTPUT_IMAGE_PATH + OUTPUT_IMAGE_FILENAME_1

original_image = cv2.imread(INPUT_IMAGE_PATH_FILENAME)

k = (5  ,5)
print(k)
filtered = cv2.GaussianBlur(original_image, k , 0)

write = filtered

cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_1, write)
