#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# Filepath.py – DESCRIPTIONS
#==========================================================================

'''
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>

'''


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


class Filepath:
    
    """
    A class used to represent the Filepath (path, name and mime-type) of a File


    -------
        Attributes
    ----------
    filePath : String
        path to the file. 
    fileName : String
        name of the file. 
    mimeType : MimeType
        file extension. f.e: .jpg, .mp3 or .html      

    
    Methods - see Descripton below
    -------
   obtainFilePath(self):
   obtainFileName(self):
   obtainMimeType(self):   
   obtainFileNameAndPath(self):
        
                        
    """
    
    def __init__(self, filePath, fileName, mimeType):
        self.filePath = filePath
        self.fileName = fileName
        self.mimeType = mimeType
        
    def obtainFilePath(self ):
       
        """ 
       
        Returns the Filepath as a String
        ----------        
              
        Returns: 
        ----------                
        Filepath as a String. 
      
        """         	
        return self.filePath

    def obtainFileName(self ):
 
        """ 
       
        Returns the Filename as a String
        ----------        
              
        Returns: 
        ----------                
        Filename as a String. 
      
        """ 
        
        return self.fileName


    def obtainMimeType(self ):
        
        """ 
       
        Returns the mimeType as a String
        ----------        
              
        Returns: 
        ----------                
        mimeType as a String. 
    
        """
        return self.mimeType()
    

    def obtainFileNameAndPath(self ):
      
        """ 
       
        Returns the path and the filename as a String
        ----------        
              
        Returns: 
        ----------                
        path and the filename as a String. 
    
        """       
        return  self.filePath  + self.fileName + self.mimeType.extensionWithPoint()

#==========================================================================
# END
#==========================================================================

