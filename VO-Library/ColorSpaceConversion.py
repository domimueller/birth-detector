#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# ColorSpaceConversion.py – DESCRIPTIONS
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
TITLE = '############ COLOR SPACE CONVERSION CONFIGURATION ############'
DELIMITER = '; '
NEWLINE = '\n'


#==========================================================================
# FUNCTIONS
#==========================================================================
 
   
class ColorSpaceConversion:
    
    """
    A class used to represent the Configuration needed for Color Space Converiion

    -------
        Attributes
    ----------
    convertingImage : Boolean
        Determines  whether Conversion is desired or not. 
    conversionType : <<Enumeration>> ConversionType
        Enumeration with Color Space Conversion Types.
    ENUM_SELECT : int
        Selection of Conversion Type      
        
        

    
    Methods - see Descripton below
    -------
   obtainConvertingImage(self)
   obtainConversionType(self)
   obtainFilteringType(self)
   obtainColorSpaceConversion(self)     
       
        
   """
   
    
    def __init__(self, convertingImage, conversionType, ENUM_SELECT ):
        self.convertingImage = convertingImage
        self.conversionType = conversionType
        self.ENUM_SELECT = ENUM_SELECT

    def obtainConvertingImage(self ):
       
        """    
        Returns whether Conversion is desired or not as a Boolean
        ----------        
              
        Returns: 
        ----------                
        Conversion or not as a Boolean. 
      
        """          
        return self.convertingImage

    def obtainConversionType(self ):
        
        """    
        Returns the Conversion Type as a String. 
        ----------        
              
        Returns: 
        ----------                
        conversionType as a String. Therefore, Conversion Type needs to be 
        extracted from Enumeration based on ENUM_SELECT.      
        """  
        
        conversionType_enum_selection = self.conversionType(self.ENUM_SELECT)
        conversionType_name = conversionType_enum_selection.name
        return conversionType_name


    def obtainColorSpaceConversion(self ):
        """    
        Returns the whole Conversion Configuration as a String
        ----------        
              
        Returns: 
        ----------                
        Returns the whole Conversion Configuration.
      
        """  
        
        data = 'Conversion Type: ' + str(self.obtainConversionType())  
        strForReturn = TITLE + NEWLINE + data + NEWLINE + NEWLINE
                
        return strForReturn

