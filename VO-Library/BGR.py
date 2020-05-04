#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# BGR.py – DESCRIPTIONS
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
TITLE = '############ BGR COLOR ############'
DELIMITER = '; '
NEWLINE = '\n'


#==========================================================================
# FUNCTIONS
#==========================================================================

class BGR:
    
   
    """
    A class used to represent the BGR Color Space
    -------      
        
    Attributes
    ----------
    blue :  int {{OCL} blue < 256}
        Blue color value
    green : int {{OCL} green < 256}
        green color value
    red :  int {{OCL} red < 256}
        red color value      
        
    
    Methods - see Descripton below
    -------
   obtainBlue(self)
   obtainGreen(self)
   obtainRed(self )
   obtainBgr(self)
   """    


    def __init__(self, blue, green, red):
        self.blue = blue
        self.green = green
        self.red = red

    def obtainBlue(self ):

        """ 
       
        Returns the Blue value of a color
        ----------        
              
        Returns: 
        ----------                
        Blue value. 
      
        """          
        return self.blue

    def obtainGreen(self, ):

        """ 
       
        Returns the green value of a color
        ----------        
              
        Returns: 
        ----------                
        green value. 
      
        """         
        return self.green

    def obtainRed(self ):
        
        """ 
       
        Returns the red value of a color
        ----------        
              
        Returns: 
        ----------                
        red value. 
      
        """         
        return self.red
    
    def obtainColor(self ):
        
        """ 
   
        Returns values of the three BGR channels for further processing
        ----------        
              
        Returns: 
        ----------                
        color in BRG color space 
      
        """      
        
        return np.array([self.obtainBlue(),self.obtainGreen(),self.obtainRed()])    

    
    def obtainDrawingColor(self ):
        
        """ 
   
        Returns values of the three BGR channels for further drawing. Makes sure
        that the function drawContours() is capable of understanding the color format.
        ----------        
              
        Returns: 
        ----------                
        color in BRG color space 
      
        """      
        
        return (self.obtainBlue(),self.obtainGreen(),self.obtainRed())    



    def obtainBgr(self, ):
        
        """ 
       
        Returns the color as a string representation
        ----------        
              
        Returns: 
        ----------                
        color as string. 
      
        """ 
        data = 'Blue Value: ' + str(self.obtainBlue())  + DELIMITER + 'Green Value: ' + str(self.obtainGreen())+ DELIMITER+ 'Red Value: ' + str(self.obtainRed()) 
        strForReturn = TITLE + NEWLINE + data + NEWLINE + NEWLINE      
        return strForReturn
    
        
        return strForReturn

