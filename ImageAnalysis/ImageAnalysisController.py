#!/usr/bin/env python3
#-*- coding: utf-8 -*-



#==========================================================================
# ImageController.py – DESCRIPTIONS 
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
    # 3. Build WRITER_FILE_* Dictionary
    # 4. Add Dictionary to List: WRITER_FILES

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
    imageWriter = ImageWriter.ImageWriter()       
    imageProcessor = ImageProcessor.ImageProcessor()       
    contourFinder = ContourFinder.ContourFinder()       
    contourDrawer = ContourDrawer.ContourDrawer()       
    
    
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
    ATTRIBUTE : TYPE
        DESCRIPTION.


    Methods
    -------
   FUNCTION(self, PARAMETER):
        see Descripton below
        
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
        
        self.controlImageReader()

    def controlImageReader(self ):
        
        readerMimeType = MimeType.MimeType(major = READER_MAJOR, 
                                           minor= READER_MINOR, 
                                           extension=READER_EXTENSION)   
        
        readerFilepath = Filepath.Filepath(filePath = READER_FILE_PATH, 
                                           fileName = READER_FILE_NAME,  
                                           mimeType=readerMimeType)
        
        self.image = self.imageReader.readImage( filePathAndName = readerFilepath ) 
        
        #jump to the next function
        self.controlTraitRecognitor()
        
    def controlTraitRecognitor(self ):

        #jump to the next function
        self.controlScoreCalculator()

    def controlScoreCalculator(self ):

        #jump to the next function
        self.controlImageWriter()

    def controlImageWriter(self ):
      
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
        
        
        # Build a List with this writerFilepaths
        writerFilepaths = [writerFilepath_1, writerFilepath_2, writerFilepath_3 ]                                   
        
        self.image = self.imageWriter.writeImages( image = self.obtainImage(), filePathAndNames = writerFilepaths  ) 
        
        #jump to the next function
        self.controlImageProcessor()

    def controlImageProcessor(self ):
        
        #jump to the next function
        self.controlContourFinder()

    def controlContourFinder(self, ):
        
        #jump to the next function
        self.controlContourDrawer()

    def controlContourDrawer(self ):
        pass
    
    def obtainImage(self ):
        return self.image
    

#==========================================================================
# MAIN
#==========================================================================

if __name__ == '__main__':
    main()
       
#==========================================================================
# END
#==========================================================================


