#!/usr/bin/python
#-*- coding: utf-8 -*-

#==========================================================================
# ContourDrawer.py – DESCRIPTIONS 
#==========================================================================

"""
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>
"""


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================
import cv2 
import numpy as np

#==========================================================================
# CONSTANTS
#==========================================================================

# DRAWING MODE 1 means that its only 1 contour drawed once. In this SW-Architecute
# other configuration is not usefull
DRAWING_MODE_DEFAULT = 0
DRAWING_MODE_ALL = -1

DRAWING_RADIUS = 2

#==========================================================================
# FUNCTIONS
#==========================================================================

class ContourDrawer:
    
    """
    A class used to Draw Contours into an Image.
    ...
    
    Attributes
        ----------        
      
    Methods - See descriptions below.
    -------
    drawContourOutline(image, contour, thickness, color)
    drawContourPoints( image, contour, thickness, color) 
    fillCircle(image, contour, thickness, color ):
    """ 
    
       
    def __init__(self):
        pass
    
    
    def drawContourOutline(self, image, contours, color, thickness):
    
        """ 
       
        draws the contour outline.
        -------              
      
        This function is based on the library OpenCV and the corresponding function cv2.drawContours.
        -------              
      
        Parameters: 
        -------                 
        image (Image): Image use for drawing
        contours: contours to draw 
        thickness: thickness of drawing lines. thickness = -1 means filling the contour with color
        color: BGR Drawing Color 
   
        Returns: 
        -------              
        Image
      
        """

        for contour in contours:
            cv2.drawContours(image, [contour], DRAWING_MODE_DEFAULT, color, thickness)
        return image


    def drawContourPoints(self, image, contours, color, thickness):
      
        """ 
       
        draws points around a contour.
        -------              
      
        This function is based on the library OpenCV and the corresponding function cv2.circle.
        -------              
      
        Parameters:         -------              

        -------                 
        image (Image): Image use for drawing
        contours: contours to draw 
        thickness: thickness of drawing lines. thickness = -1 means filling the contour with color
        color: BGR Drawing Color 
    
        Returns: 
        -------              
        Image will be returned      
        """   
        
        for contour in contours:

            squeeze = np.squeeze(contour)
            for point in squeeze:
                point = tuple(point.reshape(1, -1)[0])
                       
                if len(point) > 1:     
                    cv2.circle(image, point , DRAWING_RADIUS, color, thickness)
                
        return image
            
    def fillCircle(self, image, contours, color, thickness):
      
        """ 
       
        creats minimal enclosing Circle and fills it with color.
        -------              
      
        This function is based on the library OpenCV and the corresponding function cv2.minEnclosingCircle.
        -------              
      
        Parameters:                    

        -------                 
        image (Image): Image use for drawing
        contours: contours to draw 
        thickness: thickness of drawing lines. thickness = -1 means filling the contour with color
        color: BGR Drawing Color 
    
        
        Returns: 
        -------              
        Image will be returned      
        """       
                  
        for contour in contours:    
            # draw minimal circle around contour
            (x,y),radius = cv2.minEnclosingCircle(contour)
            center = (int(x),int(y))
            radius = int(radius)
            # draw the circles in the originalImage, not the processing image (which is binary!).
            cv2.circle(image,center,radius,color,thickness)
            
        return  image

