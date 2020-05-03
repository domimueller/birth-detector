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


#==========================================================================
# FUNCTIONS
#==========================================================================

class ContourDrawer:
    
    
    
    """
    A class used to Draw Contours into an Image.
    ...
    
    Attributes
        ----------        
    color: BGR
        color for contour drawing.     
    thickness: int
        thickness of drawing. -1 means filling the contour instead of drawing lines 
      
    Methods - See descriptions below.
    -------
    draw_contour_outline(img, cnts, color, thickness=1)
    draw_contour_points(img, cnts, color)    
    """ 
    
        
    def __init__(self):
        
        self.color = None
        self.thickness = None

    def draw_contour_outline(self, image, contours ):
    
        """ 
       
        draws the contour outline.
        -------              
      
        This function is based on the library OpenCV and the corresponding function cv2.drawContours.
        -------              
      
        Parameters: 
        -------                 
        image (Image): Image use for drawing
        contour: contours to draw 
        color: color for drawing
        thickness: thickness of drawing lines. thickness = -1 means filling the contour with color

        
        Returns: 
        -------              
        Nothing will be returned. 
      
        """
        color =  (0, 0, 0)
        thickness = -1
        for contour in contours:
            cv2.drawContours(image, [contour], 0, color, thickness)
        


    def draw_contour_points(self, image, contours, color):
        """ 
       
        draws points around a contour.
        -------              
      
        This function is based on the library OpenCV and the corresponding function cv2.circle.
        -------              
      
        Parameters:         -------              

        -------                 
        image (Image): Image use for drawing
        contour: contours to draw 
        color: color for drawing

        
        Returns: 
        -------              
        Image will be returned      
        """    
       
        for contour in contours:

            squeeze = np.squeeze(contour)

    
            for p in squeeze:
                p = tuple(p.reshape(1, -1)[0])
                       
                if len(p) > 1:     
                    cv2.circle(image, p , 2, color, -1)
                
        return image
#==========================================================================
# END
#==========================================================================