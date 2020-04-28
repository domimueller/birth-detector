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
    filePathAndNames: Tuple of Filepaths
        A Filepath Object consists of File Path, File Name and the corresponding Mime Type 
        of the File to identify it in Filesystem.     
    image: Image
        Image to write. 
      
    Methods
    -------
    writeImages(self, image, filePathAndNames )
         See descriptions below.
    """ 
    
    
    def __init__(self ):
        # further statements not yet required. Because
        #Parametrization of readImage method is more convenient
        pass


    def writeImages(self, image, filePathAndNames ):
        
    
        """ 
       
        Writes a Tuple of Images to corresponding Files.
        -------              
      
        This function is based on the library OpenCV and the corresponding function cv2.imwrite.
        -------              
      
        Parameters: 
        -------                 
        image (Image): Image to write
        filePathAndNames (Tuple of Filepaths): Tuple of File Paths, File Names and corresponding Mime Types 
        in order to identify the file. 

        
        Returns: 
        -------              
        Nothing will be returned. 
      
        """  
        
        self.filePathAndName = filePathAndNames 
        self.image = image 
        
        for filePathAndName in filePathAndNames:
            cv2.imwrite(filePathAndName.filePathAndName(), image)

#==========================================================================
# END
#==========================================================================