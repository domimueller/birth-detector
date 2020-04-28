#!/usr/bin/env python3
#-*- coding: utf-8 -*-


#==========================================================================
# EqualizingType.py – DESCRIPTIONS
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
  

class EqualizingType(Enum):
    """
    A class used to represent the enumeration of the possible Equalizing Types
    So far, only CLAHE implemented. Further Implementations possible. 
    """    

    CLAHE = 1
    
#==========================================================================
# END
#==========================================================================
