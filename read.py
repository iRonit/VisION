#!/usr/bin/python
from camera import *
from ocr import *
from speech import *
from wifi import *

IMAGE_FILE = '/home/pi/image.jpg'
TEXT_FILE = 'ocr.txt'


cam = Cam(IMAGE_FILE)             #Creating a camera object with output image path set
cam.capture_image()               #capturing image 

ocr = OCR(IMAGE_FILE,TEXT_FILE)   #creating an OCR object with input image file and output text file
if(wifi_is_connected):            #checking if the raspberry pi
  ocr.convert_matlab()            #is connected to
else:                             #a network throught wifi adapter
  ocr.convert_tesseract()         #and proceed accordingly
  
speech = Speech('Male','English') #configuring the speech object
speech.speak(TEXT_FILE)           #corresponding output audio for the input image
