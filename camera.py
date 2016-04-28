#!/usr/bin/python
import picamera

def capture_image():
  with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(5)
    camera.capture('/home/pi/image.jpg')
    camera.stop_preview()
