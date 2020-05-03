#!/usr/bin/python
#-*- coding: utf-8 -*-

#==========================================================================
# ContourDrawer.py – DESCRIPTIONS 
#==========================================================================

"""
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>
"""


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================
import cv2 
import numpy as np

#==========================================================================
# CONSTANTS
#==========================================================================


#==========================================================================
# FUNCTIONS
#==========================================================================

class ContourFinder:
    
    """
    A class used to Find and Filter Contours in an Image.
    ...
    
    Attributes
        ----------        
    finderConfig: FinderConfig
        configuration for finding and filtering contours     

    Methods - See descriptions below.
    -------
    findContours(img, cnts, color, thickness=1)
    filterContours(img, cnts, color) 
    countAllContours()
    countRelevantContours()
    """ 
        
    def __init__(self):
        self.finderConfig = None

    def findContours(self, processingImage):
        
        processingImage = cv2.cvtColor(processingImage, cv2.COLOR_BGR2GRAY)            

        contours, hierarchy = cv2.findContours(processingImage, cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE )
        return contours
    
    def filterContours(self, contours ):
        filteredcontours = []
        for contour in contours:
            conturarea = int(cv2.contourArea(contour))
            if conturarea > 500:
                approx = cv2.approxPolyDP(contour,55, True)
                #not_cow_area_approx = contour
                filteredcontours.append(approx)

    def countAllContours(self, contours):
        pass

    def countRelevantContours(self, filteredContours):
        pass

