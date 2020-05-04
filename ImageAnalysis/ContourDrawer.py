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
    drawContourOutline(img, cnts, color, thickness=1)
    drawContourPoints(img, cnts, color) 
    fillConjtour(self, image, contours ):
    """ 
    
        
    def __init__(self):
        pass

    def drawContourOutline(self, image, contours, color, thickness ):
    
        """ 
       
        draws the contour outline.
        -------              
      
        This function is based on the library OpenCV and the corresponding function cv2.drawContours.
        -------              
      
        Parameters: 
        -------                 
        image (Image): Image use for drawing
        contour: contours to draw 
        thickness: thickness of drawing lines. thickness = -1 means filling the contour with color

        
        Returns: 
        -------              
        Nothing will be returned. 
      
        """
        for contour in contours:
            cv2.drawContours(image, [contour], 0, color, thickness)
        
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
        contour: contours to draw 

        
        Returns: 
        -------              
        Image will be returned      
        """    
      
        for contour in contours:

            squeeze = np.squeeze(contour)

    
            for p in squeeze:
                p = tuple(p.reshape(1, -1)[0])
                       
                if len(p) > 1:     
                    cv2.circle(image, p , 2, color, thickness)
                
        return image
    
    def fillCircle(self, image, contours, color, thickness):
       
        """ 
       
        creats minimal enclosing Circle and fills it with color.
        -------              
      
        This function is based on the library OpenCV and the corresponding function cv2.minEnclosingCircle.
        -------              
      
        Parameters:         -------              

        -------                 
        image (Image): Image use for drawing
        contour: contours to draw 

        
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
    
#==========================================================================
# END
#==========================================================================