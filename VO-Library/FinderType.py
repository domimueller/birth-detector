#!/usr/bin/env python3
#-*- coding: utf-8 -*-


#==========================================================================
# FinderType.py – DESCRIPTIONS
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
 
class FinderType(Enum):
    
    """
    A class used to represent the enumeration of the possible Finder Types

    """        
    RETR_EXTERNAL = 1
    RETR_LIST = 2
    RETR_CCOMP = 3
    RETR_TREE = 4
    RETR_FLOODFILL = 5
    
#==========================================================================
# END
#==========================================================================
