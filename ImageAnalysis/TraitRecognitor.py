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

WARNING_MSG = 'PAY ATTENTION! MORE THAN 1 CONTURE DETECTED AS LIGHT CONTUR'

MEASURED_LIGHT_BULB_ANGLE_TITLE = 'MEASURED ANGLE OF THE LIGHT BULB: '
EXPECTED_LIGHT_BULB_REAL_LIFE_ANGLE_TITLE = 'EXPECTED ANGLE OF THE LIGHT BULB IN REAL LIFE: '

ANGLE_ANALYSIS_TITLE = '############ Angle Analysis ############'
NEWLINE = '\n' 
ADJUSTED_ROTATION_ANGLE_TITILE = 'IMAGE ROTATION ANGLE: '
ADJUSTED_ANGLE_TITILE = 'MEASURED ANGLE AFTER ADJUSTMENT: '
MIN_ECCENTRICITY = 0.9


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
        lateralLyingContours = []
        image = originalImage
        angle = 0

        print(ANGLE_ANALYSIS_TITLE + NEWLINE + NEWLINE)

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
                    print(MEASURED_LIGHT_BULB_ANGLE_TITLE + str(angle))
                else:
                    angle = angle + angle
                    print(WARNING_MSG)

        # rotate the image using the light bulb as reference.
         
        print(EXPECTED_LIGHT_BULB_REAL_LIFE_ANGLE_TITLE + str(ImageAnalysisConfiguration.LIGHT_BULB_ANGLE_EXPECTION))
        
        rotationAngle =angle-ImageAnalysisConfiguration.LIGHT_BULB_ANGLE_EXPECTION
        print(ADJUSTED_ROTATION_ANGLE_TITILE + str(rotationAngle))

        (h, w) = originalImage.shape[:2]     
        imageCenter = (w / 2, h / 2)       
        M = cv2.getRotationMatrix2D(imageCenter, rotationAngle, ImageAnalysisConfiguration.SCALE)
        rotatedImage = cv2.warpAffine(originalImage, M, (h, w))
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/contoursAllpox.jpg', rotatedImage)
 
        
        #image = cv2.cvtColor(rotatedImage, cv2.COLOR_HSV2BGR)
    

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
            print(adjustedAngle)    
   
            if adjustedAngle > minLegAngle and adjustedAngle < maxLegAngle:
                filteredByAngle.append(contour)
        print(len(filteredByAngle))

        minAreaRect_image = originalImage.copy()
        i = 0      
        for contour in contours:
            i = i+1
            #### ASPECT RATIO COMPUTATION #### 
            
            # calculate the rectangle with minimal area around the contour
            rotated_rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rotated_rect)
            box = np.int0(box)
            cv2.polylines(minAreaRect_image, [box], True, (	0,0,0), 5)
            
            # compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio           
            x,y,w,h = cv2.boundingRect(contour )
            aspectRatio = float(w)/h  
            
            
            #### EXTEND COMPUTATION ####
            contourArea = cv2.contourArea(contour)
            rectArea = w*h
            extent = float(contourArea)/rectArea
            print('################' +str(i)+'##########################')
            print(contourArea)
            print(rectArea)
            print(extent)
            print(aspectRatio)
            #### FILTER THE CONTOURS BASED ON ASPECT RATIO AND EXTEND ####
            aspectRatioMin = ImageAnalysisConfiguration.ASPECT_RATIO_MIN
            extentMax = ImageAnalysisConfiguration.EXTENT_MAX

            if aspectRatio > aspectRatioMin and extent < extentMax:
                lateralLyingContours.append(contour)


        # draw the minArea Rectangles in the Image and write it
        
        #draw all the contours in the image
        originalImage = cv2.drawContours(minAreaRect_image, contours, -1, (	120, 200, 120), -1)

        #draw only the filtered contours in the image
        originalImage = cv2.drawContours(minAreaRect_image, lateralLyingContours, -1, (	0, 0,255), -1)
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/filtered.jpg', minAreaRect_image)
 
        return (lateralLyingContours, minAreaRect_image)         
       
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

