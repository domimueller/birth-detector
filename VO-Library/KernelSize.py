#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# FilterConfiguration.py – DESCRIPTIONS
#==========================================================================

'''
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>

'''


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================
   

#==========================================================================
# CONSTANTS
#==========================================================================



#==========================================================================
# FUNCTIONS
#==========================================================================
 
class KernelSize:
    
    """
    A class used to represent the Kernel Size


    -------
        Attributes
    ----------
    kernelWidth : int
       Kernel width 
    kernelLength : int
        Kernel length 
 
        
        

    
    Methods - see Descripton below
    -------
   obtainKernelWidth(self)
   obtainKernelLength(self)
   obtainKernelSize(self)

        
   """    
    def __init__(self, width, length):
        self.kernelWidth = width
        self.kernelLength = length

    def obtainKernelWidth(self ):
       
        """    
        Returns the Kernel Width
        ----------        
              
        Returns: 
        ----------                
        Returns the Kernel Width as int
      
        """          
        return self.kernelWidth

    def obtainKernelLength(self ):

        """    
        Returns the Kernel Length
        ----------        
              
        Returns: 
        ----------                
        Returns the Kernel Length as int
      
        """        
        return self.kernelLength

    def obtainKernelSize(self ):
        
        """    
        Returns the Kernel Length and Width
        ----------        
              
        Returns: 
        ----------                
        Returns the Kernel Length and Width as String
      
        """      
        return 'Länge: ' + str(self.kernelLength) + ' Pixel; Breite: ' + str(self.kernelWidth) + ' Pixel'

#==========================================================================
# END
#==========================================================================
 