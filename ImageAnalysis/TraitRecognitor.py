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
import ImageAnalysisConfiguration  as globalConfig

import itertools

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
        
        ### Brightening the Image: Only for Exporting the images to the report!
       
        M = np.ones(originalImage.shape, dtype="uint8")*60  
        originalImage = cv2.add(originalImage, M)
        clahe = cv2.createCLAHE(clipLimit= 4.0)
        H, S, V = cv2.split(cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV))
        eq_V = clahe.apply(V)
        originalImage = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2BGR)         

        lightBulbContours = []
        filteredlightBulbsByArea = []
        filteredByAngle = []
        fliteredByRatios = []
        filteredBySimilarity = []
        lateralLyingContours = []
        uninterestingContours = []
        analysisImage = originalImage.copy()
        newimg = originalImage.copy()
        minAreaRectImage = originalImage.copy()
        minAreaRect_image= originalImage.copy()
        image = originalImage
        
        ## copy and prepare imagesf for later usage       
        positiveRotatedImage = originalImage.copy()
        negativeRotatedImage = originalImage.copy() 
        
        
        testimage = originalImage.copy()
        whiteimage = np.zeros([testimage.shape[0],testimage.shape[1], 3], dtype=np.uint8)
        whiteimage[:] = 255        

        lightBulbAngle = 0

        print(ANGLE_ANALYSIS_TITLE + NEWLINE + NEWLINE)

        # generate mask to show where in the image the light is situated
        lowerBound = globalConfig.LOWER_BOUND_LIGHT.obtainColor()
        upperBound = globalConfig.UPPER_BOUND_LIGHT.obtainColor()
        image = cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV)
        
        lightBulb = cv2.inRange(image, lowerBound , upperBound)
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/7masks.jpg', lightBulb)
        
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
         
        print(EXPECTED_LIGHT_BULB_REAL_LIFE_ANGLE_TITLE + str(globalConfig.LIGHT_BULB_ANGLE_EXPECTION))
        
        rotationAngle =lightBulbAngle-globalConfig.LIGHT_BULB_ANGLE_EXPECTION
        
        print(ADJUSTED_ROTATION_ANGLE_TITILE + str(rotationAngle)) 
        
        #image = cv2.cvtColor(rotatedImage, cv2.COLOR_HSV2BGR)
        
        filteredByAngle = []
        adjustedAngleNegative = 0
        negativeRotationAngle = 0
        positiveRotation = 0
        positivRotationAngle = 0
        
        #=================================================================================
        # FILTER THE CONTOUR BY ANGLE OF ITS FITTING ELLIPSE: ONLY ANGLES IN A
        # SPECIFIED RANGE ARE POSSIBLY LEGS IN LATERAL LYING POSITION
        #
        # Measure the angle of each contour and compute relative angle towards light bulb
        #
        # angle measurement based on fitEllipse() function.
        #================================================================================= 

        if finderConfig.obtainFilterbyAngle() == globalConfig.FILTER_BY_ANGLE_FALSE:
            for contour in contours:
               filteredByAngle.append(contour) 
        else: 
            for contour in contours:
                          
                ### DRAW THE MIN AREA RECTAGNLE FOR BETTER UNDERSTANDING OF THE CONTOURS ###
                # calculate the rectangle with minimal area around the contour
                rotated_rect = cv2.minAreaRect(contour)
                (x, y), (width, height), rotatedRectAngle = rotated_rect
                # calculate box and draw the rectangle
                box = cv2.boxPoints(rotated_rect)
                box = np.int0(box)
                cv2.polylines(minAreaRectImage, [box], True, globalConfig.BLACK.obtainDrawingColor(), globalConfig.THICKNESS_THICK)
                
                ### MEASURE THE ANGLE OF THE CONTOURS FITTING ELLIPSE ###
                ## contour Approximation to a Polynon
                peri = cv2.arcLength(contour, True)
                contourApprox = cv2.approxPolyDP(contour, 0.004 * peri, True)
               
                #   Important is contoursEllipseAngle. Ma and ma are Major Axis and Minor Axis lengths.
                (x,y),(MA,ma),contoursEllipseAngle = cv2.fitEllipse(contourApprox)
                
                # rotation values = positive: counter-clockwise
                # positivRotationAngle and negativeRotationAngle is the angle, which is to be rotated
                # in order to achieve that the light bulb in a rotated image is in the expected position
                
                # positivRotationAngle rotats the image so that the light bulb is at the top
                positivRotationAngle = lightBulbAngle - globalConfig.LIGHT_BULB_ANGLE_EXPECTION
                
                # negativeRotationAngle rotats the image so that the light bulb is at the bottom. 
                # this facilitaes to handle negative angles of the contoursEllipseAngle
                negativeRotationAngle = lightBulbAngle - (globalConfig.LIGHT_BULB_ANGLE_EXPECTION*-1)
                positiveAdjustedAngle = (contoursEllipseAngle -positivRotationAngle) % DEGREE_MODULO 
                negativeAdjustedAngle = (negativeRotationAngle + contoursEllipseAngle) % DEGREE_MODULO 
    
                # min and max angles, that are consiered to be possible for legs in lateral lying
                minLegAngle = globalConfig.MIN_LEG_ANGLE_EXPECTION
                maxLegAngle = globalConfig.MAX_LEG_ANGLE_EXPECTION
    
                # check whether the angle is in the interesting Range of Angles. 
                # separate contours with interesting angles from contours with uninteresting angles
                
                if positiveAdjustedAngle > minLegAngle and positiveAdjustedAngle < maxLegAngle:
                    filteredByAngle.append(contour)
                    continue                                
                elif negativeAdjustedAngle > minLegAngle and negativeAdjustedAngle < maxLegAngle:
                    maxLegAngle = minLegAngle*(-1)
                    minLegAngle =  maxLegAngle*(-1)
                    filteredByAngle.append(contour)
                else:
                      uninterestingContours.append(contour) 
        
        ## write images to demonstrate what the positivRotationAngle and negativeAdjustedAngle do
        (h, w) = analysisImage.shape[:2]     
        imageCenter = (w / 2, h / 2)       
        positiveRotation = cv2.getRotationMatrix2D(imageCenter, positivRotationAngle, globalConfig.SCALE)
        negativeRotation = cv2.getRotationMatrix2D(imageCenter, negativeRotationAngle, globalConfig.SCALE)
        
        
        posiveRotatedImage = cv2.warpAffine(analysisImage, positiveRotation, (h, w))
        negativeRotatedImage = cv2.warpAffine(analysisImage, negativeRotation, (h, w))
        
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/8minAreaRect_image.jpg', minAreaRectImage)
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/9positiveRotatedImage.jpg', posiveRotatedImage)
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/10negativeRotatedImage.jpg', negativeRotatedImage)
        
 
        allContoursImage = minAreaRectImage.copy()        
        ratioFilteringImage = minAreaRectImage.copy()
        resultingImage = minAreaRectImage.copy()
        
       #=================================================================================
        # DRAW THE IMAGE TO A HAVE A NICE OVERVIEW 
        # first, contours are been drawed in an image
        # then this image is beeing used again to overdraw the contours, which are beeing filtered and 
        # again considered to be legs in lateral lying position
        #=================================================================================        
    
        allContoursImage = cv2.drawContours(allContoursImage, contours, -1,  globalConfig.GREEN.obtainDrawingColor(), globalConfig.THICKNESS_FILL)
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/11allContoursImage.jpg', allContoursImage)        
        filteredByAngleImage = cv2.drawContours(allContoursImage, filteredByAngle, -1, globalConfig.RED.obtainDrawingColor(), globalConfig.THICKNESS_FILL)
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/12filteredByAngle.jpg', filteredByAngleImage)
       
                

         #=================================================================
        # probebly not important anymore - was inside the upper for loop
        
        #
        #  
        # angle measurement based on fitEllipse() function.
        #=================================================================            
        '''
        rotated_rect = cv2.minAreaRect(contour)
        (x, y), (width, height), rotatedRectAngle = rotated_rect

        minAreaRect_image = analysisImage  
        box = cv2.boxPoints(rotated_rect)
        box = np.int0(box)
        cv2.polylines(minAreaRect_image, [box], True, (0,0,0), 5)
        '''

              

        
        
        #=================================================================================
        # FILTER THE CONTOUR BY ASPECT RATIO AND EXTENT OF ITS MIN AREA RECTANGLE: 
        # ONLY CONTOURS WITH SPECIFIC ASPECT RATIO AND EXTENT ARE POSSIBLY LEGS
        # IN LATERAL LYING POSITION
        # 
        # COMPUTATION OF MIN AREA RECTANGLE IS BASED ON minAreaRect()
        # 
        # CONSIDERING THE ASPECT RATIO,  WE ARE SEARCHING FOR RECTANGLES, WITH A ASPECT 
        # RATIO BIGGER THAN A MINIMUM ASPECT RATIO PROVIDED BY CONFIGURATION
        #
        # CONSIDERING THE EXTENT,  WE ARE SEARCHING FOR EXTENTS, SMALLER THAN A 
        # MINIMUM ASPECT RATIO PROVIDED BY CONFIGURATION
        # 
        #=================================================================================        

        


        for contour in filteredByAngle:

            # calculate the rectangle with minimal area around the contour
            rotated_rect = cv2.minAreaRect(contour)
            (x, y), (width, height), rotatedRectAngle = rotated_rect
            

			# COMPUTE ASPECT RATIO
            # use the bounding box to compute the aspect ratio           
            # make sure that aspect ratio is greater than 0 
            if width > height:
                longside = width
                shortside = height
            else:
                longside = height
                shortside = width

            aspectRatio = float(longside)/shortside  
            
            #### COMPUTE EXTENT  ####
            contourArea = cv2.contourArea(contour)
            rectArea = width*height
            extent = float(contourArea)/rectArea

            #### FILTER THE CONTOURS BASED ON ASPECT RATIO AND EXTEND ####
            aspectRatioMin = globalConfig.ASPECT_RATIO_MIN
            extentMax = globalConfig.EXTENT_MAX
            
            if  aspectRatio > aspectRatioMin and extent < extentMax:

                fliteredByRatios.append(contour)
  
            else:
                uninterestingContours.append(contour)

        #=================================================================================
        # DRAW THE IMAGE TO A HAVE A NICE OVERVIEW 
        # first, contours are been drawed in an image
        # then this image is beeing used again to overdraw the contours, which are beeing filtered and 
        # again considered to be legs in lateral lying position
        #=================================================================================        
    
        allContoursImage = cv2.drawContours(allContoursImage, filteredByAngle, -1,  globalConfig.GREEN.obtainDrawingColor(), globalConfig.THICKNESS_FILL)
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/12allContoursImage.jpg', allContoursImage)        
        ratioFilteringImage = cv2.drawContours(allContoursImage, fliteredByRatios, -1, globalConfig.RED.obtainDrawingColor(), globalConfig.THICKNESS_FILL)
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/13filteredByRatios.jpg', ratioFilteringImage)
       
        
        
        
        #=================================================================================
        # FILTER THE CONTOUR BY METRIC SHOWING THE SIMILARITY: 
        # A COW HAS AT LEAST TWO LEGS. IF ONE IS DETECTED, AT LEAST A SECOND 
        # LEG (whiches looks similar) HAS TO BE DETECTED IN ORDER TO MAKE AN ANSSUMTION 
        # ABOUT THE LYING POSITION
        # 
        # COMPUTATION OF SIMILARITY METRIC BASED ON matchShapes()
        # 
        #=================================================================================        
        
        for a, b in itertools.combinations(fliteredByRatios, 2):
 
            similarity = cv2.matchShapes(a,b,1,0.0)
            if similarity < globalConfig.SIMILARITY_MIN:

                if a not in filteredBySimilarity: 
                    filteredBySimilarity.append(a)
                if b not in filteredBySimilarity:                     
                    filteredBySimilarity.append(b)

            else:
                if a not in uninterestingContours: 
                    uninterestingContours.append(a)
                if b not in uninterestingContours:                     
                    uninterestingContours.append(b)   
                    
        #=================================================================================
        # DRAW THE IMAGE TO A HAVE A NICE OVERVIEW 
        # first, contours are been drawed in an image
        # then this image is beeing used again to overdraw the contours, which are beeing filtered and 
        # again considered to be legs in lateral lying position
        #=================================================================================        
    
        allContoursImage = cv2.drawContours(allContoursImage, contours, -1,  globalConfig.GREEN.obtainDrawingColor(), globalConfig.THICKNESS_FILL)
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/14_fliteredByRatios.jpg', allContoursImage)        
        similarityFilteringImage = cv2.drawContours(allContoursImage, filteredBySimilarity, -1, globalConfig.RED.obtainDrawingColor(), globalConfig.THICKNESS_FILL)
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/15_filteredBySimilarity.jpg', similarityFilteringImage)
       
                            
        filtedBySimNoAngle = []
        fliteredByRatiosNoAngle = []
        for contour in fliteredByRatios:
        
            rotated_rect = cv2.minAreaRect(contour)
            (x, y), (width, height), rotatedRectAngle_one = rotated_rect          
            
            rotationAngle =  (globalConfig.ANKER_ANGLE-rotatedRectAngle_one)%DEGREE_MODULO
            cnt_rotated = self.rotate_contour(contour, rotationAngle)
                      
            fliteredByRatiosNoAngle.append(cnt_rotated)
     
        sameOrientationLegs = []
        for a, b in itertools.combinations(fliteredByRatiosNoAngle, 2):
 
            similarity = cv2.matchShapes(a,b,1,0.0)
            if similarity < globalConfig.SIMILARITY_MIN:

                if a not in sameOrientationLegs: 
                    filtedBySimNoAngle.append(a)
                    
                if b not in sameOrientationLegs:                     
                    filtedBySimNoAngle.append(b)
                            

        #=================================================================================
        # DRAW THE IMAGE TO A HAVE A NICE OVERVIEW 
        # first, contours are been drawed in an image
        # then this image is beeing used again to overdraw the contours, which are beeing filtered and 
        # again considered to be legs in lateral lying position
        #=================================================================================        
    
        allContoursImage = cv2.drawContours(whiteimage, fliteredByRatiosNoAngle, -1,  globalConfig.GREEN.obtainDrawingColor(), globalConfig.THICKNESS_FILL)
        similarityFilteringImage = cv2.drawContours(whiteimage, filtedBySimNoAngle, -1, globalConfig.RED.obtainDrawingColor(), globalConfig.THICKNESS_FILL)
        cv2.imwrite('C:/Users/domim/OneDrive/Desktop/bilder/neuetests/17filteredBySimilarityNoAngle.jpg', similarityFilteringImage)
       
         
      

          
        return (lateralLyingContours, minAreaRect_image)   

    def cart2pol(self, x, y):
        theta = np.arctan2(y, x)
        rho = np.hypot(x, y)
        return theta, rho
    
    
    def pol2cart(self, theta, rho):
        x = rho * np.cos(theta)
        y = rho * np.sin(theta)
        return x, y
    
    
    def rotate_contour(self, cnt, angle):
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
    
        cnt_norm = cnt - [cx, cy]
        
        coordinates = cnt_norm[:, 0, :]
        xs, ys = coordinates[:, 0], coordinates[:, 1]
        thetas, rhos = self.cart2pol(xs, ys)
        
        thetas = np.rad2deg(thetas)
        thetas = (thetas + angle) % 360
        thetas = np.deg2rad(thetas)
        
        xs, ys = self.pol2cart( thetas, rhos)
        
        cnt_norm[:, 0, 0] = xs
        cnt_norm[:, 0, 1] = ys
    
        cnt_rotated = cnt_norm + [cx, cy]
        cnt_rotated = cnt_rotated.astype(np.int32)
    
        return cnt_rotated
    

      
       
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

