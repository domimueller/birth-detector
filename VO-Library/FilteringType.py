#!/usr/bin/env python3
#-*- coding: utf-8 -*-


#==========================================================================
# FilteringType.py – DESCRIPTIONS
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
  
class FilteringType(Enum):
    """
    A class used to represent the enumeration of the possible Filtering Types
    So far, only GaussianBlug implemented. Further Implementations possible. 
    """    
    
    GAUSSIANBLUR = 1
    
#==========================================================================
# END
#==========================================================================
