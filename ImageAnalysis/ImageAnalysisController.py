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
import ContourFinderConfiguration 
import ImageAnalysisConfiguration as config


#==========================================================================
# CONSTANTS 
#==========================================================================

# The Configuration of the Image Analysis Controller is sourced in a 
# separate file name ImageAnalysisConfiguration.py 
# see: ImageAnalysisConfiguration as config


TRAIT_RECOGNITOR_TITLE = '############ RESULT OF THE TRAIT RECOGNITOR ############'
NEWLINE = '\n'

INFORMATION_MSG_NO_COW = 'NO COW DETECTED IN THIS IMAGE. '
INFORMATION_MSG_LATERAL_LYING_COW= 'IT APPEARS, THAT THE COW IS IN LATERAL LYING POSITION. CHECK THE CAMERA!'
INFORMATION_MSG_STANDING_COW = 'IT APPEARS, THAT THE COW IS STANDING. PLEASE STAY PATIENT AND HANG ON!'
INFORMATION_MSG_STANDING_COW_OR_NO_COW = 'ITS NOT SURE: EITHER THE COW IS STANDING OR NO COW IS DETECTED.'

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
        
        
        self.controlImageReader()
        self.controlImageProcessor( AdvancedUnimportantColorRange = config.ADVANCED_UNIMPORTANT_COLOR_RANGE)
        
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
        
        return self.image
        
    def controlImageProcessor(self, AdvancedUnimportantColorRange ):
       
        """ 
       
        Controls the Execution of the ImageProcessor
        -------              
      
        This function  controls the ImageProcessor. In this Project, Image Processing means f.e. brightening, 
        filtering or binarizationing Images in order to facilitate contour detection.
        -------              
      
        Parameters: 
        -------                 
        provideUnimportantColorRange (Boolean)
            determines wheter color Ranges of unimportant areas are known or not
        
        Returns: 
        -------              
        nothing will be returned. 
      
        """  
        # set MimeType for files to be written
        writerMimeType = MimeType.MimeType(major = config.WRITER_MAJOR, 
                                           minor= config.WRITER_MINOR, 
                                           extension=config.WRITER_EXTENSION)   
        
        
        
        # image analysis will be performend on the processingImage which is a copy of the original image
        self.processingImage = self.obtainImage().copy()
        segmenentingImage = self.image.copy()

        #=====================================
        ###### BRIGHTENING ######
        #=====================================   

        # apply brightening configuration
        brightenConfig = BrightenConfiguration.BrightenConfiguration(brighteningImage = config.BRIGHTENING_IMAGE_FALSE, 
                                                    brightenerFactor = config.BRIGHTENER_FACTOR, 
                                                    equalizingImage = config.EQUALIZING_IMAGE_FALSE, 
                                                    clipLimit = config.CLIP_LIMIT , 
                                                    equalizingType = EqualizingType.EqualizingType, 
                                                    ENUM_SELECT = config.ENUM_SELECT_EQUALIZING)

        # improve brightness and contrast of original image to facilitate export for report
        self.processingImage= self.imageProcessor.brightenImage(image = self.obtainProcessingImage(), config = brightenConfig )


        #==================================
        # write intermediate result to file
        #==================================
        writerFilepath = Filepath.Filepath(filePath = config.WRITER_FILE_PATH_MAIN, 
                                           fileName = config.WRITER_FILE_NAME_BRIGHTENED,  
                                           mimeType= writerMimeType)
        
        
        self.controlImageWriter( filepathAndName=writerFilepath, image= self.processingImage ) 

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
        #self.Image = self.imageProcessor.filterImage(image = self.obtainImage(), config = filterConfig )
        
 
        #==================================
        # write intermediate result to file
        #==================================
        
        writerFilepath = Filepath.Filepath(filePath = config.WRITER_FILE_PATH_MAIN, 
                                           fileName = config.WRITER_FILE_NAME_FILTERED,  
                                           mimeType= writerMimeType)
        
        
        self.controlImageWriter( filepathAndName=writerFilepath, image= self.processingImage )         
       
        


        #=====================================
        ###### UNIMPORTANT AREA DETECTION ######
        #=====================================
        
        colorRange = AdvancedUnimportantColorRange 
        
            
        # PREPARING: COLOR SPACE CONVERSION #

        colorspaceConvertConfig = ColorSpaceConversion.ColorSpaceConversion(convertingImage = config.CONVERTING_IMAGE, 
                                                              conversionType = ColorSpaceConversionType.ColorSpaceConversionType,           
                                                              ENUM_SELECT = config.ENUM_SELECT_CONVERTING_BGR2HSV)
        
        #IMPORTANT: At this point, the original Image is required, because it is beeing used for inRange() funtion (Color Ranges should not been changed)
        self.processingImage = self.imageProcessor.convertColorSpace(image = self.processingImage, config = colorspaceConvertConfig )

        
        # Build a List with the Color Ranges. More ranges can be added
        
        unimportantColorRanges=  config.defaultColorRanges       
        
        # adding more Color Ranges is possible
        if colorRange == True:   
            additionalColors = config.additionalUnimportantColorRanges
            
            for additionalColor in additionalColors:

                unimportantColorRanges.append(additionalColor )
        
        self.processingImage =  self.processingImage.copy() 
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
 
        ## configurate the ContourFinder
        finderConfig = ContourFinderConfiguration.ContourFinderConfiguration(
                        approxType = ApproximationType.ApproximationType,
                        ENUM_SELECT_APPROX = config.ENUM_SELECT_APPROX,
                        finderType = FinderType.FinderType,
                        ENUM_SELECT_FINDER = config.ENUM_SELECT_FINDER,
                        minArea = config.MIN_AREA,
                        deleteCircles = config.DELETE_CIRCLES_FALSE)       
        
        ## call Contour Finder with the unimportant area mask as argument
        contours, self.processingImage = self.controlContourFinder(self.processingImage, finderConfig )
        
        self.processingImage = self.controlContourDrawer(contours=contours, 
                                                         drawingMode = config.CIRCLE_DRAWING_MODE, 
                                                         color =config.BLACK.obtainDrawingColor(), 
                                                         thickness=config.THICKNESS_FILL)
        
                      

        #==================================
        # write intermediate result to file
        #==================================
        writerFilepath = Filepath.Filepath(filePath = config.WRITER_FILE_PATH_MAIN, 
                                           fileName = config.WRITER_FILE_NAME_UNIMPORTANT_AREAS_IMAGE,  
                                           mimeType= writerMimeType)
        
        
        self.controlImageWriter( filepathAndName=writerFilepath, image= self.processingImage )        
        

        #=====================================
        ###### Thresholding ######
        #=====================================
        ##BRIGHTENING as preparation for thresholding
           

        brightenConfig = BrightenConfiguration.BrightenConfiguration(brighteningImage = config.BRIGHTENING_IMAGE_TRUE, 
                                                    brightenerFactor = config.BRIGHTENER_FACTOR, 
                                                    equalizingImage = config.EQUALIZING_IMAGE_FALSE, 
                                                    clipLimit = config.CLIP_LIMIT , 
                                                    equalizingType = EqualizingType.EqualizingType, 
                                                    ENUM_SELECT = config.ENUM_SELECT_EQUALIZING)

        # improve brightness and contrast of original image to facilitate export for report
        self.processingImage= self.imageProcessor.brightenImage(image = self.obtainProcessingImage(), config = brightenConfig )

           
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
      
        ## here I can demonstrate difference between Processing Image (my intermidiate results and Image)
        ## If I do obtainImage() f.e. Light bulb will be detected
        segmenentingImage  =  self.obtainProcessingImage().copy() 
        segmenentingImage = cv2.cvtColor(segmenentingImage, cv2.COLOR_BGR2GRAY)        
        
        
        


        ## self.processingImage is Binary (returned Image)!
        ## image segmentation wants brightened image!
        segmenentingImage = self.imageProcessor.segmentImage(image =  segmenentingImage, config = threshConfig )
        
       
        #==================================
        # write intermediate result to file
        #==================================
        writerFilepath = Filepath.Filepath(filePath = config.WRITER_FILE_PATH_MAIN, 
                                           fileName = config.WRITER_FILE_NAME_THRESHOLDED_MASK,  
                                           mimeType= writerMimeType)
        
        
        self.controlImageWriter( filepathAndName=writerFilepath, image= segmenentingImage )  
        
        

        ## configurate the ContourFinder
        finderConfig = ContourFinderConfiguration.ContourFinderConfiguration(
                        approxType = ApproximationType.ApproximationType,
                        ENUM_SELECT_APPROX = config.ENUM_SELECT_APPROX,
                        finderType = FinderType.FinderType,
                        ENUM_SELECT_FINDER = config.ENUM_SELECT_FINDER,
                        minArea = config.MIN_AREA,
                        deleteCircles = config.DELETE_CIRCLES_TRUE)       
       
        

        ## call Contour Finder with the segmentation result as argument
        contours, segmenentingImage= self.controlContourFinder(segmenentingImage, finderConfig )

        segmenentingImage = self.controlContourDrawer(contours=contours, 
                                                         drawingMode = config.OUTLINE_DRAWING_MODE, 
                                                         color=config.RED.obtainDrawingColor(),
                                                         thickness=config.THICKNESS_FILL)
        
        #==================================
        # write intermediate result to file
        #==================================
        writerFilepath = Filepath.Filepath(filePath = config.WRITER_FILE_PATH_MAIN, 
                                           fileName = config.WRITER_FILE_NAME_THRESHOLDED_IMAGE,  
                                           mimeType= writerMimeType)
        
        
        self.controlImageWriter( filepathAndName=writerFilepath, image= segmenentingImage )  
        
        #=====================================
        ###### Trait Recognition ######
        #=====================================






        brightenConfig = BrightenConfiguration.BrightenConfiguration(brighteningImage = config.BRIGHTENING_IMAGE_TRUE, 
                                                    brightenerFactor = config.BRIGHTENER_FACTOR, 
                                                    equalizingImage = config.EQUALIZING_IMAGE_TRUE, 
                                                    clipLimit = config.CLIP_LIMIT , 
                                                    equalizingType = EqualizingType.EqualizingType, 
                                                    ENUM_SELECT = config.ENUM_SELECT_EQUALIZING)

        #improve brightness and contrast of original image to facilitate export for report if above brightening config is changed to True
        analysisImage= self.imageProcessor.brightenImage(image = self.obtainImage(), config = brightenConfig )
        
        
        lateralLyingContours, standingContours, analysedImage  = self.controlTraitRecognitor(contours, analysisImage,  finderConfig)
        print(NEWLINE+NEWLINE )
        print(TRAIT_RECOGNITOR_TITLE)

        # if typical Conours for standing and lying apprear, print the msg that lateral lying is detected.
        # It is better, if the farmer checks the camera and sees that the cow is no in an imminent birth position than
        # the farmer is beeing kept in the opinion that no action is needed.
        
        if standingContours is not None or lateralLyingContours is not None:
          
 

             if len(lateralLyingContours) >= config.MIN_NUMBER_LYING_CONTOURS:   
                print(INFORMATION_MSG_LATERAL_LYING_COW)  
                self.processingImage = self.controlContourDrawer(contours =lateralLyingContours, 
                                                         drawingMode = config.OUTLINE_DRAWING_MODE, 
                                                         color=config.RED.obtainDrawingColor(),
                                                         thickness=config.THICKNESS_FILL)                         

             elif len(lateralLyingContours) < config.MIN_NUMBER_LYING_CONTOURS:  
                print(INFORMATION_MSG_STANDING_COW_OR_NO_COW)

                self.processingImage = self.controlContourDrawer(contours =lateralLyingContours, 
                                                         drawingMode = config.OUTLINE_DRAWING_MODE, 
                                                         color=config.RED.obtainDrawingColor(),
                                                         thickness=config.THICKNESS_FILL)
             else:
                    self.processingImage = self.controlContourDrawer(contours =lateralLyingContours, 
                                         drawingMode = config.OUTLINE_DRAWING_MODE, 
                                         color=config.RED.obtainDrawingColor(),
                                         thickness=config.THICKNESS_FILL)
                    print(INFORMATION_MSG_NO_COW)

        else:
            print(INFORMATION_MSG_NO_COW)
        #==================================
        # write intermediate result to file
        #==================================
        writerFilepath = Filepath.Filepath(filePath = config.WRITER_FILE_PATH_MAIN, 
                                           fileName = config.WRITER_FILE_NAME_ANALYSED_IMAGE,  
                                           mimeType= writerMimeType)
        
        
        self.controlImageWriter( filepathAndName=writerFilepath, image= self.processingImage )                       

    def controlContourFinder(self, image,  finderConfig ):
 
        """ 
       
        Controls the Execution of the ContourFinder.
        -------              
      
        This function  controls the ContourFinder. In this Project, finding Contours is 
        strongly  related to the OpenCV function: cv.findContours().

        -------              
      
        Parameters: 
        -------                 
        processingImage: Image for analysis (Binary Image!)
        finderConfig: ContourFinderConfiguration
        
        Returns: 
        contours : Contours
        processingImage : Image
      
        """  
        image = image.copy()

        contours, image = self.contourFinder.findContours(image, self.obtainImage(), finderConfig)
        
 
        self.contourFinder.countContours(contours)

       
        return (contours, image) 
    
    def controlContourDrawer(self, contours, drawingMode, color, thickness ):
        
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
        processingImage : Image
        
        

        """  
        
        #=====================================
        ###### IMPORTANT NOTE FOR USAGE OF DRAWER ######
        #=====================================   
        
        
        # If copy is been done, only the copy will be used for drawing. That means, that every
        # intermediate step will be used for analysis, but the drawing of the last steps will not 
        # be visible in the image
        image = self.obtainProcessingImage().copy()
        
        # if the drawing of every step of the processing is required, dont do the copy.
        #image = self.obtainProcessingImage()
        
        if drawingMode == config.OUTLINE_DRAWING_MODE:
            image = self.contourDrawer.drawContourOutline(image, contours, color, thickness )
        
        elif drawingMode == config.POINTS_DRAWING_MODE:
            image = self.contourDrawer.drawContourPoints(image, contours, color, thickness)
        elif drawingMode == config.CIRCLE_DRAWING_MODE:        
            image = self.contourDrawer.fillCircle(image, contours, color, thickness )
            
                       
        return image
        
        
    def controlTraitRecognitor(self, contours, image,  finderConfig ):
        
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
            
        lateralLyingContours, originalImage = self.traitRecognitor.detectLateralLyingClow(contours, image,  finderConfig)
        standingContours = self.traitRecognitor.detectStandingCow(contours, image,  finderConfig)

       
        return (lateralLyingContours, standingContours, originalImage)
    
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


