#!/usr/bin/python
import subprocess

public class OCR:
  
  def __init__(self, image_file, text_file):
    self.__image_file = image_file
    self.__text_file = text_file
    
  def set_image_file(self,image_file):
    self.__image_file = image_file
    
  def get_image_file(self):
    return self.__image_file
    
  def set_text_file(self,text_file):
    self.__text_file = text_file
    
  def get_text_file(self):
    return self.__text_file
    
  
  def convert_tesseract(self):
    fo = open(self.__text_file, "w")
    process = subprocess.Popen(['tesseract', self.__image_file, self.__text_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()
    fo.close()
    
  
  def convert_matlab(self):
    fo = open(self.__text_file, "w")
    process = subprocess.Popen(['matlab.py',self.__image_file,self.__text_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()
    fo.close()
    
    #
    #Fill in the code here to send the image file to matlab server
    #and fetch the text and write it to the text file given here
    #
    #


