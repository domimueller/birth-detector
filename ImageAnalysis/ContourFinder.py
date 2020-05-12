#!/usr/bin/python
#-*- coding: utf-8 -*-

#==========================================================================
# ContourFinder.py – DESCRIPTIONS 
#==========================================================================

"""
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>
"""


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================
import cv2 
import numpy as np
import ImageAnalysisConfiguration

#==========================================================================
# CONSTANTS
#==========================================================================

# Configuration for Console Output
TITLE = 'NUMBER OF DETECTED CONTOURS: '
DELIMITER = '; '
NEWLINE = '\n'

ERROR_MSG = 'PAY ATTENTION! MORE THAN 1 CONTURE DETECTED AS LIGHT CONTUR'


ADJUSTED_ANGLE_TITILE = 'MEASURED ANGLE AFTER ADJUSTMENT'
ADJUSTED_ANGLE_TITILE = 'MEASURED ANGLE AFTER ADJUSTMENT'

# MOMENT CONFIGURATION
MU20 = 'mu20'
MU02 = 'mu02'
MU11 = 'mu11'
  

#==========================================================================
# FUNCTIONS
#==========================================================================

class ContourFinder:
    
    """
    A class used to Find and Pre-Filter Contours
    ...
    
    Attributes
    ----------        
    finderConfig: FinderConfig
        configuration for finding and Pre-Filtering contours     

    Methods - See descriptions below.
    -------
    findContours(img, cnts, color, thickness=1)
    filterContours(img, cnts, color) 
    countContours()
    """ 
        
    
    def __init__(self):
        self.finderConfig = None

    def findContours(self, processingImage, originalImage, finderConfig):
        
        """ 
       
        Finds Contours in an Image.
        -------              
      
        This function is based on the library OpenCV and the corresponding function cv2.findContours.
        -------              
      
        Parameters: 
        -------                 
        processingImage (Image): Image to use for Contour Finding
        originalImage (Image): Image to pass to filterContours() for Contour Drawing.
        finderConfig: (ContourFinderConfiguration)

        
        Returns: 
        -------              
        contours (Contour): contours found
        processingImage (Image): Image for further processing
        
        """           
 

        print(finderConfig.obtainContourFinderConfiguration())

        contours, hierarchy = cv2.findContours(processingImage, eval(finderConfig.obtainFinderType()) , eval(finderConfig.obtainApproxType()) )
        contours, processingImage = self.filterContours(processingImage, originalImage, finderConfig, contours)
        
        return (contours, processingImage)


    def filterContours(self,  processingImage, originalImage, finderConfig, contours):
  
        """ 
       
        Pre-Filters Contours of an Image.
        -------              
      
        This function is based on the library OpenCV and the corresponding function cv2.contourArea and cv2.moments().
        -------              
      
        Parameters: 
        -------                 
        processingImage (Image): Image to use for Contour Filtering and Application
        originalImage (Image): Image for Contour Drawing. 
        finderConfig (FinderConfig): Configuration for Conour finder and Filtering
        contours (Contour): contours found retrieved from findContours()

        
        Returns: 
        -------              
        contours (Contour): prefiltered contours 
        orignalImage (Image): Original Image
        
        """  
        
        preFilteredContours = []
        
        if len(contours) >= 1: 
            for contour in contours:
                
                conturArea = cv2.contourArea(contour)
                
                # if circles dont have to be ignored, check for minArea and then add contour to the list conturArea >= minArea
                if finderConfig.obtainDeleteCircles() == False and conturArea >= finderConfig.obtainMinArea():
                    preFilteredContours.append(contour)
                
                # if circles have to be ignored, only add them to the list if contour is no circle and conturArea >= minArea 
                if finderConfig.obtainDeleteCircles() == True and conturArea >= finderConfig.obtainMinArea():
                    
                    # Calculate image moments of the detected contour
                    moments = cv2.moments(contour)
                    
                    # determine eccentricity according to the book "Mastering OpenCV 4 with Python" written by Alberto Fernández Villán 
                    a1 = (moments[MU20] + moments[MU02]) / 2
                    a2 = np.sqrt(4 * moments[MU11] ** 2 + (moments[MU20] - moments[MU02]) ** 2) / 2
                    eccentricity  = np.sqrt(1 - (a1 - a2) / (a1 + a2))                
                                                  
                    if eccentricity  > ImageAnalysisConfiguration.ROUNDNESS_THRESHOLD:
                        preFilteredContours.append(contour)                                            
            
        return (preFilteredContours, originalImage)


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
        
        str = TITLE + contourAmount  + NEWLINE
        print(str)
        
        return contourAmount


