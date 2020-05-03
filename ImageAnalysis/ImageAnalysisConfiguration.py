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
WRITER_FILE_NAME_BRIGHTENED = 'brightenedImage'
WRITER_FILE_NAME_FILTERED = 'filteredImage'
WRITER_FILE_NAME_UNIMPORTANT_AREAS_MASK = 'unimportantAreaMask'
WRITER_FILE_NAME_UNIMPORTANT_AREAS_IMAGE = 'unimportantAreaimage'
WRITER_FILE_NAME_THRESHOLDED_IMAGE = 'thresholdedImage'


#==========================================================================
# INFORMATION AND CONFIGURATION FOR IMAGE PROCESSOR
#==========================================================================


#============================================
###### BRIGHTENING CONFIGURATION ######
#============================================
   
# Brighten Configuration #
BRIGHTENING_IMAGE = True
BRIGHTENER_FACTOR = 60
EQUALIZING_IMAGE = True
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

THRESHOLDING_IMAGE = True
MAXIMUM_VALUE = 255 # value between 0 and 255 possible
THRESHOLD = 40

## Thresholding Method Enumeration
'''
    Possible Values for  ENUM_SELECT_METHOD:
    - 1 corresponds to THRESHOLD
    - 2 corresponds to ADAPTIVE_THRESHOLD
    

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
'''
ENUM_SELECT_TYPE = 2

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

#freestyle (HSV) 
LOWER_BOUND_fr= HSV.HSV(hue=0, saturation=0, value=-100) 
UPPER_BOUND_fr = HSV.HSV(hue=360, saturation=200, value=90)


# Color Ranges
lightColorRange = ColorRange.ColorRange(lowerBound = LOWER_BOUND_LIGHT, upperBound=UPPER_BOUND_LIGHT )
floorColorRange = ColorRange.ColorRange(lowerBound = LOWER_BOUND_FLOOR, upperBound=UPPER_BOUND_FLOOR )



#============================================
###### IMPORTANT AREAS CONFIGURATION ######
#============================================

# Important Areas Configuration



#============================================
###### DRAWING CONFIGURATION ######
#============================================

CIRCLE_DRAWING_MODE = 'CIRCLE'
OUTLINE_DRAWING_MODE = 'OUTLINE'
POINTS_DRAWING_MODE = 'POINTS'