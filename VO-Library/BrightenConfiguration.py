#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# BrightenConfiguration.py – DESCRIPTIONS
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

class BrightenConfiguration:
    
    
    """
    A class used to represent the Filepath (path, name and mime-type) of a File


    -------
        Attributes
    ----------
    brighteningImage : Boolean
        Determines  whether Brightening is desired or not. 
    brightenerFactor : int
        Factor for Brightening as int 
    equalizingImage : Boolean
        Determines  whether Equalizing is desired or not.  
    clipLimit : int
        Clip Limit for Equalizing
    equalizingType : <<Enumeration>> EqualizingType
        Enumeration with Equalizing Types. So far, only CLAHE supported.
    ENUM_SELECT : int
        Selection of Equalizing Type. 1 = CLAHE       
        
        

    
    Methods - see Descripton below
    -------
   obtainBrighteningImage(self)
   obtainBrightenerFactor(self)
   obtainEqualizingImage(self)     
   obtainClipLimit(self)
   obtainEqualizingType(self)
   obtainBrightenConfiguration(self)       
        
                        
    """
    
    def __init__(self, brighteningImage, brightenerFactor, equalizingImage, clipLimit, equalizingType, ENUM_SELECT ):
       
        self.brighteningImage = brighteningImage
        self.brightenerFactor = brightenerFactor
        self.equalizingImage = equalizingImage
        self.clipLimit = clipLimit
        self.equalizingType = equalizingType
        self.ENUM_SELECT = ENUM_SELECT

    def obtainBrighteningImage(self ):
       
        """    
        Returns whether Brightening is desired or not as a Boolean
        ----------        
              
        Returns: 
        ----------                
        Brightening or not as a Boolean. 
      
        """           
        return self.brighteningImage

    def obtainBrightenerFactor(self ):
        
 
        """ 
       
        Returns the Factor for Brightening as int
        ----------        
              
        Returns: 
        ----------                
        Brightening Factor as  int
      
        """ 
        
        return self.brightenerFactor

    def obtainEqualizingImage(self ):
 
        """ 
       
        Returns whether Equalizing is desired or not as a Boolean
        ----------        
              
        Returns: 
        ----------                
        Equalizing or not as a Boolean. 
      
        
        """ 
        
        return self.equalizingImage

    def obtainClipLimit(self ):
 
 
        """ 
       
        Returns the Clip Limit for CLAHE
        ----------        
              
        Returns: 
        ----------                
        CLAHE Clip Limit
      
        """ 
        
        return self.clipLimit

    def obtainEqualizingType(self ):

 
        """ 
       
        Returns the Equalizing Type as a String. 
        ----------        
              
        Returns: 
        ----------                
        equalizingType as a String. Therefore, Equalizing Type needs to be 
        extracted from Enumeration based on ENUM_SELECT.
      
        """ 
        equalizingType_enum_selection = self.equalizingType(self.ENUM_SELECT)
        equalizingType_name = equalizingType_enum_selection.name
        return equalizingType_name

    def obtainBrightenConfiguration(self ):

 
        """ 
       
        Returns the whole Brightening Configuration as a String
        ----------        
              
        Returns: 
        ----------                
        Brightening Configuration as a String. 
      
        """    
        strForReturn = 'Brightener Factor: ' + str(self.obtainBrightenerFactor())  + '; Equalizing Type: ' + str(self.obtainEqualizingType()) + '; Clip Limit: ' + str(self.obtainClipLimit()) 
        
        return strForReturn
    
#==========================================================================
# END
#==========================================================================
