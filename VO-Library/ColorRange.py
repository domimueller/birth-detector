#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# ColorRange.py – DESCRIPTIONS
#==========================================================================

'''
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>
'''


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================

import HSV

#==========================================================================
# CONSTANTS
#==========================================================================



# Configuration for Console Output
TITLE = '############ Color Range ############'
DELIMITER = '; '
NEWLINE = '\n'


#==========================================================================
# FUNCTIONS
#==========================================================================
class ColorRange:
    
    """
    A class used to represent Color Range in HSV Color Model
    -------      
        
    Attributes
    ----------
    lowerBound :  HSV
        lower Bound of HSV Color 
    upperBound : HSV
        upper Bound of HSV Color 
   
        
    
    Methods- see Descripton below
    -------
   obtainLowerBound(self)
   obtainUpperBound(self)
   obtainColorRange(self )
   """     
    def __init__(self, lowerBound, upperBound):
        self.lowerBound = lowerBound
        self.upperBound = upperBound

    def obtainLowerBound(self ):

        """ 
   
        Returns the  lower Bound in HSV Color Space
        ----------        
              
        Returns: 
        ----------                
        lower Bound. 
      
        """             
        return self.lowerBound

    def obtainUpperBound(self ):
        
        """ 
   
        Returns the upper Bound in HSV Color Space
        ----------        
              
        Returns: 
        ----------                
        upper Bound. 
      
        """           
        return self.upperBound

    def obtainColorRange(self ):
        
        """ 
       
        Returns the color range as a string representation
        ----------        
              
        Returns: 
        ----------                
        color range as string. 
      
        """ 

        data = 'lower Bound: ' + self.obtainLowerBound().obtainHsv()  + 'upper Bound: ' + self.obtainUpperBound().obtainHsv() 
        strForReturn = TITLE + NEWLINE + data + NEWLINE + NEWLINE      
        return strForReturn
    
        
        return strForReturn

