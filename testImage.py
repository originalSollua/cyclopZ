"""
Import these things in mainline:

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
"""

def testImage():
 camera=PiCamera()
 rawCapture=PiRGBArray(camera)

 time.sleep(0.1)

 camera.capture(rawCapture,format="bgr")
 image=rawCapture.array
 dim1=image.shape[0]
 dim2=image.shape[1]
 bd1=dim1/4
 bd2=(dim1/2)+bd1
 bd3=dim2/4
 bd4=(dim2/2)+bd3
 md1=dim1/2
 md2=dim2/2
 averange=image[bd1:bd2,bd3:bd4]
 ave=np.average(averange,axis=0)
 ave=np.average(ave,axis=0)
 ave=np.uint8(ave)
 print(ave)

 ave=np.array((int(ave[0]),int(ave[1]),int(ave[2])))
 cv2.circle(image,(md1,md2),30,ave,-11)
 cv2.imshow("Image",image)
 cv2.waitKey(0)
 
 min_yellow = [30,110,140]
 max_yellow = [100,160,190]
 
 min_red = [80,50,120]
 max_red = [130,110,175]

 min_orange = [80,80,150]
 max_orange = [90,90,160]

 min_pink = [170,142,160]
 max_pink = [210,175,175]
 out='Invalid'
 if (min_yellow[0] <= ave[0] <= max_yellow[0]) and \
    (min_yellow[1] <= ave[1] <= max_yellow[1]) and \
    (min_yellow[2] <= ave[2] <= max_yellow[2]):
	# Found yellow starburst
 	out='Yellow'
 
 if (min_orange[0] <= ave[0] <= max_orange[0]) and \
    (min_orange[1] <= ave[1] <= max_orange[1]) and \
    (min_orange[2] <= ave[2] <= max_orange[2]):
	# Found yellow starburst
        out='Orange'

 if (min_red[0] <= ave[0] <= max_red[0]) and \
    (min_red[1] <= ave[1] <= max_red[1]) and \
    (min_red[2] <= ave[2] <= max_red[2]):
	# Found yellow starburst
        out='Red'

 if (min_pink[0] <= ave[0] <= max_pink[0]) and \
    (min_pink[1] <= ave[1] <= max_pink[1]) and \
    (min_pink[2] <= ave[2] <= max_pink[2]):
	# Found yellow starburst
	out='Pink'
 return out
