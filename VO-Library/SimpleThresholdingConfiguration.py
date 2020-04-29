#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# SimpleThresholdingConfiguration.py – DESCRIPTIONS
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
 
                
  
class SimpleThresholdingConfiguration:
    
    """
    A class used to represent the the Configruation needed to Segment and Binarize Images applying
    the Simple Thresholding Technique


    -------
        Attributes
    ----------
 
    thresholdingType: <<Enumeration>> SimpleThresholdingType
        Enumeration with Simple Thresholding Types        
    ENUM_SELECT : int
        Selection of Simple Thresholding Type.         

    
    Methods - see Descripton below
    -------
   obtainThresholdingType(self)
   obtainSimpleThresholdingConfiguration(self)
    
       
 

    """
    def __init__(self, thresholdingType, ENUM_SELECT):
        self.thresholdingType = thresholdingType
        self.ENUM_SELECT = ENUM_SELECT

    def obtainThresholdingType(self ):
        
        """    
        Returns the Simple Thresholding Type as a String. 
        ----------        
              
        Returns: 
        ----------                
        Thresholding Simple Type as a String. Therefore, Simple Thresholding Type needs to be 
        extracted from Enumeration based on ENUM_SELECT.      
        """  
          
        thresholdingType_enum_selection = self.thresholdingType(self.ENUM_SELECT)
        thresholdingType_name = thresholdingType_enum_selection.name

        return thresholdingType_name
    
    
    def obtainSimpleThresholdingConfiguration(self ):
      
        """    
        Returns the whole Simple Thresholding Configuration as a String
        ----------        
              
        Returns: 
        ----------                
        Returns the whole Simple Thresholding Configuration.
      
        """  
        strForReturn = 'Simple Thresholding Type: ' + str(self.obtainThresholdingType())         
        return strForReturn
    
#==========================================================================
# END
#==========================================================================
    