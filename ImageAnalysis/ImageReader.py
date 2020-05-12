#!/usr/bin/python
#-*- coding: utf-8 -*-

#==========================================================================
# ImageController.py – DESCRIPTIONS 
#==========================================================================

"""
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>
"""


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================
import cv2 

#==========================================================================
# CONSTANTS
#==========================================================================


#==========================================================================
# FUNCTIONS
#==========================================================================


class ImageReader:
    
    
    """
    A class used to represent and implement the functionality for the Image Reader.
    Reads a File based on Filepath and returns Image for further processing.
    ...
    
    Attributes
        ----------        

    Methods
    -------
    readImage(self, filePathAndName )
         See descriptions below.
    """ 
    
    
    def __init__(self ):
        # further statements not yet required. Because
        #Parametrization of readImage method is more convenient
        pass


    def readImage(self, filePathAndName ):
        
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

        return cv2.imread(filePathAndName.obtainFileNameAndPath())

#==========================================================================
# END
#==========================================================================