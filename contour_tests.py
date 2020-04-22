import numpy as np
import cv2 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

## CONSTANTS

# input image
#INPUT_IMAGE_PATH = 'C:/Users/domim/OneDrive/Desktop/bilder/normale/'
INPUT_IMAGE_PATH = 'C:/Users/domim/OneDrive/Desktop/bilder/seitlich/'
INPUT_IMAGE_FILENAME= '1.jpg'
INPUT_IMAGE_PATH_FILENAME = INPUT_IMAGE_PATH + INPUT_IMAGE_FILENAME

#output images
OUTPUT_IMAGE_PATH = 'C:/Users/domim/OneDrive/Desktop/bilder/neu/'
OUTPUT_IMAGE_FILENAME_1 = 'transformed1__approximated.jpg'
OUTPUT_IMAGE_PATH_FILENAME_1 = OUTPUT_IMAGE_PATH + OUTPUT_IMAGE_FILENAME_1

OUTPUT_IMAGE_FILENAME_2 = 'transformed2__approximated.jpg'
OUTPUT_IMAGE_PATH_FILENAME_2 = OUTPUT_IMAGE_PATH + OUTPUT_IMAGE_FILENAME_2

OUTPUT_IMAGE_FILENAME_ORIGINAL = 'tr_original.jpg'
OUTPUT_IMAGE_PATH_FILENAME_3 = OUTPUT_IMAGE_PATH + OUTPUT_IMAGE_FILENAME_ORIGINAL

OUTPUT_IMAGE_FILENAME_GRAYSCALED = 'tr_grayscaled.jpg'
OUTPUT_IMAGE_PATH_FILENAME_4 = OUTPUT_IMAGE_PATH + OUTPUT_IMAGE_FILENAME_GRAYSCALED


OUTPUT_IMAGE_FILENAME_THRESHOLDED = 'tr_thresholded.jpg'
OUTPUT_IMAGE_PATH_FILENAME_5 = OUTPUT_IMAGE_PATH + OUTPUT_IMAGE_FILENAME_THRESHOLDED

OUTPUT_IMAGE_FILENAME_FILTERED = 'tr_filtered.jpg'
OUTPUT_IMAGE_PATH_FILENAME_6 = OUTPUT_IMAGE_PATH + OUTPUT_IMAGE_FILENAME_FILTERED

## READ FILE ##
original_image = cv2.imread(INPUT_IMAGE_PATH_FILENAME)
grayscaled = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY ) 
filtered = cv2.GaussianBlur(grayscaled, (9  ,9), 0)
rect, thresholded = cv2.threshold(filtered , 0, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)
#thresholded = cv2.adaptiveThreshold(filtered , 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 7, 3)
#thresholded  = cv2.adaptiveThreshold(filtered , 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 5, 3) 
#rect, thresholded = cv2.threshold(filtered , 60, 255, cv2.THRESH_BINARY) 

def array_to_tuple(arr):
    """Converts array to tuple"""

    return tuple(arr.reshape(1, -1)[0])


def draw_contour_outline(img, cnts, color, thickness=1):
    """Draws contours outlines of each contour"""

    for cnt in cnts:
        cv2.drawContours(img, [cnt], 0, color, thickness)

def draw_contour_points(img, cnts, color):
    """Draw all points from a list of contours"""

   
    for cnt in cnts:
        # print(cnt.shape)
        # print(cnt)
        squeeze = np.squeeze(cnt)
        # print(squeeze.shape)
        # print(squeeze)

        for p in squeeze:
            p = array_to_tuple(p)
                   
            if len(p) > 1:     
                cv2.circle(img, p , 1, color, -1)
            
    return img


contours, hierarchy = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours2, hierarchy2 = cv2.findContours(thresholded, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)



# Show the number of detected contours for each call:
number_detected_contours = format(len(contours))
number_detected_contours2 = format(len(contours2))
print("detected contours (RETR_EXTERNAL): '{}' ".format(len(contours)))
print("detected contours (RETR_LIST): '{}' ".format(len(contours2)))
# Copy image to show the results:
image_contours = original_image.copy()
image_contours_2 = original_image.copy()

# Draw the outline of all detected contours:


draw_contour_points(image_contours, contours, (0, 0, 255))
draw_contour_points(image_contours_2, contours2, (255,0 , 0))

#draw_contour_outline(image_contours, contours, (0, 0, 255), 5)
#draw_contour_outline(image_contours_2, contours2, (255, 0, 0), 5)


## DISPLAY IMAGE WITH MATLLIB ##
# Create the dimensions of the figure and set title:
fig = plt.figure(figsize=(20, 20))
plt.suptitle("Find Conturs in Cow: Preprocessing Steps", fontsize=14, fontweight='bold')
fig.patch.set_facecolor('silver')

ax = plt.subplot(3, 2, 1)
plt.imshow(original_image,)
plt.title('Original Image')
plt.axis('off')


ax = plt.subplot(3, 2, 2)
plt.imshow(grayscaled, cmap='gray')
plt.title('Grayscaled')

ax = plt.subplot(3, 2, 3)
plt.imshow(filtered, cmap='gray')
plt.title('Filtered')


ax = plt.subplot(3, 2, 4)
plt.imshow(thresholded, cmap='gray')
plt.title('Thresholded')
plt.axis('off')

m = cv2.moments(contours[0])
print(m)
print()
plt.show()

fig = plt.figure(figsize=(20, 8))
plt.suptitle("Find Conturs in Cow: Result Comparison", fontsize=14, fontweight='bold')
fig.patch.set_facecolor('silver')

ax = plt.subplot(1, 2, 1)
plt.imshow(image_contours, cmap='gray')
plt.title('cv2.RETR_EXTERNAL: Number of Detected Contours: ' + number_detected_contours)
plt.axis('off')


ax = plt.subplot(1, 2, 2)
plt.imshow(image_contours_2, cmap='gray')
plt.title('Grayscale: cv2.RETR_LIST Number of Detected Contours: ' + number_detected_contours2)
plt.axis('off')
plt.show()

#SAVE THE IMAGE#

cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_1, image_contours)
cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_2, image_contours_2)
cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_3, original_image)
cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_4, grayscaled)
cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_5, thresholded)