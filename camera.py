#!/usr/bin/python
import picamera

class Cam:
  def __init__(self, image_file):
    self.__image_file = image_file
    
  def capture_image(self):
    with picamera.PiCamera() as camera:
      camera.start_preview()
      time.sleep(5)
      camera.capture(self.__image_file)
      camera.stop_preview()
