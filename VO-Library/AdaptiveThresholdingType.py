#!/usr/bin/env python3
#-*- coding: utf-8 -*-


#==========================================================================
# AdaptiveThresholdingType.py – DESCRIPTIONS
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
  
class AdaptiveThresholdingType(Enum):
    
    """
    A class used to represent the enumeration of the possible Adaptive Thresholding Types

    """    
    ADAPTIVE_THRESH_MEAN_C = 1
    ADAPTIVE_THRESH_GAUSSIAN_C = 2
    
#==========================================================================
# END
#==========================================================================
