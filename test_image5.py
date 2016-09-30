from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

camera=PiCamera()
rawCapture=PiRGBArray(camera)

time.sleep(0.1)

camera.capture(rawCapture,format="bgr")
image=rawCapture.array

gsimage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gsimage,(51,51),30)
thresh=cv2.threshold(blurred,125,200,cv2.THRESH_BINARY)[1]
edge=cv2.Canny(thresh,0,10,3)
ret, labels, stats, centroids=cv2.connectedComponentsWithStats(edge)

for x in centroids:
 cv2.circle(image,(int(x[0]),int(x[1])),10,(0,0,0),-11)
print(centroids)
cv2.imshow("Image",image)
cv2.waitKey(0)
