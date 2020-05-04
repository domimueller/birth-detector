#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# AdaptiveThresholdingConfiguration.py – DESCRIPTIONS
#==========================================================================

'''
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>

'''


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================


import sys
sys.path.append('../VO-Library')

#==========================================================================
# CONSTANTS
#==========================================================================


# Configuration for Console Output
TITLE = '############ ADAPTIVE THRESHOLDING CONFIGURATION ############'
DELIMITER = '; '
NEWLINE = '\n'
CV = 'cv2.'
#==========================================================================
# FUNCTIONS
#==========================================================================
 
   
class AdaptiveThresholdingConfiguration:
    
    """
    A class used to represent the the Configruation needed to Segment and Binarize Images applying
    the Adaptive Thresholding Technique


    -------
        Attributes
    ----------
    thresholdingType: <<Enumeration>> AdaptiveThresholdingType
        Enumeration with Adaptive Thresholding Types        
    ENUM_SELECT : int
        Selection of Adaptive Thresholding Type.         
    blockSize : int
        determines the size of the neighbourhood area 
    cSubtractor : int
        a constant which is subtracted from the mean or weighted mean calculated.
    
    Methods - see Descripton below
    -------
   obtainThresholdingType(self)
   obtainSimpleThresholdingConfiguration(self)
   obtainCSubtractor(self ):
    
       
 
    """    
    def __init__(self, thresholdingType, ENUM_SELECT, blockSize, cSubtractor):
        self.thresholdingType = thresholdingType
        self.ENUM_SELECT = ENUM_SELECT
        self.blockSize = blockSize
        self.cSubtractor = cSubtractor

    def obtainThresholdingType(self ):

        """    
        Returns the Adaptive Thresholding Type as a String. 
        ----------        
              
        Returns: 
        ----------                
        Thresholding Adaptive Type as a String. Therefore, Adaptive Thresholding Type needs to be 
        extracted from Enumeration based on ENUM_SELECT.      
        """  
          
        thresholdingType_enum_selection = self.thresholdingType(self.ENUM_SELECT)
        thresholdingType_name = thresholdingType_enum_selection.name
        thresholdingType = CV + thresholdingType_name

        return thresholdingType

    def obtainBlockSize(self ):
       
        """    
        Returns the Block Size
        ----------        
              
        Returns: 
        ----------                
        Returns the Block Size as int
      
        """ 
        
        return self.blockSize

    def obtainCSubtractor(self ):
       
        """    
        Returns the C Subtractor
        ----------        
              
        Returns: 
        ----------                
        Returns the C Subtractor as int
      
        """           
        
        return self.cSubtractor

    def obtainAdaptiveThresholdingConfiguration(self ):        
        
        """    
        
        Returns the whole Adaptive Thresholding Configuration as a String
        ----------        
              
        Returns: 
        ----------                
        Returns the whole Adaptive Thresholding Configuration.
      
        """  
        data = 'Adaptive Thresholding Type: ' + str(self.obtainThresholdingType())  + DELIMITER + 'Block Size: ' + str(self.obtainBlockSize())+ DELIMITER+ 'C Subtractor: ' + str(self.obtainCSubtractor()) 
        strForReturn = TITLE + NEWLINE + data + NEWLINE + NEWLINE      
        return strForReturn
    

