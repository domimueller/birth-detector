#!/usr/bin/env python3
#-*- coding: utf-8 -*-



#==========================================================================
# ContourRotator.py – DESCRIPTIONS 
#==========================================================================

"""
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>
"""


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================


import cv2 
import numpy as np

import sys
sys.path.append('../VO-Library')




#==========================================================================
# CONSTANTS
#==========================================================================

MOMENTS_M10 = 'm10'
MOMENTS_M00 = 'm00'
MOMENTS_M01 = 'm01'

# Configuration for Console Output
class ContourRotator:
    
    """
    A class used to represent and implement the functionality for the Ratation of Contours.
    ...
    
    Attributes
    ----------        
   
    Methods - See descriptions below.
    
    -------
    cart2pol(self, x, y )
    pol2cart(self,theta, rho )
    rotateContour(countour, angle)       

    
    """     
    def __init__(self):
        pass
    
    def cart2pol(self, x, y):
        
        """ 
        Converts Coordinates.

        -------              
        Converts Cartesian Coordinates to Polar Coordinates
      
        -------              
      
        Parameters: 
        -------                 
        x vlaue of Coornates as Cartesian System
        y vlaue of Coornates as Cartesian System

        
        Returns: 
        -------              
        theta: Polar Point in Coordinates 
        rho: Polar Point in Coordinates
        """              
        
         
        
        theta = np.arctan2(y, x)
        rho = np.hypot(x, y)
        return theta, rho

    def pol2cart(self, theta, rho):
        
        """ 
        Converts Coordinates.

        -------              
        Converts Polar Coordinates to Cartesian Coordinates
      
        -------              
      
        Parameters: 
        -------                 
        theta vlaue of Coornates as Polar System
        rho vlaue of Coornates as Polar System

        
        Returns: 
        -------              
        X: Cartesian Point in Coordinates 
        Y: Cartesian Point in Coordinates
        """              
         
        x = rho * np.cos(theta)
        y = rho * np.sin(theta)
        return x, y
    
    def rotateContour(self, contour, angle):
        
        
        """ 
        rotates the Contour.

        -------              
        Computates the new rotated Contour Matrix 
      
        -------              
      
        Parameters: 
        -------                 
        angle of rotation
        contour to rotate
        
        Returns: 
        -------              
        rotated contour
        """ 

        
        M = cv2.moments(contour)
        cx = int(M[MOMENTS_M10]/M[MOMENTS_M00])
        cy = int(M[MOMENTS_M01]/M[MOMENTS_M00])
    
        cnt_norm = contour - [cx, cy]
        
        coordinates = cnt_norm[:, 0, :]
        xs, ys = coordinates[:, 0], coordinates[:, 1]
        thetas, rhos = self.cart2pol(xs, ys)
        
        thetas = np.rad2deg(thetas)
        thetas = (thetas + angle) % 360
        thetas = np.deg2rad(thetas)
        
        xs, ys = self.pol2cart( thetas, rhos)
        
        cnt_norm[:, 0, 0] = xs
        cnt_norm[:, 0, 1] = ys
    
        cnt_rotated = cnt_norm + [cx, cy]
        cnt_rotated = cnt_rotated.astype(np.int32)
    
        return cnt_rotated
    

