#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# ThresholdingConfiguration.py – DESCRIPTIONS
#==========================================================================

'''
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>

'''


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================
   

#==========================================================================
# CONSTANTS
#==========================================================================

# Configuration for Console Output
TITLE = '############ OVERALL THRESHOLDING CONFIGURATION ############'
DELIMITER = '; '
NEWLINE = '\n'
CV = 'cv2.'
ACTIVATION_MESSAGE = ' ACTIVATED'

# the + sign is not stored in enumeration. therefore, if OTSU or TRIANGLE is selected, return the correct parameter
OTSU_TYPE_ENUM_NAME = 'cv2.THRESH_BINARY_AND_THRESH_OTSU'
OTSU_TYPE_PARAM_NAME = 'cv2.THRESH_BINARY+cv2.THRESH_OTSU'

TRIANGLE_TYPE_ENUM_NAME = 'cv2.THRESH_BINARY_AND_THRESH_TRIANGLE'
TRIANGLE_TYPE_PARAM_NAME = 'cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE'


#==========================================================================
# FUNCTIONS
#==========================================================================
 
                
    
class ThresholdingConfiguration:
    
    
    """
    A class used to represent the the Configruation needed to Segment and Binarize Images applying
    the Thresholding Technique


    -------
        Attributes
    ----------
    thresholdingImage : Boolean
        Determines  whether thresholding is desired or not.
    threshold: int
        threshold value to determine whether to apply new value on this pixel or not
    thresholdingMethod: <<Enumeration>> ThresholdingMethod
        Enumeration with Thresholding Methods        
    ENUM_SELECT_METHOD : int
        Selection of Thresholding Method. 
    thresholdingType: <<Enumeration>> ThresholdingType
        Enumeration with Thresholding Type        
    ENUM_SELECT_TYPE : int
        Selection of Thresholding Type.                 
    adaptiveThresholdingConfiguration: AdaptiveThresholdingConfiguration        
        Configuration and data needed to apply adaptive Thresholding 
    maximumValue: int {{OCL} maximumValue< 256}
        value to be set if pixel value is more than the threshold value
        
        

    
    Methods - see Descripton below
    -------
   obtainThresholdingImage(self)
   obtainThreshold(self)
   obtainThresholdingMethod(self)
   obtainThresholdinType(self)
   obtainMaximumValue(self)
   obtainThresholdingConfiguration(self)     
       
        
   """
    def __init__(self, thresholdingImage, threshold, thresholdingMethod, ENUM_SELECT_METHOD, thresholdingType, 
                 ENUM_SELECT_TYPE, adaptiveThresholdingConfiguration, maximumValue):
        
        self.thresholdingImage = thresholdingImage
        self. threshold = threshold
        self.thresholdingMethod = thresholdingMethod
        self.ENUM_SELECT_METHOD = ENUM_SELECT_METHOD        
        self.thresholdingType = thresholdingType
        self.ENUM_SELECT_TYPE = ENUM_SELECT_TYPE                
        self.adaptiveThresholdingConfiguration = adaptiveThresholdingConfiguration
        self.maximumValue = maximumValue

    def obtainThresholdingImage(self ):
       
        """    
        Returns whether Thresholding is desired or not as a Boolean
        ----------        
              
        Returns: 
        ----------                
        Thresholding or not as a Boolean. 
      
        """         
        return self.thresholdingImage
    
    def obtainThreshold(self ):
        
        """    
        Returns the Threshold value 
        ----------        
              
        Returns: 
        ----------                
        Threshold.
      
        """    
        
        return self.threshold    

    def obtainThresholdingMethod(self ):

        """    
        Returns the Thresholding Method as a String. 
        ----------        
              
        Returns: 
        ----------                
        Thresholding Method as a String. Therefore, Thresholding Method needs to be 
        extracted from Enumeration based on ENUM_SELECT_METHOD.      
        """  
        
        thresholdingMethod_enum_selection = self.thresholdingMethod(self.ENUM_SELECT_METHOD)
        thresholdingMethod_name = thresholdingMethod_enum_selection.name
        thresholdingMethod = CV + thresholdingMethod_name
        return thresholdingMethod
    
    def obtainThresholdingType(self ):

        """    
        Returns the Thresholding Type as a String. 
        ----------        
              
        Returns: 
        ----------                
        Thresholding Type as a String. Therefore, Thresholding TYPE needs to be 
        extracted from Enumeration based on ENUM_SELECT_TYPE.      
        """  
          
        thresholdingType_enum_selection = self.thresholdingType(self.ENUM_SELECT_TYPE)
        thresholdingType_name = thresholdingType_enum_selection.name
        thresholdingType = CV + thresholdingType_name
        
        
        # the + sign is not stored in enumeration. therefore, if OTSU or TRIANGLE is selected, return the correct parameter
        if thresholdingType == OTSU_TYPE_ENUM_NAME:
                thresholdingType  = OTSU_TYPE_PARAM_NAME

        if thresholdingType == TRIANGLE_TYPE_ENUM_NAME:
                thresholdingType  = TRIANGLE_TYPE_PARAM_NAME                
        return thresholdingType 

    def obtainMaximumValue(self ):
        
        """    
        Returns the maximum value 
        ----------        
              
        Returns: 
        ----------                
        Value as int to be set if pixel value is more than the threshold value.
      
        """    
        
        return self.maximumValue

    def obtainThresholdingConfiguration(self ):
        
        """    
        Returns the whole Thresholding Configuration as a String
        ----------        
              
        Returns: 
        ----------                
        Returns the whole Thresholding Configuration.
      
        """  


        activationMessage = str(self.obtainThresholdingMethod()) + ACTIVATION_MESSAGE
        data = 'Thresholding Desired: ' + str(self.obtainThresholdingImage()) + DELIMITER + 'Threshold: ' +  str(self.obtainThreshold()) + DELIMITER + 'Thresholding Method: ' + str(self.obtainThresholdingMethod()) + DELIMITER + 'Thresholding Type: ' + str(self.obtainThresholdingType()) + DELIMITER + 'Maximum Value: ' + str(self.obtainMaximumValue())
 
        strForReturn = TITLE + NEWLINE + activationMessage + NEWLINE + NEWLINE  + data + NEWLINE  + NEWLINE 
        return strForReturn

#==========================================================================
# END
#==========================================================================
