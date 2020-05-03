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

MIN_AREA = 200
# Configuration for Console Output
TITLE = '############ NUMBER OF DETECTED CONTOURS ############'
DELIMITER = '; '
NEWLINE = '\n'


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
        
        """ 
       
        Finds Contours in an Image.
        -------              
      
        This function is based on the library OpenCV and the corresponding function cv2.findContours.
        -------              
      
        Parameters: 
        -------                 
        processingImage (Image): Image to use for Contour Finding
        originalImage (Image): Image to pass to filterContours() for Contour Drawing. 

        
        Returns: 
        -------              
        contours (Contour): contours found
        processingImage (Image): Image for further processing
        
        """          

        contours, hierarchy = cv2.findContours(processingImage, cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE )
        
        contours, processingImage = self.filterContours(contours, processingImage, originalImage)
        
        return (contours, processingImage)

    def filterContours(self, contours, processingImage, originalImage ):
        
        """ 
       
        Filters Contours of an Image.
        -------              
      
        This function is based on the library OpenCV and the corresponding function cv2.contourArea.
        -------              
      
        Parameters: 
        -------                 
        contours (Contour): contours found retrieved from findContours()
        processingImage (Image): Image to use for Contour Filtering and Application
        originalImage (Image): Image for Contour Drawing. 

        
        Returns: 
        -------              
        contours (Contour): contours found
        processingImage (Image): Image for further processing
        
        """   
                  
        filteredContours = []
        for contour in contours:
            
            conturArea = int(cv2.contourArea(contour))
            
            # only contourArea > MIN_AREA considered to remove noise
            if conturArea > MIN_AREA:
                
                filteredContours.append(contour)
                
                #this image will now be our processingImage                
                processingImage = originalImage
                
        return (filteredContours, processingImage)

    def countContours(self, contours):
        
        """ 
       
        Counts number of detected contours.
        -------              
      
        Counts number of detected contours, returns it and prints it to the console.
        -------              
      
        Parameters: 
        -------                 
        contours (Contour): contours found retrieved from findContours()
 

        
        Returns: 
        -------              
        contourAmount (int):  number of detected contours
        
        """          
        contourAmount = format(len(contours))
        
        str = TITLE + NEWLINE + contourAmount  + NEWLINE
        print(str)
        
        return contourAmount
