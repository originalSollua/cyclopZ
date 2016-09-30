from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

camera=PiCamera()
for x in range(0,100):
 rawCapture=PiRGBArray(camera)

 time.sleep(0.1)

 camera.capture(rawCapture,format="bgr")
 image=rawCapture.array

 edges=cv2.Canny(image,0,100,3)
 cv2.imshow("Image",edges)
 cv2.waitKey(1)
