#!/usr/bin/python
#-*- coding: utf-8 -*-

#==========================================================================
# ImageController.py – DESCRIPTIONS 
#==========================================================================

"""
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>
"""


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================
import cv2 

#==========================================================================
# CONSTANTS
#==========================================================================


#==========================================================================
# FUNCTIONS
#==========================================================================


class ImageReader:
    def __init__(self, filePathAndName):
        self.filePathAndName = filePathAndName
        
        self.readImage( filePathAndName = filePathAndName )

    def readImage(self, filePathAndName ):
        print('hier')
        print(filePathAndName.filePathAndName())
        original_image = cv2.imread(filePathAndName.filePathAndName())
        print(original_image)


