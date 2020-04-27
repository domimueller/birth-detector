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


class ImageWriter:
    
    
    """
    A class used to represent and implement the functionality for the Image Writer.
    Writes an Image to a File.
    ...
    
    Attributes
        ----------        
    filePathAndName: Filepath
        File Path, File Name and corresponding Mime Type of the File to identify it in Filesystem. 
   
    Methods
    -------
    writeImage(self, filePathAndName )
         See descriptions below.
    """ 
    
    
    def __init__(self ):
        # further statements not yet required. Because
        #Parametrization of readImage method is more convenient
        pass


    def writeImages(self, image, filePathAndName ):
        
        """ 
       
        Writes an Image to a File.
        -------              
      
        This function is based on the library OpenCV and the corresponding function cv2.imwrite.
        -------              
      
        Parameters: 
        -------                 
        filePathAndName (Filepath): File Path, File Name and corresponding Mime Type of the File to identify it in Filesystem. 

        
        Returns: 
        -------              
        Nothing will be returned. 
      
        """  

        self.filePathAndName = filePathAndName 
        self.image = image 
        print(self.filePathAndName.filePathAndName())
        cv2.imwrite(self.filePathAndName.filePathAndName(), self.image)

#==========================================================================
# END
#==========================================================================