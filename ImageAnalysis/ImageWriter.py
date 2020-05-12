#!/usr/bin/python
#-*- coding: utf-8 -*-

#==========================================================================
# ImageWriter.py – DESCRIPTIONS 
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


class ImageWriter:
    
    """
    A class used to represent and implement the functionality for the Image Writer.
    Writes an Image to a File.
    ...
    
    Attributes
        ----------        

      
    Methods
    -------
    writeImage(self, filePathAndName, image )
         See descriptions below.
    """ 
        
    def __init__(self):
        pass

    def writeImage(self, filePathAndName, image):
    
        """ 
       
        Writes an Image to a corresponding File.
        -------              
      
        This function is based on the library OpenCV and the corresponding function cv2.imwrite.
        -------              
      
        Parameters: 
        -------                 
        image (Image): Image to write
        filePathAndName (Filepath): File Path, File Name and corresponding Mime Type of the File to identify it in Filesystem. 


        
        Returns: 
        -------              
        Nothing will be returned. 
      
        """  
                
        cv2.imwrite(filePathAndName.obtainFileNameAndPath(), image)

