#!/usr/bin/env python3
#-*- coding: utf-8 -*-



#==========================================================================
# ImageProcessor.py – DESCRIPTIONS 
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



#==========================================================================
# FUNCTIONS
#==========================================================================

class ImageProcessor:
    
        
    """
    A class used to represent and implement the functionality for the Image Processor.
    The Image Processor gets a File from Image Reader and optimizes Brightness, Contrast, converts Colorspace
    and applys filters on the Image. Furthermore, the Image will be binarized using the thresholding technique.
    ...
    
    Attributes
        ----------        
    image: Image
        Image to process.     
    imageReader : ImageReader
         brings the data and functionality of the ImageReader.
    brightenConfig : BrightenConfiguration
         brings the data needed to raise Brightness and histogram equalization on the image.  
    colorspaceConvertConfig : ColorSpaceConversion
         brings the data needed to convert Images to different ColorSpaces. 
         Most Important Conversions: BGR to Grayscale and BGR to YUV and vise versa .           
    filterConfig : FilterConfiguration
         brings the data needed to apply a Filter to the Image. Most Important Filter: GaussianBlur
    threshConfig : ThresholdingConfiguration
         brings the data needed to Binarize an Image based on a threshold.  

    Methods
    -------
    brightenImage(image, config)
    convertColorSpace(image, config)
    filterImage(self, image, config)
    segmentImage(self, image, config)
         See descriptions below.
    """ 
    
    def __init__(self):
        self.image = None
        self.reader = None
        self.brightenConfig = None
        self.colorspaceConvertConfig = None
        self.filterConfig = None
        self.threshConfig = None
        self.writer = None
        

    def brightenImage(self, image, config):
        
        """ 
       
        Raises the Brightness and performs Histogram Equalization on the image.
        -------              
      
        The Brightness will be raised by creating a new array of a the same shape and type as the image. 
        This new array will first be filled with ones and then multiplied with a configurable factor. 
        By using the function cv2.add(), the image will be modified based on the new array. 
        After that, Histogram Equalization will be done by performing cv2.createCLAHE().
        -------              
      
        Parameters: 
        -------                 
        image (Image): Image to process. 
        config (BrightenConfiguration): Configuration Data to raise Brighness 
        and perform Histogram Equalization. 

        
        Returns: 
        -------              
        New Image will be returned 
      
        """  
        
        self.image = image
        self.brightenConfig = config
        
        print(self.brightenConfig.obtainBrightenConfiguration())
        
        ## check if Brightening is desired and then perform the brightening based on the Brightener Factor
        if self.brightenConfig.obtainBrighteningImage()== True: 
            M = np.ones(self.image.shape, dtype="uint8")*self.brightenConfig.obtainBrightenerFactor()  
            self.image = cv2.add(self.image, M)
       
        
        ## check if Equalizing is desired and then perform the equalizing based on the desired Method
        if self.brightenConfig.obtainEqualizingImage()== True: 
            
           ## check if selected Equalizing Type = CLAHE. Enumeration Selection 
           # done by enumeration Config variable ENUM_SELECT_EQUALIZING in ImageAnalysisController.py
           if self.brightenConfig.obtainEqualizingType() == 'CLAHE':
                cla = cv2.createCLAHE(clipLimit= self.brightenConfig.obtainClipLimit())
                H, S, V = cv2.split(cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV))
                eq_V = cla.apply(V)
                self.image = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2BGR)            
        
        return self.image
   
    def convertColorSpace(self, image, config):

        """ 
       
        Converts the Image to different Color Spaces.
        -------              
      
        The Conversion between the Color Spaces will be performed by using the 
        function cv2.cvtColor() of the OpenCV Library.  The most important 
        Conversions are from BGR to Grayscale and from BGR to YUV and vise versa 
        
        -------              
      
        Parameters: 
        -------                 
        image (Image): Image to process. 
        config (ColorSpaceConversion): Configuration Data to convert between
        different Color Spaces 

        
        Returns: 
        -------              
        New Image will be returned  
      
        """          
        self.image = image
        self.colorspaceConvertConfig = config
     
        print(self.colorspaceConvertConfig.obtainColorSpaceConversion())
        
        ## check if Filtering is desired and then perform the filtering based on the desired Method
        if self.colorspaceConvertConfig.obtainConvertingImage()== True: 
                      
           # pass the value given by enumeration to the Function cv2.cvtColor() 
           conversionParameter = 'cv2.' + self.colorspaceConvertConfig.obtainConversionType()
           self.image = cv2.cvtColor(self.image, eval(conversionParameter))
        
        return self.image

    def filterImage(self, image, config):
       
        """ 
       
        Applys a Filter to the Image.
        -------              
      
        The Filter generates a smooth Image and reduces Noise. At the Moment, 
        only the Application of cv2.GaussianBlur() is implemented. Gaussian Blur works with 
        a Kernel, which size is configurable via the Filter Configuration.
        The Implementation of further Filters is possible. 
        
        -------              
      
        Parameters: 
        -------                 
        image (Image): Image to process. 
        config (FilterConfiguration): Configuration Data to determine Kernel Size
        and Apply the Filter.

        
        Returns: 
        -------              
        Nothing will be returned 
        
        """    
        self.image = image
        self.filterConfig = config
     
        print(self.filterConfig.obtainFilterConfiguration())
        
        ## check if Filtering is desired and then perform the filtering based on the desired Method
        if self.filterConfig.obtainFilteringImage()== True: 
                      
           ## check if selected Filtering Type = GAUSSIANBLUR. Enumeration Selection 
           # done by enumeration Config variable ENUM_SELECT_FILTERING in ImageAnalysisController.py
           if self.filterConfig.obtainFilteringType() == 'GAUSSIANBLUR':        
               self.image = cv2.GaussianBlur(self.image, 
                                      (self.filterConfig.kernelSize.obtainKernelWidth(), self.filterConfig.kernelSize.obtainKernelLength()), 
                                      0)
        return self.image

    def segmentImage(self, image, config):

        """ 
       
        Performs Image Segmentation.
        -------              
      
        Image Segementation partitions the Image into different regions. This will be done
        by applying either simple or adaptive Thresholding technique. In Simple Thresholding, 
        for every pixel, the same threshold value is applied. In Adaptive Thresholding, the 
        threshold for small regions of the image will be determined. So we get different 
        thresholds for different regions of the same image and it gives us better results 
        for images with varying illumination.
        In simple as well as in adaptive Thresholding, different Methods are configurable
        via the Thresholding Configuration.
        -------              
      
        Parameters: 
        -------                 
        image (Image): Image to process. 
        config (ThresholdingConfiguration): Configuration Data to determine Thresholding
        Methods and there Parameters.

        
        Returns: 
        -------              
        New Image will be returned  
        
        """   
        
        self.threshConfig = config
        self.image = image        
        print(self.threshConfig.obtainThresholdingConfiguration())
        
        ## check if Thresholding is desired and then perform the threshilding based on the desired Method
        if self.threshConfig.obtainThresholdingImage()== True: 
            
           ## check if selected Thresholding Method = THRESHOLD. Enumeration Selection 
           # done by enumeration Config variable ENUM_SELECT_THRESHOLDING in ImageAnalysisController.py
           
           if self.threshConfig.obtainThresholdingMethod() == 'THRESHOLD':    
               type_parameter = 'cv2.' + str(self.threshConfig.obtainThresholdingType())
               rect, self.image = cv2.threshold(self.image , 
                                                self.threshConfig.obtainThreshold(), 
                                                self.threshConfig.obtainMaximumValue(), 
                                                eval(type_parameter))
               
               
            ## check if selected Thresholding Method = ADAPTIVE_THRESHOLD. Enumeration Selection 
           # done by enumeration Config variable ENUM_SELECT_THRESHOLDING in ImageAnalysisController.py              
           elif self.threshConfig.obtainThresholdingMethod() == 'ADAPTIVE_THRESHOLD':  
                              

               print(self.threshConfig.adaptiveThresholdingConfiguration.obtainAdaptiveThresholdingConfiguration())
               
               thresholding_type_parameter = 'cv2.' + str(self.threshConfig.obtainThresholdingType())
               adaptive_type_parameter = 'cv2.' + str(self.threshConfig.adaptiveThresholdingConfiguration.obtainThresholdingType())

               
               self.image = cv2.adaptiveThreshold(self.image, 
                                                         self.threshConfig.obtainMaximumValue(), 
                                                         eval(adaptive_type_parameter),
                                                         eval(thresholding_type_parameter),
                                                         self.threshConfig.adaptiveThresholdingConfiguration.obtainBlockSize(),
                                                         self.threshConfig.adaptiveThresholdingConfiguration.obtainCSubtractor())               
               
        return self.image        
    


#==========================================================================
# END
#==========================================================================