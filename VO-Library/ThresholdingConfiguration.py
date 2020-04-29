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
    thresholdingMethod: <<Enumeration>> ThresholdingMethod
        Enumeration with Thresholding Methods        
    ENUM_SELECT : int
        Selection of Thresholding Method.         
    simpleThresholdingConfiguration: SimpleThresholdingConfiguration
        Configuration and data needed to apply Simple Thresholding
    adaptiveThresholdingConfiguration: AdaptiveThresholdingConfiguration        
        Configuration and data needed to apply adaptive Thresholding 
    maximumValue: int {{OCL} maximumValue< 256}
        value to be set if pixel value is more than the threshold value
        
        

    
    Methods - see Descripton below
    -------
   obtainThresholdingImage(self)
   obtainThresholdingMethod(self)
   obtainMaximumValue(self)
   obtainThresholdingConfiguration(self)     
       
        
   """
    def __init__(self, thresholdingImage, thresholdingMethod, ENUM_SELECT,
                 simpleThresholdingConfiguration, adaptiveThresholdingConfiguration, maximumValue):
        
        self.thresholdingImage = thresholdingImage
        self.thresholdingMethod = thresholdingMethod
        self.simpleThresholdingConfiguration = simpleThresholdingConfiguration
        self.adaptiveThresholdingConfiguration = adaptiveThresholdingConfiguration
        self.maximumValue = maximumValue
        self.ENUM_SELECT = ENUM_SELECT

    def obtainThresholdingImage(self ):
       
        """    
        Returns whether Thresholding is desired or not as a Boolean
        ----------        
              
        Returns: 
        ----------                
        Thresholding or not as a Boolean. 
      
        """         
        return self.thresholdingImage

    def obtainThresholdingMethod(self ):

        """    
        Returns the Thresholding Method as a String. 
        ----------        
              
        Returns: 
        ----------                
        Thresholding Method as a String. Therefore, Thresholding Method needs to be 
        extracted from Enumeration based on ENUM_SELECT.      
        """  
          
        thresholdingMethod_enum_selection = self.thresholdingMethod(self.ENUM_SELECT)
        thresholdingMethod_name = thresholdingMethod_enum_selection.name

        return thresholdingMethod_name

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
        strForReturn = 'Thresholding Method: ' + str(self.obtainThresholdingMethod()) + '; Maximum Value: ' + str(self.obtainMaximumValue())        
        return strForReturn

#==========================================================================
# END
#==========================================================================
