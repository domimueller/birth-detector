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
import ImageAnalysisConfiguration
import math
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
        filteredContours = []
        for contour in contours:
            
            conturArea = cv2.contourArea(contour)
            
            # if circles dont have to be ignored, check for minArea and then add contour to the list conturArea >= minArea
            if finderConfig.obtainDeleteCircles() == False and conturArea >= finderConfig.obtainMinArea():
                
                filteredContours.append(contour)
            
            # if circles have to be ignored, only add them to the list if contour is no circle and conturArea >= minArea 
            if finderConfig.obtainDeleteCircles() == True and conturArea >= finderConfig.obtainMinArea():
                
                # Calculate image moments of the detected contour
                moments = cv2.moments(contour)
                
                # determine eccentricity according to the book "Mastering OpenCV 4 with Python" written by Alberto Fernández Villán 
                a1 = (moments['mu20'] + moments['mu02']) / 2
                a2 = np.sqrt(4 * moments['mu11'] ** 2 + (moments['mu20'] - moments['mu02']) ** 2) / 2
                eccentricity  = np.sqrt(1 - (a1 - a2) / (a1 + a2))                
                
                               
                if eccentricity  > ImageAnalysisConfiguration.ROUNDNESS_THRESHOLD:
                    filteredContours.append(contour)
            
            
                    
            #this image will now be our processingImage                
            processingImage = originalImage
            
            
        return (filteredContours, processingImage)

    def contourAngleFiltering(self, contours, originalImage, finderConfig ):
        filteredByAngle = []
        lightBulbContours = []
        filteredlightBulbsByArea = []
        filteredlightBulbsByAngle = []
        image = originalImage
        

        # generate mask to show where in the image the light is situated
        lowerBound = ImageAnalysisConfiguration.LOWER_BOUND_LIGHT.obtainColor()
        upperBound = ImageAnalysisConfiguration.UPPER_BOUND_LIGHT.obtainColor()
        image = cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV)
        
        lightBulb = cv2.inRange(image, lowerBound , upperBound)
        
        #derive contours from mask of lightning 
        lightBulbContours, hierachy = cv2.findContours( lightBulb, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE );
       
        
        image = cv2.cvtColor(originalImage, cv2.COLOR_HSV2BGR)

        
        # filter contours from lightning mask by area size        
        for contour in lightBulbContours:
            conturArea = cv2.contourArea(contour)
            
            if conturArea >= finderConfig.obtainMinArea():

                filteredlightBulbsByArea.append(contour)             
       

        for lightBulb in filteredlightBulbsByArea:
                             
                #  Ma and ma are Major Axis and Minor Axis lengths. angle ist orientation of Ellipse
                (x,y),(MA,ma),angle = cv2.fitEllipse(lightBulb) 
                
                if int(len(filteredlightBulbsByArea)) == 1:
                    angle = angle
                    print('Gemessener Winkel Lampe: ' + str(angle))
                else:
                    angle = angle + angle
                    print(ERROR_MSG)

        # rotate the image using the light bulb as reference.

        print('Vermutung des Winkels der Lampe')
        print(ImageAnalysisConfiguration.LIGHT_BULB_ANGLE_EXPECTION)
        rotationAngle =angle-ImageAnalysisConfiguration.LIGHT_BULB_ANGLE_EXPECTION
        print('Berechneter Winkel zur verschiebung des Bilds')
        print(rotationAngle)
        #rotationAngle = 45
        (h, w) = originalImage.shape[:2]     
        imageCenter = (w / 2, h / 2)       
        M = cv2.getRotationMatrix2D(imageCenter, rotationAngle, ImageAnalysisConfiguration.SCALE)
        rotatedImage = cv2.warpAffine(originalImage, M, (h, w))
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/contoursAllpox.png', rotatedImage)
        
        #image = cv2.cvtColor(rotatedImage, cv2.COLOR_HSV2BGR)
    
        print('Adjusted Measured Angle')
        print(rotationAngle)
        
        print('Adjusted Calculated Angle')

        filteredByAngle = []
        for contour in contours:
          
            
            ## contour Approximation to a Polynon
            peri = cv2.arcLength(contour, True)
            contourApprox = cv2.approxPolyDP(contour, 0.004 * peri, True)
           
            #  Ma and ma are Major Axis and Minor Axis lengths. angle ist orientation of Ellipse
            (x,y),(MA,ma),angle = cv2.fitEllipse(contourApprox)          
            
            adjustedAngle = angle - ImageAnalysisConfiguration.LIGHT_BULB_ANGLE_EXPECTION 
            minLegAngle = ImageAnalysisConfiguration.MIN_LEG_ANGLE_EXPECTION
            maxLegAngle = ImageAnalysisConfiguration.MAX_LEG_ANGLE_EXPECTION

            if adjustedAngle > minLegAngle and adjustedAngle < maxLegAngle:
                filteredByAngle.append(contour)

        return (filteredByAngle, lightBulb)

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
