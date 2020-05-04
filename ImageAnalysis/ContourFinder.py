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

# Configuration for Console Output
TITLE = 'NUMBER OF DETECTED CONTOURS: '
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
        
        contours, processingImage = self.filterContours(contours, processingImage, originalImage, finderConfig)
        
        return (contours, processingImage)

    def filterContours(self, contours, processingImage, originalImage, finderConfig ):
        
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
        finderConfig (FinderConfig): Configuration for Conour finder and Filtering

        
        Returns: 
        -------              
        contours (Contour): contours found
        processingImage (Image): Image for further processing
        
        """  
        i=0
        filteredContours = []
        for contour in contours:
            
            conturArea = cv2.contourArea(contour)
            
            # if circles dont have to be ignored, check for minArea and then add contour to the list conturArea >= minArea
            if finderConfig.obtainDeleteCircles() == False and conturArea >= finderConfig.obtainMinArea():
                
                filteredContours.append(contour)

            
            # if circles have to be ignored, only add them to the list if contour is no circle and conturArea >= minArea 
            if finderConfig.obtainDeleteCircles() == True and conturArea >= finderConfig.obtainMinArea():
                #print(finderConfig.obtainDeleteCircles())
                
                # Calculate image moments of the detected contour
                moments = cv2.moments(contour)
                a1 = (moments['mu20'] + moments['mu02']) / 2
                a2 = np.sqrt(4 * moments['mu11'] ** 2 + (moments['mu20'] - moments['mu02']) ** 2) / 2
                ecc = np.sqrt(1 - (a1 - a2) / (a1 + a2))                
                #print(ecc)
                
                if ecc > 0.7:
                    i=i+1
                    print(ecc)
                    filteredContours.append(contour)
                
            
            #print('amount of contours with eccentricity <= 1 ' +str(i))
            
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
        
        str = TITLE + contourAmount  + NEWLINE
        print(str)
        
        return contourAmount
