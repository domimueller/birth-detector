#!/usr/bin/env python3
#-*- coding: utf-8 -*-


#==========================================================================
# ThresholdingType.py – DESCRIPTIONS
#==========================================================================

'''
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>
'''

#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================

from enum import Enum

#==========================================================================
# FUNCTIONS
#==========================================================================
  
class ThresholdingType(Enum):
    
    """
    A class used to represent the enumeration of the possible Thresholding Types

    """    
       
    THRESH_BINARY = 1
    THRESH_BINARY_INV = 2
    THRESH_TRUNC = 3
    THRESH_TOZERO = 4
    THRESH_TOZERO_INV = 5
    THRESH_BINARY_AND_THRESH_OTSU = 6
    THRESH_BINARY_AND_THRESH_TRIANGLE = 7
    
#==========================================================================
# END
#==========================================================================
