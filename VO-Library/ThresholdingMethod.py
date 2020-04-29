#!/usr/bin/env python3
#-*- coding: utf-8 -*-


#==========================================================================
# ThresholdingMethod.py – DESCRIPTIONS
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
  
class ThresholdingMethod(Enum):
    
    """
    A class used to represent the enumeration of the possible Thresholding Methods

    """    
        
    THRESHOLD = 1
    ADAPTIVE_THRESHOLD = 2
    
#==========================================================================
# END
#==========================================================================
