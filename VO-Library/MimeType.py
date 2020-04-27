#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# MimeType.py – DESCRIPTIONS
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

class MimeType:
   
    """
    A class used to represent the MimeType of a File
    -------      
        
    Attributes
    ----------
    major : String
        media type of the file. f.e; image, audio or text
    minor : String
        subtype of the file. f.e: jpeg, basic or plain
    extension : String
        file extension. f.e: .jpg, .mp3 or .html      
    """    


    def __init__(self, major, minor, extension):
        
        """ 
       
        Constructs a  MimeType Object
        ----------        
        ----------                
      
        Parameters: 
        ----------        
        major, minor and extension: see description above       
      
      
        """                 

        self.major = major
        self.minor = minor
        self.extension = extension

       

    def value(self ):

        """ 
       
        Returns the Value of the MimeType as a String
        ----------        
              
        Returns: 
        ----------                
        MimeType as a String. 
      
        """         	
        return self.major + '/' + self.minor

    def extension(self ):
        """ 
       
        Returns the file extension as a String
        ----------        
              
        Returns: 
        ----------                
  		file extension as a String
        """         	  

        return self.extension

    def extensionWithPoint(self ):

        """ 
       
        Returns the file extension with a point before as a String
        ----------        
              
        Returns: 
        ----------                
        Returns the file extension with a point before  
      
        """         	
        return '.' + self.extension
#==========================================================================
# END
#==========================================================================