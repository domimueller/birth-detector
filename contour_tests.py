import numpy as np
import cv2 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

## CONSTANTS

# input image
INPUT_IMAGE_PATH = 'C:/Users/domim/OneDrive/Desktop/bilder/normale/'
INPUT_IMAGE_PATH = 'C:/Users/domim/OneDrive/Desktop/bilder/seitlich/'
INPUT_IMAGE_FILENAME= '1585691986.5171263-300x225.jpg'
INPUT_IMAGE_FILENAME= '2.jpg'

INPUT_IMAGE_PATH_FILENAME = INPUT_IMAGE_PATH + INPUT_IMAGE_FILENAME

#output images
OUTPUT_IMAGE_PATH = 'C:/Users/domim/OneDrive/Desktop/bilder/neu/'
OUTPUT_IMAGE_FILENAME_1 = 'transformed1.jpg'
OUTPUT_IMAGE_PATH_FILENAME_1 = OUTPUT_IMAGE_PATH + OUTPUT_IMAGE_FILENAME_1

OUTPUT_IMAGE_FILENAME_2 = 'transformed2.jpg'
OUTPUT_IMAGE_PATH_FILENAME_2 = OUTPUT_IMAGE_PATH + OUTPUT_IMAGE_FILENAME_2


OUTPUT_IMAGE_FILENAME_7 = 'transformed3.jpg'
OUTPUT_IMAGE_PATH_FILENAME_7 = OUTPUT_IMAGE_PATH + OUTPUT_IMAGE_FILENAME_7


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
background_image = np.zeros([original_image.shape[0],original_image.shape[1], 1], dtype=np.uint8)
background_image = cv2.cvtColor(background_image, cv2.COLOR_GRAY2BGR )
background_image[: ] = (0,0,255)

def equalize_clahe_color_hsv(img, cliplimit):
    """Equalize the image splitting it after conversion to HSV and applying CLAHE
    to the V channel and merging the channels and convert back to BGR
    """

    cla = cv2.createCLAHE(clipLimit=cliplimit)
    H, S, V = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
    eq_V = cla.apply(V)
    eq_image = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2BGR)
    return eq_image



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

    ax = plt.subplot(1, 3, pos)
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


def get_position_to_draw(text, point, font_face, font_scale, thickness):
    """Gives the coordinates to draw centered"""

    text_size = cv2.getTextSize(text, font_face, font_scale, thickness)[0]
    text_x = point[0] - text_size[0] / 2
    text_y = point[1] + text_size[1] / 2
    return round(text_x), round(text_y)

def sort_contours_size(cnts):
    """Sort contours based on the size"""

    cnts_sizes = [cv2.contourArea(contour) for contour in cnts]
    (cnts_sizes, cnts) = zip(*sorted(zip(cnts_sizes, cnts)))
    return cnts_sizes, cnts

## make image brighter
M = np.ones(original_image.shape, dtype="uint8")
M = np.ones(original_image.shape, dtype="uint8")*60  
  
added_image_60 = cv2.add(original_image, M)


M = np.ones(original_image.shape, dtype="uint8")*30    
added_image_30 = cv2.add(original_image, M)


M = np.ones(original_image.shape, dtype="uint8")*15    
added_image_15 = cv2.add(original_image, M)

M = np.ones(original_image.shape, dtype="uint8")*10    
added_image_10 = cv2.add(original_image, M)

M = np.ones(original_image.shape, dtype="uint8")*5    
added_image_5 = cv2.add(original_image, M)

#old appoaches
hist_original = hist_color_img(original_image)

image_equalized_3_channels = equalize_hist_color(original_image)
hist_image_eq = hist_color_img(image_equalized_3_channels)


hsv_equalized_image = equalize_hist_color_hsv(original_image)


image_clahe_color_hsv = equalize_clahe_color_hsv(original_image, 400)

image_clahe_color_hsv_added_60 = equalize_clahe_color_hsv(added_image_60, 400)
image_clahe_color_hsv_added_30 = equalize_clahe_color_hsv(added_image_30, 400)
image_clahe_color_hsv_added_15 = equalize_clahe_color_hsv(added_image_15, 400)
image_clahe_color_hsv_added_10 = equalize_clahe_color_hsv(added_image_10, 400)

### best clahe
image_clahe_color_hsv_added_5 = equalize_clahe_color_hsv(added_image_5, 400)
hist_image_clahe_color_hsv_added_5 = hist_color_img(image_clahe_color_hsv_added_5)

## inRange for best clahe
# define range of blue color in HSV

'''
Stallgang: RGB= 75, 45, 21
Pfosten: RGB = 99, 63, 51
Stroh: RGB = 222, 167, 77
cow_RGB = np.uint8([[[227, 194, 89]]])
cow_RGB2 =  = np.uint8([[[163, 89, 52]]])
cow_RGB2 =  = np.uint8([[[163, 89, 52]]]) 
'''
cow_RGB = np.uint8([[[227, 194, 89]]])
cow_RGB2 = np.uint8([[[163, 89, 52]]]) 
cow_RGB3 = np.uint8([[[89, 56, 41]]]) 
cow_RGB4 = np.uint8([[[34, 25, 20]]]) 


print('RGB3' + str(cow_RGB3))
floor_rgb = np.uint8([[[16, 15, 13]]])
pole_rgb = np.uint([[[99, 63, 51]]])
straw_rgb = np.uint([[[222, 167, 77]]])
light_rgb = np.uint8([[[245, 249, 252]]])

print('RGB: ' + str(cow_RGB))
floor_HSV = cv2.cvtColor(floor_rgb,cv2.COLOR_RGB2HSV)
print('fllo' + str(floor_HSV))

cow_HSV =cv2.cvtColor(cow_RGB,cv2.COLOR_RGB2HSV)
cow_HSV_2 =cv2.cvtColor(cow_RGB2,cv2.COLOR_RGB2HSV)
cow_HSV_3 =cv2.cvtColor(cow_RGB3,cv2.COLOR_RGB2HSV)
cow_HSV_3 =cv2.cvtColor(cow_RGB3,cv2.COLOR_RGB2HSV)

dark_cow = cv2.cvtColor(cow_RGB4,cv2.COLOR_RGB2HSV)
print('dark:')
print(dark_cow )
#floor_lower_range = 

RANGE = 50

##### COLORS BELONGING TO THE COW #####
#Bright skin
cow_upper_HSV_brightskin = np.array([73,205,139])
cow_lower_HSV_brightskin = np.array([-47, 105, 39])

#Dark Skin RANGES
cow_upper_HSV_darkskin = np.array([31,135,64])
cow_lower_HSV_darkskin = np.array([-19,75,15])

##### COLORS NOT BELONGING TO THE COW #####

#Light 
lower_HSV_light = np.array([0,0,140])
upper_HSV_light = np.array([360,100,255])

#floor
lower_HSV_floor = np.array([0,0,0])
upper_HSV_floor = np.array([360,100,90])




hsv = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV ) 
equalized= equalize_clahe_color_hsv(hsv, 4.0)
filtered = cv2.GaussianBlur(hsv, (9  ,9), 0)

# Threshold the HSV image-_> inrange macht alles weiss, was in der Range ist und alles schwarz was ausserhalb ist
#positives
mask_darkskin = cv2.inRange(filtered, cow_lower_HSV_darkskin , cow_upper_HSV_darkskin)
mask_brightskin = cv2.inRange(filtered, cow_lower_HSV_brightskin , cow_upper_HSV_brightskin)


#negatives
mask_light = cv2.inRange(filtered, lower_HSV_light , upper_HSV_light)
mask_floor = cv2.inRange(filtered, lower_HSV_floor , upper_HSV_floor)

#put negatives together
negative_masks = cv2.bitwise_or(mask_light,mask_floor, mask=None)
negative_bg = cv2.bitwise_and(filtered,background_image, mask=negative_masks)

possible_cow_area_mask = cv2.bitwise_not(negative_masks)
possible_cow_area = cv2.bitwise_and(filtered, filtered, mask=possible_cow_area_mask)

possible_cow_area_bg = cv2.bitwise_and(filtered, filtered, mask=possible_cow_area_mask)

not_cow_light = cv2.bitwise_and(filtered,background_image, mask=mask_light)
not_cow_floor = cv2.bitwise_and(filtered,background_image, mask=mask_floor)

# Bitwise-AND mask and original image --> das führt dazu, dass alles was nach inRange weiss war nun wieder die richtige Farbe hat und alles andere schwarz ist
resulting_mask=cv2.bitwise_or(mask_darkskin,mask_brightskin, mask=None)
resulting_image=cv2.bitwise_and(filtered,background_image, mask=resulting_mask)


cannycontoures = cv2.Canny(original_image,10, 250)          
# Equalize the image and calculate histogram:
show_hist_with_matplotlib_rgb(hist_original, "color histogram", 1, ['b', 'g', 'r'])
show_hist_with_matplotlib_rgb(hist_image_clahe_color_hsv_added_5, "color histogram equalized", 3, ['b', 'g', 'r'])


grayscaled = cv2.cvtColor(image_clahe_color_hsv, cv2.COLOR_BGR2GRAY )
grayscaled = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY ) 
 
filtered = cv2.GaussianBlur(grayscaled, (9  ,9), 0)

#thresholded = cv2.adaptiveThreshold(filtered , 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 3)

# eher gut
#thresholded  = cv2.adaptiveThreshold(filtered , 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 3) 
rect, thresholded = cv2.threshold(possible_cow_area , 40, 255, cv2.THRESH_BINARY) 
#rect, thresholded  = cv2.threshold(filtered , 0, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)




#thresholded = cv2.Canny(grayscaled,20,55)
# retr extrenal meist nicht gut.

contours, hierarchy = cv2.findContours(thresholded, cv2.RETR_CCOMP , cv2.CHAIN_APPROX_SIMPLE )
contours2, hierarchy2 = cv2.findContours(thresholded, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contours3, hierarchy3 = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#cannycontoures, hierarchy4 = cv2.findContours(cannycontoures, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)


# Show the number of detected contours for each call:
number_detected_contours = format(len(contours))
number_detected_contours2 = format(len(contours2))

print("detected contours (RETR_LIST): '{}' ".format(len(contours)))
print("detected contours (RETR_LIST): '{}' ".format(len(contours2)))
# Copy image to show the results:
image_contours = equalize_clahe_color_hsv(added_image_5, 4.0).copy()
image_contours_2 = equalize_clahe_color_hsv(added_image_5, 4.0).copy()
image_contours_3 = equalize_clahe_color_hsv(added_image_5, 4.0).copy()
image_contours_4 = equalize_clahe_color_hsv(added_image_5, 4.0).copy()
image_contours_5 = equalize_clahe_color_hsv(added_image_5, 4.0).copy()
image_contours_6 = equalize_clahe_color_hsv(added_image_5, 4.0).copy()
image_contours_7 = equalize_clahe_color_hsv(added_image_5, 4.0).copy()


# Draw the outline of all detected contours:

draw_contour_outline(image_contours, contours, (0, 0,255 ), 2)
draw_contour_outline(image_contours_2, contours2, (0, 0, 255), 2)
draw_contour_outline(image_contours_3, contours3, (0, 0, 255), 2)



bigContures = []

"""Sort contours based on the size"""
for contour in contours:
    conturarea = int(cv2.contourArea(contour))
    if conturarea > 4000:
        bigContures.append(contour)
    #print(conturarea)
    #if conturarea > 20:
    
for bigContur in bigContures:
    #print(bigContur)
    a=bigContur



"""Sort contours based on the size"""
bigContures2 = []

for contour in contours2:
    conturarea = int(cv2.contourArea(contour))
    if conturarea > 4000:
        bigContures2.append(contour)
    #print(conturarea)
    #if conturarea > 20:
    
for bigContur in bigContures2:
    #print(bigContur)
    a=bigContur


"""Sort contours based on the size"""
bigContures3 = []

for contour in contours3:
    conturarea = int(cv2.contourArea(contour))
    if conturarea > 4000:
        bigContures3.append(contour)
    #print(conturarea)
    #if conturarea > 20:
    
for bigContur in bigContures3:
    #print(bigContur)
    a=bigContur




number_detected_contours3 = format(len(bigContures))
number_detected_contours4 = format(len(bigContures2))

draw_contour_outline(image_contours_4, bigContures, (0, 0,255 ), 2)
draw_contour_outline(image_contours_5, bigContures2, (0, 0, 255), 2)
draw_contour_outline(image_contours_6, bigContures3, (0, 0, 255), 2)

#draw_contour_outline(image_contours_7, bigContures4, (0, 0, 255), 2)

# Plot the image

#draw_contour_points(image_contours, contours, (255, 0, 0))
#draw_contour_points(image_contours_2, contours2, (255,0 , 0))




## DISPLAY IMAGE WITH MATLLIB ##
# Create the dimensions of the figure and set title:
'''
fig = plt.figure(figsize=(20, 20))
plt.suptitle("Find Conturs in Cow: Preprocessing Steps", fontsize=14, fontweight='bold')
fig.patch.set_facecolor('silver')

ax = plt.subplot(10, 2, 1)
plt.imshow(original_image,)
plt.title('Original Image')
plt.axis('off')

ax = plt.subplot(10, 2, 2)
plt.imshow(added_image_10,)
plt.title('added_image')
plt.axis('off')

ax = plt.subplot(10, 2, 3)
plt.imshow(hsv_equalized_image, cmap='hsv')
plt.title('Equalized Image (hsv)')
plt.axis('off')

ax = plt.subplot(10, 2, 4)
plt.imshow(hsv_equalized_image)
plt.title('image_clahe_color_hsv')
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
plt.title('cv2.RETR_CCOMP: Number of Detected Contours: ' + number_detected_contours)
plt.axis('off')


ax = plt.subplot(1, 2, 2)
plt.imshow(image_contours_2)
plt.title('Grayscale: cv2.RETR_LIST Number of Detected Contours: ' + number_detected_contours2)
plt.axis('off')
plt.show()




fig = plt.figure(figsize=(20, 8))
plt.suptitle("Find Big Conturs in Cow: Result Comparison", fontsize=14, fontweight='bold')
fig.patch.set_facecolor('silver')

ax = plt.subplot(1, 2, 1)
plt.imshow(image_contours_3)
plt.title('cv2.RETR_CCOMP: Number of Detected Contours: ' + number_detected_contours3)
plt.axis('off')


ax = plt.subplot(1, 2, 2)
plt.imshow(image_contours_4)
plt.title('Grayscale: cv2.RETR_LIST Number of Detected Contours: ' + number_detected_contours4)
plt.axis('off')
plt.show()


'''

#SAVE THE IMAGE#

cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_1, image_contours)
cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_2, image_contours_2)
cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_7, image_contours_3)

cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_3, original_image)
cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_4, grayscaled)
cv2.imwrite(OUTPUT_IMAGE_PATH_FILENAME_5, thresholded)


cv2.imwrite(OUTPUT_IMAGE_PATH + 'original.jpg', original_image)
cv2.imwrite(OUTPUT_IMAGE_PATH + 'zzz_best_clahe.jpg', image_clahe_color_hsv_added_5)


cv2.imwrite(OUTPUT_IMAGE_PATH + 'zzz_mask_darkskin.jpg', mask_darkskin)
cv2.imwrite(OUTPUT_IMAGE_PATH + 'zzz_mask_brightskin.jpg', mask_brightskin)
cv2.imwrite(OUTPUT_IMAGE_PATH + 'zzz_mask_light.jpg', mask_light)



cv2.imwrite(OUTPUT_IMAGE_PATH + 'cannycontoures.jpg', image_contours_7)

cv2.imwrite(OUTPUT_IMAGE_PATH + 'zzzzzz_resulting_mask.jpg', resulting_mask)



cv2.imwrite(OUTPUT_IMAGE_PATH + 'Big_area_RETR_CCOMP1.jpg', image_contours_4)
cv2.imwrite(OUTPUT_IMAGE_PATH + 'Big_Area_RETR_LIST2.jpg', image_contours_5)
cv2.imwrite(OUTPUT_IMAGE_PATH + 'Big_Area_RETR_External.jpg', image_contours_6)



cv2.imwrite(OUTPUT_IMAGE_PATH + 'zzzz_ts.jpg', background_image)
not_cow_ligh =  cv2.cvtColor(not_cow_light, cv2.COLOR_HSV2BGR)
cv2.imwrite(OUTPUT_IMAGE_PATH + 'aa_notcow__light.jpg', not_cow_light)

not_cow_floor= cv2.cvtColor(not_cow_floor, cv2.COLOR_HSV2BGR)
cv2.imwrite(OUTPUT_IMAGE_PATH + 'aa_notcow__floor.jpg', not_cow_floor)

cv2.imwrite(OUTPUT_IMAGE_PATH + 'aaa_negativ_masks.jpg', negative_masks)

negative_bg= cv2.cvtColor(negative_bg, cv2.COLOR_HSV2BGR)
cv2.imwrite(OUTPUT_IMAGE_PATH + 'aaa_negativ_bg.jpg', negative_bg)

possible_cow_area= cv2.cvtColor(possible_cow_area, cv2.COLOR_HSV2BGR)
cv2.imwrite(OUTPUT_IMAGE_PATH + 'aaa_possible_area.jpg', possible_cow_area)

possible_cow_area_bg= cv2.cvtColor(possible_cow_area_bg, cv2.COLOR_HSV2BGR)
cv2.imwrite(OUTPUT_IMAGE_PATH + 'aaa_possible_area_bg.jpg', possible_cow_area_bg)


cv2.imwrite(OUTPUT_IMAGE_PATH + 'aaa_possible_area_mask.jpg', possible_cow_area_mask)





resulting_image = cv2.cvtColor(resulting_image, cv2.COLOR_HSV2BGR )
cv2.imwrite(OUTPUT_IMAGE_PATH + 'zzzz_destruktiv.jpg', resulting_image)


