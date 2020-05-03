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

    def findContours(self, processingImage, originalImage):
        

        contours, hierarchy = cv2.findContours(processingImage, cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE )
        contours, processingImage = self.filterContours(contours, processingImage, originalImage)
        return (contours, processingImage)

    def filterContours(self, contours, processingImage, originalImage ):
        
        filteredContours = []
        for contour in contours:
            
            conturArea = int(cv2.contourArea(contour))
            
            # only contourArea > 200px considered to remove noise
            if conturArea >200:
                # draw minimal circle around contour
                
                (x,y),radius = cv2.minEnclosingCircle(contour)
                center = (int(x),int(y))
                radius = int(radius)
                # draw the circles in the originalImage, not the processing image (which is binary!).
                cv2.circle(originalImage,center,radius,(0,0,0),-1)
                
                #this image will now be our processingImage                
                processingImage = originalImage
                
        return (filteredContours, processingImage)

    def countAllContours(self, contours):
        pass

    def countRelevantContours(self, filteredContours):
        pass

