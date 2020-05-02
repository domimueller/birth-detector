#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# HSV.py – DESCRIPTIONS
#==========================================================================

'''
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>
'''


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================

import numpy as np

#==========================================================================
# CONSTANTS
#==========================================================================


# Configuration for Console Output
TITLE = '' # at the moment, no title desired. 
DELIMITER = '; '
NEWLINE = '\n'


#==========================================================================
# FUNCTIONS
#==========================================================================

class HSV:
    
    """
    A class used to represent the HSV Color Space
    -------      
        
    Attributes
    ----------
    hue :  int {{OCL} hue < 361}
        Hue value
    saturation : int {{OCL} saturation < 101}
        saturation value
    value :  int {{OCL} value < 101}
        value (brightness)   
        
    
    Methods- see Descripton below
    -------
   obtainHue(self)
   obtainSaturation(self)
   obtainValue(self )
   obtainHsv(self)
   """    

    def __init__(self, hue, saturation, value):
        self.hue = hue
        self.saturation = saturation
        self.value = value

    def obtainHue(self ):

        """ 
   
        Returns the Hue value of a color
        ----------        
              
        Returns: 
        ----------                
        Hue value. 
      
        """          
        return self.hue

    def obtainSaturation(self ):
      
        """ 
   
        Returns the Saturation value of a color
        ----------        
              
        Returns: 
        ----------                
        Saturation value. 
      
        """          
        return self.saturation

    def obtainValue(self ):
        
        """ 
   
        Returns the value (brightness) of a color
        ----------        
              
        Returns: 
        ----------                
        value (brightness) 
      
        """          
        return self.value

    def obtainColor(self ):
        
        """ 
   
        Returns values of the three HSV channels for further processing
        ----------        
              
        Returns: 
        ----------                
        color in HSV color space 
      
        """      
        
        return np.array([self.obtainHue(),self.obtainSaturation(),self.obtainValue()])

    def obtainHsv(self ):
        
        """ 
       
        Returns the color as a string representation
        ----------        
              
        Returns: 
        ----------                
        color as string. 
      
        """ 
        data = 'Hue Value: ' + str(self.obtainHue())  + DELIMITER + 'Saturation Value: ' + str(self.obtainSaturation())+ DELIMITER+ 'Value (Brightness): ' + str(self.obtainValue()) 
        strForReturn = TITLE + NEWLINE + data + NEWLINE + NEWLINE      
        return strForReturn
    
        
        return strForReturn
