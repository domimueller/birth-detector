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

DEGREE_MODULO = 360

ANGLE_INVERTER = -1
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
        removedContours = []
        negimg = originalImage.copy()
        newimg = originalImage.copy()
        minAreaRectImage = originalImage.copy()
        minAreaRect_image= originalImage.copy()
        image = originalImage

        lightBulbAngle = 0

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
                
                # uncomment to see how the ellipse looks like
                #img = cv2.ellipse(originalImage.copy(),(int(x),int(y)),(int(MA),int(ma)),0,0,360,(0,0,0),2) 
                
                
                if int(len(filteredlightBulbsByArea)) == 1:
                    lightBulbAngle = angle
                    print(MEASURED_LIGHT_BULB_ANGLE_TITLE + str(angle))
                                      

           
                    #  Ma and ma are Major Axis and Minor Axis lengths. angle ist orientation of Ellipse
                else:
                    lightBulbAngle = lightBulbAngle + angle
                    print(WARNING_MSG)

        # rotate the image using the light bulb as reference.
         
        print(EXPECTED_LIGHT_BULB_REAL_LIFE_ANGLE_TITLE + str(ImageAnalysisConfiguration.LIGHT_BULB_ANGLE_EXPECTION))
        
        rotationAngle =lightBulbAngle-ImageAnalysisConfiguration.LIGHT_BULB_ANGLE_EXPECTION
        
        print(ADJUSTED_ROTATION_ANGLE_TITILE + str(rotationAngle))

        (h, w) = originalImage.shape[:2]     
        imageCenter = (w / 2, h / 2)       
        M = cv2.getRotationMatrix2D(imageCenter, rotationAngle, 0.25)
        rotatedImage = cv2.warpAffine(originalImage, M, (h, w))
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/contoursAllpox.jpg', rotatedImage)
 
        
        #image = cv2.cvtColor(rotatedImage, cv2.COLOR_HSV2BGR)
        
        filteredByAngle = []
        adjustedAngleNegative = 0
        negativeRotationAngle = 0
        
        for contour in contours:
          

            ## contour Approximation to a Polynon
            peri = cv2.arcLength(contour, True)
            contourApprox = cv2.approxPolyDP(contour, 0.004 * peri, True)
           
            #  Ma and ma are Major Axis and Minor Axis lengths. angle ist orientation of Ellipse
            (x,y),(MA,ma),contourAngle = cv2.fitEllipse(contourApprox)
            
            # positive rotation values means counter-clockwise!
            
            positivRotationAngle = lightBulbAngle - ImageAnalysisConfiguration.LIGHT_BULB_ANGLE_EXPECTION
            negativeRotationAngle = lightBulbAngle - (ImageAnalysisConfiguration.LIGHT_BULB_ANGLE_EXPECTION*-1)
            positiveAdjustedAngle = (contourAngle -positivRotationAngle) % DEGREE_MODULO 
            negativeAdjustedAngle = (negativeRotationAngle + contourAngle) % DEGREE_MODULO 

            minLegAngle = ImageAnalysisConfiguration.MIN_LEG_ANGLE_EXPECTION
            maxLegAngle = ImageAnalysisConfiguration.MAX_LEG_ANGLE_EXPECTION
            
            # calculate the rectangle with minimal area around the contour
            rotated_rect = cv2.minAreaRect(contour)
            (x, y), (width, height), rotatedRectAngle = rotated_rect
    
            minAreaRect_image = negimg  
            #minAreaRect_image = cv2.rectangle(minAreaRect_image, (x,x+w),(y, y+h),(0,0,0), 5) 
            box = cv2.boxPoints(rotated_rect)
            box = np.int0(box)
            cv2.polylines(minAreaRect_image, [box], True, (0,0,0), 5)
            
            if positiveAdjustedAngle > minLegAngle and positiveAdjustedAngle < maxLegAngle:
                
                filteredByAngle.append(contour)
                continue
                        
        
            ## angle analysis for legs directing from right to left
            elif negativeAdjustedAngle > minLegAngle and negativeAdjustedAngle < maxLegAngle:

                maxLegAngle = minLegAngle*(-1)
                minLegAngle =  maxLegAngle*(-1)
                filteredByAngle.append(contour)
            else:
                  removedContours.append(contour)  


            ## angle analysis for legs directing from left to right

              
        (h, w) = negimg.shape[:2]     
        imageCenter = (w / 2, h / 2)       
        M = cv2.getRotationMatrix2D(imageCenter, negativeRotationAngle, ImageAnalysisConfiguration.SCALE)
        negimg = cv2.warpAffine(negimg, M, (h, w))
 
        print('Endresultat')
        print(len(filteredByAngle))
        
        i = 0      
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/orginal.jpg', originalImage)
        
        for contour in filteredByAngle:
            i = i+1
            #### ASPECT RATIO COMPUTATION #### 
            
            # calculate the rectangle with minimal area around the contour
            rotated_rect = cv2.minAreaRect(contour)
            (x, y), (width, height), rotatedRectAngle = rotated_rect
           
            convexHull= cv2.convexHull(contour)
            #cv2.polylines(minAreaRect_image, convexHull, False, (0,0,0), 5)
            
            #minAreaRect_image = cv2.rectangle(minAreaRect_image, (x,x+w),(y, y+h),(0,0,0), 5) 
            box = cv2.boxPoints(rotated_rect)
            box = np.int0(box)
            cv2.polylines(minAreaRect_image, [box], True, (0,0,0), 5)
            
            # compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio           


            #print('width' + str(width))
            #print('height' + str(height))
            
            # make sure that aspect ratio is greater than 0 
            if width > height:
                longside = width
                shortside = height
            else:
                longside = height
                shortside = width

            aspectRatio = float(longside)/shortside  
            
  
            #### EXTEND COMPUTATION ####
            contourArea = cv2.contourArea(contour)
            rectArea = w*h
            extent = float(contourArea)/rectArea
            '''
            print('################' +str(i)+'##########################')
            print(contourArea)
            print(rectArea)
            print(extent)
            print(aspectRatio)
           '''
            #### FILTER THE CONTOURS BASED ON ASPECT RATIO AND EXTEND ####
            aspectRatioMin = ImageAnalysisConfiguration.ASPECT_RATIO_MIN
            extentMax = ImageAnalysisConfiguration.EXTENT_MAX
            
            if  aspectRatio > aspectRatioMin and extent < extentMax:

                lateralLyingContours.append(contour)
  
            else:
                removedContours.append(contour)
                
        print('lateralLyingContours')
        print(len(lateralLyingContours))
       
        
        import itertools
        sameOrientationLegs = []
        for a, b in itertools.combinations(lateralLyingContours, 2):
            ret = cv2.matchShapes(a,b,3,0.0)


            print(ret)
            
            if ret < 4:
                sameOrientationLegs.append(a)

                sameOrientationLegs.append(b)

            else:
                removedContours.append(a)
                #removedContours.append(b)                    

        
        #draw all the contours in the image
        testimage = minAreaRect_image.copy()
        testimage = cv2.drawContours(testimage, contours, -1, (	0, 0,255), -1)
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/zzall.jpg', testimage)
        
        minAreaRect_image = cv2.drawContours(testimage, lateralLyingContours, -1, (	120, 200, 120),-1)
        
   
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/zzfiltered.jpg', minAreaRect_image)
        
        print('LL')
        print(len(contours))
        #draw only the filtered contours in the image        
            
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

