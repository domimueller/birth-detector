#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#==========================================================================
# ContourFinderConfiguration.py – DESCRIPTIONS
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


# Configuration for Console Output
TITLE = '############ CONTOUR FINDER CONFIGURATION ############'
DELIMITER = '; '
NEWLINE = '\n'
CV = 'cv2.'


#==========================================================================
# FUNCTIONS
#==========================================================================
class ContourFinderConfiguration:

    """
    A class used to represent the the Configruation needed to Segment and Binarize Images applying
    the Thresholding Technique


    -------
        Attributes
    ----------

    approxType: <<Enumeration>> ApproximationType
        Enumeration with Approximation Types
    ENUM_SELECT_APPROX : int
        Selection of Approximation Type. 
    minArea: int
        min area for contour to be considered
    finderType: <<Enumeration>> FinderType
        Enumeration with Finder Type        
    ENUM_SELECT_FINDER : int
        Selection of Finder Type.                 
    deleteCircles: Boolean        
        whether perfect circles should be considered or not 
    filterbyAngle: Boolean        
        whether Filtering the Contours by Angle is desired or not 

        
        

    
    Methods - see Descripton below
    -------
   obtainApproxType(self)
   obtainFinderType(self, )
   obtainMinArea(self)
   obtainDeleteCircles(self)
   obtainFilterbyAngle(self)
   obtainContourFinderConfiguration(self)
       
        
   """    
    
    def __init__(self, approxType, ENUM_SELECT_APPROX, finderType, ENUM_SELECT_FINDER, minArea,  deleteCircles, filterbyAngle):
        self.approxType = approxType
        self.ENUM_SELECT_APPROX = ENUM_SELECT_APPROX
        self.finderType = finderType
        self.ENUM_SELECT_FINDER = ENUM_SELECT_FINDER
        self.deleteCircles = deleteCircles
        self.minArea = minArea
        self.filterbyAngle = filterbyAngle


    def obtainApproxType(self, ):
        
        """    
        Returns whether the desired Contour Approximation Type
        ----------        
              
        Returns: 
        ----------                
        desired Approximation Type 
      
        """            
         
        approxType_enum_selection = self.approxType(self.ENUM_SELECT_APPROX)
        approxType_name = approxType_enum_selection.name
        approxType = CV + approxType_name
        return approxType 

    def obtainFinderType(self, ):
        
        """    
        Returns whether the desired Finder Type
        ----------        
              
        Returns: 
        ----------                
        desired Finder Type 
      
        """          
        
        finderType_enum_selection = self.finderType(self.ENUM_SELECT_FINDER)
        finderType_name = finderType_enum_selection.name
        finderType = CV + finderType_name 
        return finderType 


    def obtainMinArea(self, ):
    
        """    
        Returns min Area of a Contour in order to be considered
        ----------        
              
        Returns: 
        ----------                
        min Area of a Contour 
      
        """        
        return int(self.minArea)


    def obtainDeleteCircles(self, ):
        
        """    
        Returns whether circles should be considered or not
        ----------        
              
        Returns: 
        ----------                
        Consideration of circles or not 
      
        """              
       
        
        return self.deleteCircles


    def obtainFilterbyAngle(self, ):
        
        """    
        Returns whether Filtering by Angles is desired or not
        ----------        
              
        Returns: 
        ----------                
        Consideration of Angle Filtering or not
      
        """              
       
        
        return self.filterbyAngle

   

    def obtainContourFinderConfiguration(self, ):
        """ 
       
        Returns the Contour Finder as a string representation
        ----------        
              
        Returns: 
        ----------                
        Contour Finder as string. 
      
        """ 
        data = 'Approximation Type: ' + str(self.obtainApproxType())  + DELIMITER + 'Contour Finder Type: ' + str(self.obtainFinderType())+ DELIMITER + 'Contour Min Area: ' + str(self.obtainMinArea ())+ DELIMITER + 'Circle Deletion: ' + str(self.obtainDeleteCircles()) + DELIMITER+ 'Filter by Angle: ' + str(self.obtainFilterbyAngle()) 
        strForReturn = TITLE + NEWLINE + data + NEWLINE + NEWLINE      
        return strForReturn
    
                
        
        pass


