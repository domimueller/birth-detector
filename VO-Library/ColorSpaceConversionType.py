#!/usr/bin/env python3
#-*- coding: utf-8 -*-


#==========================================================================
# ColorSpaceConverisionType.py – DESCRIPTIONS
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
  
class ColorSpaceConversionType(Enum):
    
    """
    A class used to represent the enumeration of the possible Color Space Conversion Types
    """    
    
    COLOR_BGR2GRAY = 1
    COLOR_BGR2HSV = 2
    COLOR_HSV2BGR = 3
    COLOR_GRAY2BGR = 4
    COLOR_BGR2YUV = 5
    COLOR_YUV2BGR = 6
    
#==========================================================================
# END
#==========================================================================
