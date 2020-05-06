#!/usr/bin/env python3
#-*- coding: utf-8 -*-



#==========================================================================
# ImageProcessor.py – DESCRIPTIONS 
#==========================================================================

"""
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>
"""


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================


import cv2 
import numpy as np

import ImageWriter
import ContourDrawer
import ContourFinder
import ImageAnalysisController

import sys
sys.path.append('../VO-Library')
import ColorSpaceConversion
import ColorSpaceConversionType
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



class TraitRecognitor:
    
    """
    A class used to represent and implement the functionality for the Trait Recognition of Cows.
    ...
    
    Attributes
    ----------        
    standingCowIsDetected: Boolean
        Expresses, whether a standing cow is been detected     
    lateralLyingCowIsDetected: Image
       Expresses, whether a lateral lying cow is been detected     
      
    Methods - See descriptions below.
    
    -------
    detectStandingCow(self, image, contours )
    detectLateralLyingClow(self, image, contours )
    obtainStandingCowIsDetected()       
    obtainLateralLyingCowIsDetected()
    obtainTraitRecognitor()
    
    """ 
     
    def __init__(self):
        self.standingCowIsDetected = None
        self.lateralLyingCowIsDetected = None
        
        # funtion execution


    def detectStandingCow(self, contours, image,  finderConfig):
        
        """ 
       
        Analyses Image data to detect standing cow
        -------              
      
        Detects Contours in order to analyse wheter a standing cow is in the image.
        -------              
      
        Parameters: 
        -------                 
        contours : Contours detected by findContours()

        
        Returns: 
        -------              
        contours which are the foundation of the decision
        """              
        
        
       

    def detectLateralLyingClow(self, contours, originalImage,  finderConfig ):
        
        """ 
       
        Analyses Image data to detect a cow in lateral lying position
        -------              
      
        Detects Contours in order to analyse wheter a cow in in lateral lying position, which is a sign
        for an ongoing or imminent birth.
        -------              
      
        Parameters: 
        -------                 
        contours : Contours detected by findContours()

        
        Returns: 
        -------              
        contours which are the foundation of the decision
        """          
        
        filteredByAngle = []
        lightBulbContours = []
        filteredlightBulbsByArea = []
        filteredlightBulbsByAngle = []
        image = originalImage
        angle = 0

        # generate mask to show where in the image the light is situated
        lowerBound = ImageAnalysisConfiguration.LOWER_BOUND_LIGHT.obtainColor()
        upperBound = ImageAnalysisConfiguration.UPPER_BOUND_LIGHT.obtainColor()
        image = cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV)
        
        lightBulb = cv2.inRange(image, lowerBound , upperBound)
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/masks.jpg', lightBulb)
        
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
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/contoursAllpox.jpg', rotatedImage)
 
        

        
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
    
        print(len(contours))
           
        print(len(filteredByAngle))

        return (filteredByAngle)         


    def obtainStandingCowIsDetected(self ):
        

        """ 
       
        Returns wheter standing Cow is been detected by last analysis (without executing analysis again) 
        ----------        
              
        Returns: 
        ----------                
        Boolean to express whether standing cow is in the image
. 
      
        """         
        return self.standingCowIsDetected

    def obtainLateralLyingCowIsDetected(self, ):
        """ 
       
        Returns wheter lateral lying Cow is been detected by last analysis (without executing analysis again) 
        ----------        
              
        Returns: 
        ----------                
        Boolean to express whether lateral lying cow is in the image or not.
      
        """        
        return self.lateralLyingCowIsDetected


    def obtainTraitRecognitor(self, ):
      
        """ 
       
        Returns general Information about Trait Recognition
        ----------        
              
        Returns: 
        ----------                
        String. 
              
        """
        
        pass

