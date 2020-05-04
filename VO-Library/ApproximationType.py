#!/usr/bin/env python3
#-*- coding: utf-8 -*-


#==========================================================================
# ApproximationType.py – DESCRIPTIONS
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
 
class ApproximationType(Enum):
    
    """
    A class used to represent the enumeration of the possible Approximation Types

    """    
    
    CHAIN_APPROX_NONE = 1
    CHAIN_APPROX_SIMPLE = 2
    CHAIN_APPROX_TC89_L1 = 3
    CHAIN_APPROX_TC89_KCOS = 4
    
    
#==========================================================================
# END
#==========================================================================
    