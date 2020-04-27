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

import ImageReader 
import TraitRecognitor
import ScoreCalculator
import ImageWriter
import ImageProcessor
import ContourFinder
import ContourDrawer

import sys
sys.path.append('../VO-Library')

import Filepath
import MimeType

#==========================================================================
# CONSTANTS
#==========================================================================

#### INFORMATION AND CONFIGURATION FOR IMAGE READER ####
#Filepath and Filename for the Image Reader

READER_FILE_PATH = 'C:/Users/domim/OneDrive/Desktop/bilder/seitlich/'
READER_FILE_NAME = '1'

#Mimetype Information for Image Reader 
READER_MAJOR = 'image'
READER_MINOR = 'jpeg'
READER_EXTENSION = 'jpg' 


#### INFORMATION AND CONFIGURATION FOR IMAGE WRITER ####

# The Image Writer is capable of writing multiple Files of the same Mime Type
# Limitation to one Mime Type per Executionn due to faster configuration

#How to add further file writing: 
    # 1. Add WRITER_FILE_PATH_* Constant
    # 2. Add WRITER_FILE_NAME_* Constant
    # 3. Build writerFilePath_* variable with dataType Filepath (below)
    # 4. Add it to Tuple: writerFilepaths (below)

# Prepare Key-Value-Pairs. 
DICT_KEY_PATH = 'path'
DICT_KEY_NAME = 'name'

# Prepare FilePaths to write . 
WRITER_FILE_PATH_1 = 'C:/Users/domim/OneDrive/Desktop/bilder/neu/'
WRITER_FILE_PATH_2 = 'C:/Users/domim/OneDrive/Desktop/bilder/neu/'
WRITER_FILE_PATH_3 = 'C:/Users/domim/OneDrive/Desktop/bilder/neu/'

# Prepare FileNames to write . 
WRITER_FILE_NAME_1 = '1'
WRITER_FILE_NAME_2 = '2'
WRITER_FILE_NAME_3 = '3'




#Mimetype Information for Image Writer 
WRITER_MAJOR = 'image'
WRITER_MINOR = 'jpeg'
WRITER_EXTENSION = 'jpg'
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

    Methods - see Descriptons below
    -------
   controlImageReader(self )
   controlImageProcessor(self )   
   controlContourFinder(self )
   controlContourDrawer(self ) 
   controlTraitRecognitor(self ) 
   controlScoreCalculator(self )
   controlImageWriter(self )
   obtainImage(self )
        
        
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
        
        
        readerMimeType = MimeType.MimeType(major = READER_MAJOR, 
                                           minor= READER_MINOR, 
                                           extension=READER_EXTENSION)   
        
        readerFilepath = Filepath.Filepath(filePath = READER_FILE_PATH, 
                                           fileName = READER_FILE_NAME,  
                                           mimeType=readerMimeType)
        
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
        
        
        #jump to the next function
        self.controlContourFinder()

    def controlContourFinder(self ):
 
        """ 
       
        Controls the Execution of the ContourFinder.
        -------              
      
        This function  controls the ContourFinder. In this Project, finding Contours is 
        strongly  related to the OpenCV function: cv.findContours().

        -------              
      
        Parameters: 
        -------                 
        no parameters. 

        
        Returns: 
        -------              
        nothing will be returned.
      
        """  

        
        #jump to the next function
        self.controlContourDrawer()

    def controlContourDrawer(self ):
        
        """ 
       
        Controls the Execution of the ContourDrawer.
        -------              
      
        This function  controls the ContourDrawer. Drawing Contours is 
        strongly  related to the OpenCV function: cv.drawContours().
        -------              
      
        Parameters: 
        -------                 
        no parameters. 

        
        Returns: 
        -------              
        nothing will be returned.
      
        """  
        
    
        #jump to the next function
        self.controlTraitRecognitor()        
        
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
        self.controlImageWriter()


    
    def controlImageWriter(self ):
        
        """ 
       
        Controls the Execution of the ImageWriter.
        -------              
      
        This function builds the data (based on Constants above) that will be needed for Image Writing. 
        -------               
      
        Parameters: 
        -------                 
        no parameters. 

        
        Returns: 
        -------              
        nothing will be returned. 
      
        """  
        
      
        writerMimeType = MimeType.MimeType(major = WRITER_MAJOR, 
                                           minor= WRITER_MINOR, 
                                           extension=WRITER_EXTENSION)   
        
        writerFilepath_1 = Filepath.Filepath(filePath = WRITER_FILE_PATH_1, 
                                           fileName = WRITER_FILE_NAME_1,  
                                           mimeType=writerMimeType)
        
        
        writerFilepath_2 = Filepath.Filepath(filePath = WRITER_FILE_PATH_2, 
                                           fileName = WRITER_FILE_NAME_2,  
                                           mimeType=writerMimeType) 
        
        
        
        writerFilepath_3= Filepath.Filepath(filePath = WRITER_FILE_PATH_3, 
                                           fileName = WRITER_FILE_NAME_3,  
                                           mimeType=writerMimeType)
        
        
        # Build a Tuple with this writerFilepaths
        writerFilepaths = (writerFilepath_1, writerFilepath_2, writerFilepath_3 )                                   
        
        self.image = self.imageWriter.writeImages( image = self.obtainImage(), filePathAndNames = writerFilepaths  ) 
        
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
    
    
#==========================================================================
# MAIN
#==========================================================================

if __name__ == '__main__':
    main()
       
#==========================================================================
# END
#==========================================================================

