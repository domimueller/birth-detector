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
OUTPUT_IMAGE_FILENAME_1 = 'transformed1.jpg'
OUTPUT_IMAGE_PATH_FILENAME_1 = OUTPUT_IMAGE_PATH + OUTPUT_IMAGE_FILENAME_1

OUTPUT_IMAGE_FILENAME_2 = 'transformed2.jpg'
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



def hist_color_img(img):
    """Calculates the histogram for a three-channel image"""

    histr = []
    histr.append(cv2.calcHist([img], [0], None, [256], [0, 256]))
    histr.append(cv2.calcHist([img], [1], None, [256], [0, 256]))
    histr.append(cv2.calcHist([img], [2], None, [256], [0, 256]))
    
    return histr

def equalize_hist_color(img):
    """Equalize the image splitting the image applying cv2.equalizeHist() to each channel and merging the results"""

    channels = cv2.split(img)
    eq_channels = []
    for ch in channels:
        eq_channels.append(cv2.equalizeHist(ch))

    eq_image = cv2.merge(eq_channels)
    return eq_image

def show_hist_with_matplotlib_rgb(hist, title, pos, color):
    """Shows the histogram using matplotlib capabilities"""

    ax = plt.subplot(3, 4, pos)
    # plt.title(title)
    plt.xlabel("bins")
    plt.ylabel("number of pixels")
    plt.xlim([0, 256])

    for (h, c) in zip(hist, color):
        plt.plot(h, color=c)

def equalize_hist_color_hsv(img):
    """Equalizes the image splitting it after HSV conversion and applying cv2.equalizeHist()
    to the V channel, merging the channels and convert back to the BGR color space
    """

    H, S, V = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
    eq_V = cv2.equalizeHist(V)
    eq_image = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2BGR)
    return eq_image




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
                cv2.circle(img, p , 2, color, -1)
            
    return img
#old appoaches
hist_color = hist_color_img(original_image)
image_equalized_3_channels = equalize_hist_color(original_image)
hist_image_eq = hist_color_img(image_equalized_3_channels)

hsv_equalized_image = equalize_hist_color_hsv(original_image)
          
# Equalize the image and calculate histogram:


show_hist_with_matplotlib_rgb(hist_color, "color histogram", 1, ['b', 'g', 'r'])
show_hist_with_matplotlib_rgb(hist_image_eq, "color histogram equalized", 5, ['b', 'g', 'r'])

grayscaled = cv2.cvtColor(hsv_equalized_image, cv2.COLOR_BGR2GRAY ) 
filtered = cv2.GaussianBlur(grayscaled, (9  ,9), 0)
#rect, thresholded = cv2.threshold(filtered , 0, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)
thresholded = cv2.adaptiveThreshold(filtered , 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 3)
#thresholded  = cv2.adaptiveThreshold(filtered , 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 5, 3) 
#rect, thresholded = cv2.threshold(filtered , 60, 255, cv2.THRESH_BINARY) 

contours, hierarchy = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours2, hierarchy2 = cv2.findContours(thresholded, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)



# Show the number of detected contours for each call:
number_detected_contours = format(len(contours))
number_detected_contours2 = format(len(contours2))
print("detected contours (RETR_LIST): '{}' ".format(len(contours)))
print("detected contours (RETR_LIST): '{}' ".format(len(contours2)))
# Copy image to show the results:
image_contours = original_image.copy()
image_contours_2 = original_image.copy()

# Draw the outline of all detected contours:

draw_contour_outline(image_contours, contours, (0, 0,255 ), 2)
draw_contour_outline(image_contours_2, contours2, (0, 0, 255), 2)

#draw_contour_points(image_contours, contours, (255, 0, 0))
#draw_contour_points(image_contours_2, contours2, (255,0 , 0))




## DISPLAY IMAGE WITH MATLLIB ##
# Create the dimensions of the figure and set title:
fig = plt.figure(figsize=(20, 20))
plt.suptitle("Find Conturs in Cow: Preprocessing Steps", fontsize=14, fontweight='bold')
fig.patch.set_facecolor('silver')

ax = plt.subplot(10, 2, 1)
plt.imshow(original_image,)
plt.title('Original Image')
plt.axis('off')

ax = plt.subplot(10, 2, 2)
plt.imshow(image_equalized_3_channels,)
plt.title('Equalized Image (3 Channels)')
plt.axis('off')

ax = plt.subplot(10, 2, 3)
plt.imshow(hsv_equalized_image, cmap='hsv')
plt.title('Equalized Image (hsv)')
plt.axis('off')


ax = plt.subplot(10, 2, 5)
plt.imshow(grayscaled, cmap='gray')
plt.title('Grayscaled')

ax = plt.subplot(10, 2, 6)
plt.imshow(filtered, cmap='gray')
plt.title('Filtered')


ax = plt.subplot(10, 2, 7)
plt.imshow(thresholded, cmap='gray')
plt.title('Thresholded')
plt.axis('off')



fig = plt.figure(figsize=(20, 8))
plt.suptitle("Find Conturs in Cow: Result Comparison", fontsize=14, fontweight='bold')
fig.patch.set_facecolor('silver')

ax = plt.subplot(1, 2, 1)
plt.imshow(image_contours)
plt.title('cv2.RETR_EXTERNAL: Number of Detected Contours: ' + number_detected_contours)
plt.axis('off')


ax = plt.subplot(1, 2, 2)
plt.imshow(image_contours_2)
plt.title('Grayscale: cv2.RETR_LIST Number of Detected Contours: ' + number_detected_contours2)
plt.axis('off')
plt.show()

#SAVE THE IMAGE#

cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_1, image_contours)
cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_2, image_contours_2)
cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_3, original_image)
cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_4, grayscaled)
cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_5, thresholded)

cv2.imwrite(OUTPUT_IMAGE_PATH + 'hsv.jpg', hsv_equalized_image)
cv2.imwrite(OUTPUT_IMAGE_PATH + '3-channel-eq.jpg', image_equalized_3_channels)
cv2.imwrite(OUTPUT_IMAGE_PATH + 'filtered.jpg', filtered)
