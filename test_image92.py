from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import Tkinter

camera=PiCamera()
root=Tkinter.Tk()

for x in range(1,100):
 rawCapture=PiRGBArray(camera)

 time.sleep(0.1)

 camera.capture(rawCapture,format="bgr")
 image=rawCapture.array
 hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
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

 min_yellow = [30,110,140]
 max_yellow = [100,160,190]
 
 min_red = [80,50,120]
 max_red = [130,110,175]

 min_orange = np.array([5,50,50],np.uint8)
 max_orange = np.array([15,255,255],np.uint8)

 min_pink = [170,142,160]
 max_pink = [210,175,175]

 colorStr='No Starburst'

 if (min_yellow[0] <= ave[0] <= max_yellow[0]) and \
    (min_yellow[1] <= ave[1] <= max_yellow[1]) and \
    (min_yellow[2] <= ave[2] <= max_yellow[2]):
	# Found yellow starburst
 	colorStr='Yellow'

 if (min_orange[0] <= ave[0] <= max_orange[0]) and \
    (min_orange[1] <= ave[1] <= max_orange[1]) and \
    (min_orange[2] <= ave[2] <= max_orange[2]):
	# Found yellow starburst
	colorStr='Orange'

 if (min_red[0] <= ave[0] <= max_red[0]) and \
    (min_red[1] <= ave[1] <= max_red[1]) and \
    (min_red[2] <= ave[2] <= max_red[2]):
	# Found yellow starburst
	colorStr='Red'

 if (min_pink[0] <= ave[0] <= max_pink[0]) and \
    (min_pink[1] <= ave[1] <= max_pink[1]) and \
    (min_pink[2] <= ave[2] <= max_pink[2]):
	# Found yellow starburst
	colorStr='Pink'
 print(image.shape)
 orange=cv2.inRange(hsv,min_orange,max_orange)
 rgbStr='bgr='+str(ave[0])+' '+str(ave[1])+' '+str(ave[2])
 scx=root.winfo_screenwidth()/2
 scy=root.winfo_screenwidth()/2
 cv2.putText(image,colorStr,(scx+50,scy+10),cv2.FONT_HERSHEY_SIMPLEX,0.5, \
            (0,255,0),2)
 cv2.putText(image,rgbStr,(scx+50,scy-10),cv2.FONT_HERSHEY_SIMPLEX,0.5, \
             (0,255,0),2)
 cv2.circle(image,(scx,scy),30,ave,-11)
 cntrs=cv2.findContours(orange.copy(),cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_NONE)
 cntrs=cntrs[1]
 for c in cntrs:
  m=cv2.moments(c)
  if m["m00"] == 0:
    cx = int(m["m10"]/.0001)
    cy = int(m["m10"]/.0001)
  else:
    cx = int(m["m10"]/m["m00"])
    cy = int(m["m01"]/m["m00"])
  cv2.drawContours(image,[c],-1,(0,255,0),1)
 cv2.imshow("Image",image)
 cv2.waitKey(1)

