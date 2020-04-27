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


#==========================================================================
# FUNCTIONS
#==========================================================================

def main():
#
    readerMimeType = MimeType.MimeType(major = 'image', minor='jpeg', extension='jpg')
    
    readerFilepath = Filepath.Filepath(filePath = 'C:/Users/domim/OneDrive/Desktop/bilder/seitlich/', fileName = '1',  mimeType=readerMimeType)
    
    imageReader = ImageReader.ImageReader(readerFilepath)
    
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

    def controlImageReader(self, ):
        pass

    def controlTraitRecognitor(self, ):
        pass

    def controlScoreCalculator(self, ):
        pass

    def controlImageWriter(self, ):
        pass

    def controlImageProcessor(self, ):
        pass

    def controlContourFinder(self, ):
        pass

    def controlContourDrawer(self, ):
        pass

#==========================================================================
# MAIN
#==========================================================================

if __name__ == '__main__':
    main()
       
#==========================================================================
# END
#==========================================================================


