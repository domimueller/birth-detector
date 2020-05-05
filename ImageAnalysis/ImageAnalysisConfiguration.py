#!/usr/bin/env python3
#-*- coding: utf-8 -*-



#==========================================================================
# ImageAnalysisConfiguration.py – DESCRIPTIONS 
#==========================================================================

"""
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>
"""


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================

import sys
sys.path.append('../VO-Library')

## Import Value Objects
import HSV
import BGR
import ColorRange



#==========================================================================
# CONSTANTS - CONFIGURATION OF THE IMAGE ANALYSIS CONTROLLER
#==========================================================================

#============================================
###### IMAGE READER CONFIGURATION ######
#============================================

#Mimetype Information for Image Reader 
READER_MAJOR = 'image'
READER_MINOR = 'jpeg'
READER_EXTENSION = 'jpg' 

#Filepath and Filename for the Image Reader

READER_FILE_PATH = 'C:/Users/domim/OneDrive/Desktop/bilder/seitlich/'
READER_FILE_NAME = '2'

#============================================
###### IMAGE WRITER CONFIGURATION ######
#============================================
   
#Mimetype Information for Image Writer 
WRITER_MAJOR = 'image'
WRITER_MINOR = 'jpeg'
WRITER_EXTENSION = 'jpg'

# Prepare FilePaths to write . 
WRITER_FILE_PATH_MAIN = 'C:/Users/domim/OneDrive/Desktop/bilder/neuetests/'

# Prepare FileNames to write . 
WRITER_FILE_NAME_BRIGHTENED = '1_brightenedImage'
WRITER_FILE_NAME_FILTERED = '2_filteredImage'
WRITER_FILE_NAME_UNIMPORTANT_AREAS_MASK = '3_unimportantAreaMask'
WRITER_FILE_NAME_UNIMPORTANT_AREAS_IMAGE = '4_unimportantAreaimage'
WRITER_FILE_NAME_THRESHOLDED_MASK = '5_thresholdedMask'
WRITER_FILE_NAME_THRESHOLDED_IMAGE = '6_ContoursAfterThresholding'


#==========================================================================
# INFORMATION AND CONFIGURATION FOR IMAGE PROCESSOR
#==========================================================================


#============================================
###### BRIGHTENING CONFIGURATION ######
#============================================
   
# Brighten Configuration #
BRIGHTENING_IMAGE = True
BRIGHTENER_FACTOR = 60
EQUALIZING_IMAGE = False
CLIP_LIMIT = 4.0

## Equalizing Type
'''
    Possible Values for  ENUM_SELECT_EQUALIZING:
    - 1 corresponds to CLAHE

    Any other Values are not allowed and end up with an error message. 
'''
ENUM_SELECT_EQUALIZING = 1 #CLAHE



# Color Space Conversion Configuration #
CONVERTING_IMAGE = True
## Converting Type
'''
    Possible Values for  ENUM_SELECT_FILTERING:
    - 1 corresponds to COLOR_BGR2GRAY  
    - 2 corresponds to COLOR_BGR2HSV 
    - 3 corresponds to COLOR_HSV2BGR
    - 4 corresponds to COLOR_GRAY2BGR 
    - 5 corresponds to COLOR_BGR2YUV 
    - 6 corresponds to COLOR_YUV2BGR 

    Any other Values are not allowed and end up with an error message. 
'''
ENUM_SELECT_CONVERTING_BGR2GRAY = 1 #COLOR_BGR2GRAY
ENUM_SELECT_CONVERTING_BGR2HSV = 2




#============================================
###### FILTERING CONFIGURATION ######
#============================================ 
FILTER_NAME = 'GAUSSIANBLUR'
FILTERING_IMAGE = True
KERNEL_WIDTH = 9
KERNEL_LENGTH = 9

## Filtering Type
'''
    Possible Values for  ENUM_SELECT_FILTERING:
    - 1 corresponds to GAUSSIANBLUR

    Any other Values are not allowed and end up with an error message. 
'''
ENUM_SELECT_FILTERING = 1 #GAUSSIANBLUR  


#============================================
###### THRESHOLDING CONFIGURATION ######
#============================================

SIMPLE_THRESHOLD_NAME = 'cv2.THRESHOLD'
ADAPTIVE_THRESHOLD_NAME = 'cv2.ADAPTIVE_THRESHOLD'

THRESHOLDING_IMAGE = True
MAXIMUM_VALUE = 255 # value between 0 and 255 possible
THRESHOLD =90

## Thresholding Method Enumeration
'''
    Possible Values for  ENUM_SELECT_METHOD:
    - 1 corresponds to cv2.THRESHOLD
    - 2 corresponds to cv2.ADAPTIVE_THRESHOLD
    

    Any other Values are not allowed and end up with an error message. 
'''
ENUM_SELECT_METHOD = 1

 
# Thresholding Type Enumeration
'''
    Possible Values for  ENUM_SELECT_TYPE:
    - 1 corresponds to THRESH_BINARY
    - 2 corresponds to THRESH_BINARY_INV
    - 3 corresponds to THRESH_TRUNC
    - 4 corresponds to THRESH_TOZERO
    - 5 corresponds to THRESH_TOZERO_INV
    - 6 corresponds to THRESH_BINARY_AND_THRESH_OTSU 
    - 7 corresponds to THRESH_BINARY_AND_THRESH_TRIANGLE
    

    Any other Values are not allowed and end up with an error message.
    PLEASE NOTE: For adaptive Thresholding only THRESH_BINARY and THRESH_BINARY_INV are available
'''
ENUM_SELECT_TYPE = 1

#adaptive Thresholding Configuration
BLOCK_SIZE = 11
C_SUBTRACTOR = 3

'''
    Possible Values for  ENUM_SELECT_ADAPTIVE_THRESHOLDING:
    - 1 corresponds to ADAPTIVE_THRESH_MEAN_C
    - 2 corresponds to ADAPTIVE_THRESH_GAUSSIAN_C     

    Any other Values are not allowed and end up with an error message. 
''' 
ENUM_SELECT_ADAPTIVE_THRESHOLDING = 1



#============================================
###### UNIMPORTANT AREAS CONFIGURATION ######
#============================================

# light (HSV) Bounds
LOWER_BOUND_LIGHT= HSV.HSV(hue=0, saturation=0, value=140)
UPPER_BOUND_LIGHT= HSV.HSV(hue=360, saturation=100, value=255)
                           
#floor (HSV) 
LOWER_BOUND_FLOOR= HSV.HSV(hue=0, saturation=0, value=0) 
UPPER_BOUND_FLOOR = HSV.HSV(hue=360, saturation=100, value=90)


# Color Ranges
lightColorRange = ColorRange.ColorRange(lowerBound = LOWER_BOUND_LIGHT, upperBound=UPPER_BOUND_LIGHT )
floorColorRange = ColorRange.ColorRange(lowerBound = LOWER_BOUND_FLOOR, upperBound=UPPER_BOUND_FLOOR )



#============================================
###### IMPORTANT AREAS CONFIGURATION ######
#============================================

# Important Areas Configuration

#============================================
###### CONTOUR FINDER CONFIGURATION ######
#============================================

MIN_AREA = 1250
MIN_AREA_BIG = 2000

DELETE_CIRCLES_TRUE = True
DELETE_CIRCLES_FALSE = False

FILTER_BY_ANGLE_TRUE = True
FILTER_BY_ANGLE_FALSE = False


'''
    Possible Values for  ENUM_SELECT_APPROX:
    - 1 corresponds to CHAIN_APPROX_NONE
    - 2 corresponds to CHAIN_APPROX_SIMPLE
    - 3 corresponds to CHAIN_APPROX_TC89_L1
    - 4 corresponds to CHAIN_APPROX_TC89_KCOS

    

    Any other Values are not allowed and end up with an error message. 
'''
    
ENUM_SELECT_APPROX = 1

'''
    Possible Values for  ENUM_SELECT_FINDER:
    - 1 corresponds to RETR_EXTERNAL
    - 2 corresponds to RETR_LIST
    - 3 corresponds to RETR_CCOMP
    - 4 corresponds to RETR_TREE
    - 5 corresponds to RETR_FLOODFILL

        = 1

    Any other Values are not allowed and end up with an error message. 
'''
    
ENUM_SELECT_FINDER = 2

#============================================
###### CONTOUR DRAWER CONFIGURATION ######
#============================================

CIRCLE_DRAWING_MODE = 'CIRCLE'
OUTLINE_DRAWING_MODE = 'OUTLINE'
POINTS_DRAWING_MODE = 'POINTS'

THICKNESS_BOLD = 10
THICKNESS_FILL = -1
THICKNESS_THIN = 2

RED = BGR.BGR(blue=0, green=0, red=250)
BLUE= BGR.BGR(blue=255, green=0, red=0)
GREEN= BGR.BGR(blue=0, green=255, red=0)
BLACK= BGR.BGR(blue=0, green=0, red=0)


