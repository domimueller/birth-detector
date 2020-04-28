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
 
                
    
class FilterConfiguration:
    
    
    """
    A class used to represent the Filepath (path, name and mime-type) of a File


    -------
        Attributes
    ----------
    filteringImage : Boolean
        Determines  whether Filtering is desired or not. 
    kernelSize : KernelSize
        Kernel width and length 
    filteringType : <<Enumeration>> FilteringType
        Enumeration with Filtering Types. So far, only Gaussian Blur supported.
    ENUM_SELECT : int
        Selection of Filtering Type. 1 = Gaussian Blur       
        
        

    
    Methods - see Descripton below
    -------
   obtainFilteringImage(self)
   obtainKernelSize(self)
   obtainFilteringType(self)
   obtainFilterConfiguration(self)     
       
        
   """
   
   
    def __init__(self, filteringImage, kernelSize, filteringType, ENUM_SELECT ):
        self.filteringImage = filteringImage
        self.kernelSize = kernelSize
        self.filteringType = filteringType
        self.ENUM_SELECT = ENUM_SELECT

    def obtainFilteringImage(self ):
       
        """    
        Returns whether Filtering is desired or not as a Boolean
        ----------        
              
        Returns: 
        ----------                
        Filtering or not as a Boolean. 
      
        """  
        
        return self.filteringImage
    
    def obtainKernelSize(self ):
           
            """    
            Returns whether Kernel Size 
            ----------        
                  
            Returns: 
            ----------                
            Returns whether Kernel Size as a String
          
            """  
            
            return self.kernelSize.obtainKernelSize()
        
    def obtainFilteringType(self ):
        
        """    
        Returns the Filtering Type as a String. 
        ----------        
              
        Returns: 
        ----------                
        filteringType as a String. Therefore, Filtering Type needs to be 
        extracted from Enumeration based on ENUM_SELECT.      
        """  
        filteringType_enum_selection = self.filteringType(self.ENUM_SELECT)
        filteringType_name = filteringType_enum_selection.name
        return filteringType_name

    def obtainFilterConfiguration(self ):
        
        """    
        Returns the whole Filtering Configuration as a String
        ----------        
              
        Returns: 
        ----------                
        Returns the whole Filtering Configuration.
      
        """  
        
        strForReturn = 'Kernel Size: ' + str(self.kernelSize.obtainKernelSize())  + '; Filter Type: ' + str(self.obtainFilteringType()) 
        
        return strForReturn
    
    
#==========================================================================
# END
#==========================================================================

