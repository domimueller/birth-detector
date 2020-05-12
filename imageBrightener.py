


#==========================================================================
# THIS FILE ONLY EXISTS FOR EXPERIMENT TESTING AND EXECUTION.
# THE FILE WILL BE REMOVED LATER ON
#==========================================================================


import numpy as np
import cv2 

## CONSTANTS

BRIGHTENING_FACTOR = 80
CLIP_LIMIT = 4.0
# input image
INPUT_FOLDER = 'C:/Users/domim/OneDrive/Desktop/bilder/brightening/'
OUTPUT_FOLDER = INPUT_FOLDER + 'bearbeitet/'
INPUT_FILENAME_1 = 'austrittklauen.jpg'
INPUT_FILENAME_2 = 'schleim.jpg'
INPUT_FILENAME_3 = 'schleimvagina.jpg'
INPUT_FILENAME_4 = 'schwanhebungkamerabild.jpg'
INPUT_FILENAME_5 = 'seitlichesligen.jpg'


inputfiles = [INPUT_FILENAME_1, INPUT_FILENAME_2,  INPUT_FILENAME_3, INPUT_FILENAME_4, INPUT_FILENAME_5]




for inputfile in inputfiles:
    inputfilepath = INPUT_FOLDER+inputfile       
    image = cv2.imread(inputfilepath)
   
    M = np.ones(image.shape, dtype="uint8")*BRIGHTENING_FACTOR  
    image = cv2.add(image, M)
   
    clahe = cv2.createCLAHE(clipLimit= CLIP_LIMIT)
    H, S, V = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
    eq_V = clahe.apply(V)
    image = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2BGR)            

    outputfile =   OUTPUT_FOLDER+inputfile             
    
    cv2.imwrite(outputfile, image)
