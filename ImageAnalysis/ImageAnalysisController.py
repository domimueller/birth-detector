#!/usr/bin/env python3
#-*- coding: utf-8 -*-



#==========================================================================
# ImageAnalysisController.py – DESCRIPTIONS 
#==========================================================================

"""
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>
"""


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================

## Import Classes for Functionality
import numpy as np
import cv2 


import ImageReader 
import TraitRecognitor
import ScoreCalculator
import ImageWriter
import ImageProcessor
import ContourFinder
import ContourDrawer

import sys
sys.path.append('../VO-Library')

## Import Value Objects

import AdaptiveThresholdingConfiguration
import AdaptiveThresholdingType
import ApproximationType
import BGR
import BrightenConfiguration
import ColorSpaceConversion
import ColorSpaceConversionType
import ContourFinderConfiguration
import EqualizingType
import Filepath
import FilterConfiguration
import FilteringType
import FinderType
import KernelSize
import MimeType
import ThresholdingType
import ThresholdingConfiguration
import ThresholdingMethod
import HSV
import ColorRange
import ImageAnalysisConfiguration as config


#==========================================================================
# CONSTANTS 
#==========================================================================

# The Configuration of the Image Analysis Controller is sourced in a 
# separate file name ImageAnalysisConfiguration.py 
# see: ImageAnalysisConfiguration as config

#==========================================================================
# FUNCTIONS
#==========================================================================

def main():
#

    imageReader = ImageReader.ImageReader()
    traitRecognitor = TraitRecognitor.TraitRecognitor()
    scoreCalculator = ScoreCalculator.ScoreCalculator()       
    imageProcessor = ImageProcessor.ImageProcessor()       
    contourFinder = ContourFinder.ContourFinder()       
    contourDrawer = ContourDrawer.ContourDrawer()   
    imageWriter = ImageWriter.ImageWriter()       
    
    
    
    ImageAnalysisController(imageReader = imageReader, traitRecognitor = traitRecognitor, 
                            scoreCalculator = scoreCalculator, imageWriter = imageWriter, 
                            imageProcessor = imageProcessor, contourFinder = contourFinder, 
                            contourDrawer = contourDrawer) 



class ImageAnalysisController:
    
    '''
    A class used to represent and implement the functionality for the Image Analysis Controller.
    Controls the Image reading and writing, Score calculation and Contour finding and drawing
    
    
    Attributes
    ----------        
    imageReader : ImageReader
         brings the data and functionality of the ImageReader.
    traitRecognitor : TraitRecognitor
         brings the data and functionality of the TraitRecognitor.
    scoreCalculator : ScoreCalculator
         brings the data and functionality of the ScoreCalculator.
    imageProcessor : ImageProcessor
         brings the data and functionality of the ImageProcessor.
    contourFinder : ContourFinder
         brings the data and functionality of the ContourFinder.
    contourDrawer : ContourDrawer
         brings the data and functionality of the ContourDrawer.         
    imageWriter : ImageWriter
         brings the data and functionality of the ImageWriter.
    image : Image
         always refers to the Image for displaying purpose
    processingImage : Image
         the image for processing and performing analysis
    Methods - see Descriptons below
    -------
   controlImageReader(self )
   controlImageProcessor(self )   
   controlContourFinder(self, processingImage )
   controlContourDrawer(self ) 
   controlTraitRecognitor(self ) 
   controlScoreCalculator(self )
   controlImageWriter(self )
   obtainImage(self )
   obtainProcessingImage(self )    
        
    '''
    
    def __init__(self, imageReader, traitRecognitor, scoreCalculator, 
                 imageWriter, imageProcessor, contourFinder,contourDrawer):
        
        self.imageReader = imageReader
        self.traitRecognitor = traitRecognitor
        self.scoreCalculator = scoreCalculator
        self.imageWriter = imageWriter
        self.imageProcessor = imageProcessor
        self.contourFinder = contourFinder
        self.contourDrawer = contourDrawer
        self.image = None
        self.Processingimage = None
        
        
        #jump to the first function
        self.controlImageReader()

    def controlImageReader(self ):

        """ 
       
        Controls the Execution of the ImageReader
        -------              
      
        This function builds the data (based on Constants above) that will be needed for Image Reading. 
        -------              
      
        Parameters: 
        -------                 
        no parameters. 

        
        Returns: 
        -------              
        nothing will be returned.
      
        """  
        
        
        readerMimeType = MimeType.MimeType(major = config.READER_MAJOR, 
                                           minor= config.READER_MINOR, 
                                           extension= config.READER_EXTENSION)   
        
        readerFilepath = Filepath.Filepath(filePath = config.READER_FILE_PATH, 
                                           fileName = config.READER_FILE_NAME,  
                                           mimeType= readerMimeType)
        
        self.image = self.imageReader.readImage( filePathAndName = readerFilepath ) 
        
        #jump to the next function
        self.controlImageProcessor()
        
    def controlImageProcessor(self ):
       
        """ 
       
        Controls the Execution of the ImageProcessor
        -------              
      
        This function  controls the ImageProcessor. In this Project, Image Processing means f.e. brightening, 
        filtering or binarizationing Images in order to facilitate contour detection.
        -------              
      
        Parameters: 
        -------                 
        no parameters. 

        
        Returns: 
        -------              
        nothing will be returned. 
      
        """  
        # set MimeType for files to be written
        writerMimeType = MimeType.MimeType(major = config.WRITER_MAJOR, 
                                           minor= config.WRITER_MINOR, 
                                           extension=config.WRITER_EXTENSION)   
        
        
        
        # image analysis will be performend on the processingImage which is a copy of the original image
        self.processingImage = self.image.copy()
        self.test = self.image.copy()
  

        #=====================================
        ###### BRIGHTENING ######
        #=====================================   

        # apply brightening configuration
        brightenConfig = BrightenConfiguration.BrightenConfiguration(brighteningImage = config.BRIGHTENING_IMAGE, 
                                                    brightenerFactor = config.BRIGHTENER_FACTOR, 
                                                    equalizingImage = config.EQUALIZING_IMAGE, 
                                                    clipLimit = config.CLIP_LIMIT , 
                                                    equalizingType = config.EqualizingType.EqualizingType, 
                                                    ENUM_SELECT = config.ENUM_SELECT_EQUALIZING)

        # improve brightness and contrast of original image to facilitate export for report
        self.image = self.imageProcessor.brightenImage(image = self.image, config = brightenConfig )

        
        #==================================
        # write intermediate result to file
        #==================================
        writerFilepath = Filepath.Filepath(filePath = config.WRITER_FILE_PATH_MAIN, 
                                           fileName = config.WRITER_FILE_NAME_BRIGHTENED,  
                                           mimeType= writerMimeType)
        
        
        self.controlImageWriter( filepathAndName=writerFilepath, image= self.image ) 

        #=====================================
        ###### FILTERING ######
        #===================================== 

        # apply filtering configuration
        kernelSize = KernelSize.KernelSize(width = config.KERNEL_WIDTH, 
                                           length = config.KERNEL_LENGTH)  
         
        filterConfig = FilterConfiguration.FilterConfiguration(filteringImage = config.FILTERING_IMAGE, 
                                                              kernelSize = kernelSize,
                                                              filteringType = FilteringType.FilteringType,           
                                                              ENUM_SELECT = config.ENUM_SELECT_FILTERING)
        
        self.processingImage = self.imageProcessor.filterImage(image = self.processingImage, config = filterConfig )
        
 
        #==================================
        # write intermediate result to file
        #==================================
        
        writerFilepath = Filepath.Filepath(filePath = config.WRITER_FILE_PATH_MAIN, 
                                           fileName = config.WRITER_FILE_NAME_FILTERED,  
                                           mimeType= writerMimeType)
        
        
        self.controlImageWriter( filepathAndName=writerFilepath, image= self.processingImage )         
       
        
        #====================================
        ###### COLOR SPACE CONVERSION ######
        #====================================      


        # apply color space conversion configuration

        colorspaceConvertConfig = ColorSpaceConversion.ColorSpaceConversion(convertingImage = config.CONVERTING_IMAGE, 
                                                              conversionType = config.ColorSpaceConversionType.ColorSpaceConversionType,           
                                                              ENUM_SELECT = config.ENUM_SELECT_CONVERTING_BGR2HSV)
        
        self.processingImage = self.imageProcessor.convertColorSpace(image = self.processingImage, config = colorspaceConvertConfig )



        #=====================================
        ###### UNIMPORTANT AREA DETECTION ######
        #=====================================
                  
        # Build a Tuple with the Color Ranges. More ranges can be added
        unimportantColorRanges= ( config.floorColorRange, config.lightColorRange )          
        
        ## self.processingImage (returned image) is Binary Image!
        self.processingImage = self.imageProcessor.detectUnimporantArea( image = self.processingImage, 
                                                            unimportantColorRanges = unimportantColorRanges)
        
        #==================================
        # write intermediate result to file
        #==================================
        writerFilepath = Filepath.Filepath(filePath = config.WRITER_FILE_PATH_MAIN, 
                                           fileName = config.WRITER_FILE_NAME_UNIMPORTANT_AREAS_MASK,  
                                           mimeType= writerMimeType)
        
        
        self.controlImageWriter( filepathAndName=writerFilepath, image= self.processingImage ) 
        
        
        ## call Contour Finder with the unimportant area mask as argument
        contours, self.processingImage = self.controlContourFinder(self.processingImage )
        self.processingImage = self.controlContourDrawer(contours=contours, drawingMode = config.CIRCLE_DRAWING_MODE)
        
        #==================================
        # write intermediate result to file
        #==================================
        writerFilepath = Filepath.Filepath(filePath = config.WRITER_FILE_PATH_MAIN, 
                                           fileName = config.WRITER_FILE_NAME_UNIMPORTANT_AREAS_IMAGE,  
                                           mimeType= writerMimeType)
        
        
        self.controlImageWriter( filepathAndName=writerFilepath, image= self.processingImage )        
        
        #=====================================
        ###### Important Area Detection ######
        #=====================================
               

        #=====================================
        ###### Thresholding ######
        #=====================================
           
        # apply adaptive thresholding configuration 
        adaptiveThresholdingConfiguration = AdaptiveThresholdingConfiguration.AdaptiveThresholdingConfiguration(
                                            thresholdingType= AdaptiveThresholdingType.AdaptiveThresholdingType,
                                            ENUM_SELECT = config.ENUM_SELECT_ADAPTIVE_THRESHOLDING,
                                            blockSize = config.BLOCK_SIZE, 
                                            cSubtractor = config.C_SUBTRACTOR)      
        # put all together 
        threshConfig = ThresholdingConfiguration.ThresholdingConfiguration(
                        thresholdingImage = config.THRESHOLDING_IMAGE,
                        threshold = config.THRESHOLD,
                        thresholdingMethod = ThresholdingMethod.ThresholdingMethod,
                        ENUM_SELECT_METHOD = config.ENUM_SELECT_METHOD,
                        thresholdingType = ThresholdingType.ThresholdingType,
                        ENUM_SELECT_TYPE = config.ENUM_SELECT_TYPE,
                        adaptiveThresholdingConfiguration = adaptiveThresholdingConfiguration,
                        maximumValue = config.MAXIMUM_VALUE)
        
        ## self.processingImage is Binary Image!
        self.processingImage = self.imageProcessor.segmentImage(image = self.processingImage, config = threshConfig )        
        
        #==================================
        # write intermediate result to file
        #==================================
        writerFilepath = Filepath.Filepath(filePath = config.WRITER_FILE_PATH_MAIN, 
                                           fileName = config.WRITER_FILE_NAME_THRESHOLDED_IMAGE,  
                                           mimeType= writerMimeType)
        
        
        self.controlImageWriter( filepathAndName=writerFilepath, image= self.processingImage )        
       
    

    def controlContourFinder(self, processingImage ):
 
        """ 
       
        Controls the Execution of the ContourFinder.
        -------              
      
        This function  controls the ContourFinder. In this Project, finding Contours is 
        strongly  related to the OpenCV function: cv.findContours().

        -------              
      
        Parameters: 
        -------                 
        processingImage: Image for analysis (Binary Image!)
        
        Returns: 
        -------              
        nothing will be returned.
      
        """  
        self.processingImage = processingImage
        
        # self.processingImage needs to be a binary Image!
        contours, self.processingImage = self.contourFinder.findContours(self.processingImage, self.obtainImage())
        
        self.contourFinder.countContours(contours)
       
        return (contours, self.processingImage) 
    
    def controlContourDrawer(self, contours, drawingMode=config.OUTLINE_DRAWING_MODE ):
        
        """ 
       
        Controls the Execution of the ContourDrawer.
        -------              
      
        This function  controls the ContourDrawer. Drawing Contours is 
        strongly  related to the OpenCV function: cv.drawContours().
        -------              
      
        Parameters: 
        -------                 
        contours: Contours derived from findContours()

        
        Returns: 
        -------              
        nothing will be returned.
      
        """  
        
        if drawingMode == 'OUTLINE':
            self.processingImage = self.contourDrawer.drawContourOutline(self.obtainProcessingImage(), contours )
        
        elif drawingMode == 'POINTS':
            self.processingImage = self.contourDrawer.drawContourPoints(self.obtainProcessingImage(), contours)
        elif drawingMode == 'CIRCLE':        
            self.processingImage = self.contourDrawer.fillCircle(self.obtainProcessingImage(), contours )
            
        #jump to the next function
        self.controlTraitRecognitor()
               
        return self.processingImage
        
        
    def controlTraitRecognitor(self ):
        
        """ 
       
        Controls the Execution of the TraitRecognitor.
        -------              
      
        This function  controls the TraitRecognitor. Traits are described in the report of the Bachelor Thesis.
        -------              
      
        Parameters: 
        -------                 
        no parameters.
        
        Returns: 
        -------              
        nothing will be returned. 
      
        """  
        

        #jump to the next function
        self.controlScoreCalculator()

    def controlScoreCalculator(self ):
        
        """ 
       
        Controls the Execution of the ScoreCalculator.
        -------              
      
        This function controls the ScoreCalculator. The Calculation of the Score is 
        based on the Interview Data of this Bachelor Thesis (Trait Ranking Data).
        -------                
      
        Parameters: 
        -------                 
        no parameters.

        
        Returns: 
        -------              
        nothing will be returned. 
      
        """  
        

        #jump to the next function
        #self.controlImageWriter()



    
    def controlImageWriter(self, filepathAndName, image ):
        
        """ 
       
        Controls the Execution of the ImageWriter.
        -------              
      
        This function builds the data (based on Constants above) that will be needed for Image Writing. 
        -------               
      
        Parameters: 
        -------                 
        filepathAndName: filepathAndName
            Location in Filesystem to write Image
        image: Image
            Image to write

        
        Returns: 
        -------              
        nothing will be returned. 
      
        """
        
        self.imageWriter.writeImage( image = image, filePathAndName = filepathAndName  ) 
        
    def obtainImage(self ):
        
        """ 
       
        Obtains the Image Attribute.
        -------              
      
        This function facilitates to obtain the Image Attribute. It does not provide any further Business Logic.
        -------                 
      
        Parameters: 
        -------                 
        no parameters. 

        
        Returns: 
        -------              
        Image for further processing. 
      
        """  
        
        return self.image
    
    def obtainProcessingImage(self ):
        
        """ 
       
        Obtains the Image for Processing and Analysis.
        -------              
      
        This function facilitates to obtain the Processing Image Attribute. It does not provide any further Business Logic.
        -------                 
      
        Parameters: 
        -------                 
        no parameters. 

        
        Returns: 
        -------              
        Image for further processing. 
      
        """  
        
        return self.processingImage
    
     
#==========================================================================
# MAIN
#==========================================================================

if __name__ == '__main__':
    main()
       
#==========================================================================
# END
#==========================================================================


