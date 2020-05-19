#!/usr/bin/env python3
#-*- coding: utf-8 -*-



#==========================================================================
# RraitRecognitor.py – DESCRIPTIONS 
#==========================================================================

"""
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>
"""


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================


import cv2 
import numpy as np

import sys
sys.path.append('../VO-Library')
sys.path.append('../ImageAnalysisHousekeeping')
import ContourRotator as rotator
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
BLANK_IMG_COLOR = 255

##### For Demonstration Purpose. Write down the intermidiate steps


PATH = globalConfig.WRITER_FILE_PATH_MAIN 

FILENAME_MASK = '7LightBulbMasks.jpg'
FILENAME_FILTERED_BY_ANGLE = '8filteredByAngle.jpg'
FILENAME_FILTERED_BY_RATIOS = '9filteredByRatios.jpg'
FILENAME_FILTERED_BY_SIMILARITY = '10filteredBySimilarity.jpg'

maskFileNamePath = PATH + FILENAME_MASK
angleFileNamePath = PATH + FILENAME_FILTERED_BY_ANGLE
ratiosFileNamePath = PATH + FILENAME_FILTERED_BY_RATIOS
similarityFileNamePath = PATH + FILENAME_FILTERED_BY_SIMILARITY

class TraitRecognitor:
    
    """
    A class used to represent and implement the functionality for the Trait Recognition of Cows.
    Filters contours based on given criteria.
    ...
    
    Attributes
    ----------        
    standingCowIsDetected: Boolean
        Expresses, whether a standing cow is been detected     
    lateralLyingCowIsDetected: Image
       Expresses, whether a lateral lying cow is been detected    
       
      
    Methods - See descriptions below.
    
    -------
    detectStandingCow(self, contour, image, config):
    detectLateralLyingClow(self, contours, image, config)
    detectRotationAngle(self, image, config)
    filterByAngle(self, image, contours, config)
    filterByGeometricRatios(self, image, allContours, filteredByAngleContours)  
    matchShapes(self, image, allContours, filteredByRatiosContours):
    obtainStandingCowIsDetected()       
    obtainLateralLyingCowIsDetected()
    
    """
    def __init__(self):
        self.standingCowIsDetected = None
        self.lateralLyingCowIsDetected = None

    def detectStandingCow(self, contour, image, config):
        """ 
        
        ### OUT OF SCOPE - NOT YET IMPLEMENTED ###
       
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
        
        pass
    

    def detectLateralLyingCow(self, contours, image, config):
        """ 
       
        Orchestrates other Contour Filtering functions
        -------              
      
        acts as orchestration function to execute angle filtering, extent filtering, 
        aspect ratio filtering and similarity filtering
        -------              
      
        Parameters: 
        -------                 
        contours : Contours detected by findContours()
        image: Image to draw
        config: Filtering parameters
        
        Returns: 
        -------              
        contours which are the foundation of the decision
        minAreaRectImage: Image with minimal area Rectangle going around each contour
        """          
               
        
        filteredByRatios, filteredBySimilarity  = [],  []
        minAreaRectImage = image.copy()
        
        for contour in contours: 
            ### DRAW THE MIN AREA RECTAGNLE FOR BETTER UNDERSTANDING OF THE CONTOURS ###
            # calculate the rectangle with minimal area around the contour
            rotated_rect = cv2.minAreaRect(contour)
            (x, y), (width, height), rotatedRectAngle = rotated_rect
       
            # calculate box and draw the rectangle
            box = cv2.boxPoints(rotated_rect)
            box = np.int0(box)
            cv2.polylines(minAreaRectImage, [box], True, globalConfig.BLACK.obtainDrawingColor(), globalConfig.THICKNESS_THICK)  


        filteredByAngle = self.filterByAngle( minAreaRectImage, contours, config)        
        filteredByRatios = self.filterByGeometricRatios( minAreaRectImage, contours, filteredByAngle)  
        
        # return filteredByRatios because filteredBySimilarity is zero if only one Contour is left
        filteredBySimilarity = self.matchShapes(minAreaRectImage, contours, filteredByRatios)
        
        if len(filteredBySimilarity) < 2:
            filteredContours = filteredByRatios
        else:
            filteredContours = filteredBySimilarity
            
        return (filteredContours, minAreaRectImage)   


    def detectRotationAngle(self, image, config):
        
        """ 
       
        Detects the rotation Angle to compute the angle for angle Comparison
        -------              
      
        This Function reads a Color Range, which is corresponding to an unique object (reference object) in the image
        with know orientation (angle). Because we know the real-life angle, we can compute the correct angle
        for comparison. In the current implementation, this unique object is the light bulb.
        -------              
      
        Parameters: 
        -------                 
        image: Image to draw
        config: Filtering parameters
        
        Returns: 
        -------              
        angle for comparison

        """          
        
        
        filteredlightBulbsByArea = []   

        lightBulbAngle = 0
        finderConfig= config
        

        print(ANGLE_ANALYSIS_TITLE + NEWLINE + NEWLINE)

        # generate mask to show where in the image the light is situated
        lowerBound = globalConfig.LOWER_BOUND_LIGHT.obtainColor()
        upperBound = globalConfig.UPPER_BOUND_LIGHT.obtainColor()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        lightBulb = cv2.inRange(image, lowerBound , upperBound)
        cv2.imwrite(maskFileNamePath, lightBulb)
        
        #derive contours from mask of lightning 
        lightBulbContours, hierachy = cv2.findContours( lightBulb, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE );
        image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

        # filter contours from lightning mask by area size        
        for contour in lightBulbContours:
            conturArea = cv2.contourArea(contour)
            if conturArea >= finderConfig.obtainMinArea():

                filteredlightBulbsByArea.append(contour)             
       

        for lightBulb in filteredlightBulbsByArea:
                             
                #  Ma and ma are Major Axis and Minor Axis lengths. angle ist orientation of Ellipse
                if len(lightBulb) > 4:
                    (x,y),(MA,ma),angle = cv2.fitEllipse(lightBulb) 
                
                    # uncomment to see how the ellipse looks like
                    #img = cv2.ellipse(originalImage.copy(),(int(x),int(y)),(int(MA),int(ma)),0,0,360,(0,0,0),2) 
                    
                    
                    if int(len(filteredlightBulbsByArea)) == 1:
                        lightBulbAngle = angle % DEGREE_MODULO 
                        print(MEASURED_LIGHT_BULB_ANGLE_TITLE + str(angle))
                                                      
                        #  Ma and ma are Major Axis and Minor Axis lengths. angle ist orientation of Ellipse
                    else:
                        lightBulbAngle = (lightBulbAngle + angle)% DEGREE_MODULO 
                        print(WARNING_MSG)

        # rotate the image using the light bulb as reference.
        print(EXPECTED_LIGHT_BULB_REAL_LIFE_ANGLE_TITLE + str(globalConfig.LIGHT_BULB_ANGLE_EXPECTION))
        rotationAngle =lightBulbAngle-globalConfig.LIGHT_BULB_ANGLE_EXPECTION
        print(ADJUSTED_ROTATION_ANGLE_TITILE + str(rotationAngle)) 
     
        return lightBulbAngle
    
    def filterByAngle(self, image, contours, config):
   
        
        """ 
       
        Detects the rotation Angle to compute the angle for angle Comparison
        -------              
      
        Measure the angle of each contour and compute relative angle towards the reference object (light bulb)
        -------              
      
        Parameters: 
        -------                 
        image: Image to draw
        config: Filtering parameters
        contours: Contours to filter
        
        Returns: 
        -------              
        contours: filtered Contours
       
        """ 
        
        #=================================================================================
        # FILTER THE CONTOUR BY ANGLE OF ITS FITTING ELLIPSE: ONLY ANGLES IN A
        # SPECIFIED RANGE ARE POSSIBLY LEGS IN LATERAL LYING POSITION
        #
        # Measure the angle of each contour and compute relative angle towards light bulb
        #
        # angle measurement based on fitEllipse() function.
        #================================================================================= 


        ## copy and prepare imagesf for later usage       
        negativeRotatedImage, minAreaRectImage, analysisImage  = image.copy(), image.copy(), image.copy() 
        
        
        filteredByAngle, uninterestingContours = [], []
        negativeRotationAngle, positiveRotation, positivRotationAngle, lightBulbAngle  = 0, 0, 0, 0

        lightBulbAngle = self.detectRotationAngle(image, config)

        if globalConfig.FILTER_BY_ANGLE == False:
            for contour in contours:
               filteredByAngle.append(contour)
             
              
        else: 
            for contour in contours:
                          
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
                positiveRotationAngle = lightBulbAngle - globalConfig.LIGHT_BULB_ANGLE_EXPECTION
                
                # negativeRotationAngle rotats the image so that the light bulb is at the bottom. 
                # this facilitaes to handle negative angles of the contoursEllipseAngle
                negativeRotationAngle = lightBulbAngle - (globalConfig.LIGHT_BULB_ANGLE_EXPECTION*-1)
                positiveAdjustedAngle = (contoursEllipseAngle - positiveRotationAngle)% DEGREE_MODULO 
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
        
        # writing this images will show the result of this step --> writing not required at the moment
        posiveRotatedImage = cv2.warpAffine(analysisImage, positiveRotation, (h, w))
        negativeRotatedImage = cv2.warpAffine(analysisImage, negativeRotation, (h, w))
                

       #=================================================================================
        # DRAW THE IMAGE TO A HAVE A NICE OVERVIEW 
        # first, contours are been drawed in an image
        # then this image is beeing used again to overdraw the contours, which are beeing filtered and 
        # again considered to be legs in lateral lying position
        #=================================================================================        
    
        allContoursImage = minAreaRectImage.copy()        
        allContoursImage = cv2.drawContours(allContoursImage, contours, -1,  globalConfig.GREEN.obtainDrawingColor(), globalConfig.THICKNESS_FILL)
        filteredByAngleImage = cv2.drawContours(allContoursImage, filteredByAngle, -1, globalConfig.RED.obtainDrawingColor(), globalConfig.THICKNESS_FILL)
        cv2.imwrite(angleFileNamePath, filteredByAngleImage)
        
        return filteredByAngle
    
    def filterByGeometricRatios(self, image, allContours, filteredByAngleContours):

        """ 
       
        Filters the contours by geometric properties
        -------              
      
        The function filters the contours by the Ratios "Aspect Ratio" and "Extent"
        -------              
      
        Parameters: 
        -------                 
        image: Image to draw
        allContours: Not filtered contours, all contours
        filteredByAngleContours: Contours filtered by angle
        
        Returns: 
        -------              
        fliteredByRatios: filtered Contours
       
        """ 
           

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
        # MAXIMUM EXTENT PROVIDED BY CONFIGURATION
        # 
        #=================================================================================        
       
        filteredByAngle = filteredByAngleContours 
        fliteredByRatios, uninterestingContours = [], []
        allContoursImage = image.copy()        

        
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
    
        allContoursImage = cv2.drawContours(allContoursImage, allContours, -1,  globalConfig.GREEN.obtainDrawingColor(), globalConfig.THICKNESS_FILL)
        ratioFilteringImage = cv2.drawContours(allContoursImage, fliteredByRatios, -1, globalConfig.RED.obtainDrawingColor(), globalConfig.THICKNESS_FILL)
        cv2.imwrite(ratiosFileNamePath, ratioFilteringImage)
       
        return fliteredByRatios
        
        
       
    def matchShapes(self, image, allContours, filteredByRatiosContours):

        """ 
       
        Filters the contours by Similarity Metric
        -------              
      
        The function filters the contours based on the OpenCV function cv2.matchShapes().
        This Function returns a similarity metric, which is been applied for filtering.
        -------              
      
        Parameters: 
        -------                 
        image: Image to draw
        allContours: Not filtered contours, all contours
        filteredByRatiosContours: Contours filtered by angle and Ratios
        
        Returns: 
        -------              
        filteredBySimilarity: filtered Contours
       
        """ 
           
        
        #=================================================================================
        # FILTER THE CONTOUR BY METRIC SHOWING THE SIMILARITY: 
        # A COW HAS AT LEAST TWO LEGS. IF ONE IS DETECTED, AT LEAST A SECOND 
        # LEG (whiches looks similar) HAS TO BE DETECTED IN ORDER TO MAKE AN ANSSUMTION 
        # ABOUT THE LYING POSITION
        # 
        # COMPUTATION OF SIMILARITY METRIC BASED ON matchShapes()
        # 
        #=================================================================================        
        
        whiteimage = image.copy()
        whiteimage = np.zeros([whiteimage.shape[0],whiteimage.shape[1], 3], dtype=np.uint8)
        whiteimage[:] = BLANK_IMG_COLOR    
        
        fliteredByRatios = filteredByRatiosContours
        fliteredByRatiosNoAngle, filteredBySimilarity, uninterestingContours  = [], [], []

        for contour in fliteredByRatios:
        
            rotated_rect = cv2.minAreaRect(contour)
            (x, y), (width, height), rotatedRectAngle = rotated_rect               
            rotationAngle =  (globalConfig.ANKER_ANGLE-rotatedRectAngle)%DEGREE_MODULO
            cnt_rotated = rotator.ContourRotator().rotateContour(contour, rotationAngle)
                      
            fliteredByRatiosNoAngle.append(cnt_rotated)
     
        sameOrientationLegs = []
        for a, b in itertools.combinations(fliteredByRatiosNoAngle, 2):
 
            similarity = cv2.matchShapes(a,b,1,0.0)
            if similarity < globalConfig.SIMILARITY_MAX:

                if a not in sameOrientationLegs: 
                    filteredBySimilarity.append(a)
                    
                if b not in sameOrientationLegs:                     
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
    
        whiteimage = cv2.drawContours(whiteimage, fliteredByRatiosNoAngle, -1,  globalConfig.GREEN.obtainDrawingColor(), globalConfig.THICKNESS_FILL)
        similarityFilteringImage = cv2.drawContours(whiteimage, filteredBySimilarity, -1, globalConfig.RED.obtainDrawingColor(), globalConfig.THICKNESS_FILL)
        cv2.imwrite(similarityFileNamePath, similarityFilteringImage)
       
        return filteredBySimilarity

      
       
    def obtainStandingCowIsDetected(self ):
        

        """
        ## not yet used but helpfull for further development ##
       
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
        ## not yet used but helpfull for further development ##
        
        Returns wheter lateral lying Cow is been detected by last analysis (without executing analysis again) 
        ----------        
              
        Returns: 
        ----------                
        Boolean to express whether lateral lying cow is in the image or not.
      
        """        
        return self.lateralLyingCowIsDetected

