#!/usr/bin/env python3
#-*- coding: utf-8 -*-



#==========================================================================
# ImageProcessor.py – DESCRIPTIONS 
#==========================================================================

"""
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>
"""


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================



import sys
sys.path.append('../VO-Library')

import Filepath
import MimeType

#==========================================================================
# CONSTANTS
#==========================================================================

#==========================================================================
# FUNCTIONS
#==========================================================================

class ImageProcessor:
    
        
    """
    A class used to represent and implement the functionality for the Image Reader.
    Reads a File based on Filepath and returns Image for further processing.
    ...
    
    Attributes
        ----------        
    filePathAndName: Filepath
        File Path, File Name and corresponding Mime Type of the File to identify it in Filesystem. 
   
    Methods
    -------
    readImage(self, filePathAndName )
         See descriptions below.
    """ 
    
    def __init__(self):
        self.image = None
        self.reader = None
        self.writer = None
        self.brightenConfig = None
        self.colorspaceConvertConfig = None
        self.filterConfig = None
        self.threshConfig = None

    def brightenImage(self, image, config):
        
        """ 
       
        Reads a File and returns an Image for further processing.
        -------              
      
        This function is based on the library OpenCV and the corresponding function cv2.imread.
        -------              
      
        Parameters: 
        -------                 
        filePathAndName (Filepath): File Path, File Name and corresponding Mime Type of the File to identify it in Filesystem. 

        
        Returns: 
        -------              
        Image for further processing. 
      
        """  
        
        pass

    def convertColorSpace(self, image, config):
        pass

    def filterImage(self, image, config):
        pass

    def segmentImage(self, image, config):
        pass
    


#==========================================================================
# END
#==========================================================================