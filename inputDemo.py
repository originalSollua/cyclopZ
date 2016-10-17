from reader import SixAxis
import time
from keydrive import cyclopzkeys
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
import threading
import sys

class ImageThread(object):
    def __init__(self,interval=1):
	self.interval=interval
	thread = threading.Thread(target=self.run, args=())
	thread.daemon = True
	self.camera = PiCamera()
	thread.start()

    def run(self):
	while True:
            rawCapture=PiRGBArray(self.camera)
	    time.sleep(0.1)
            self.camera.capture(rawCapture,format='bgr')
            image=rawCapture.array
			if variable = 'edge':
				edges = cv2.Canny(image,0,100,3)
				cv2.imshow("Image",edges)
				cv2.waitKey(1)
			elif variable = 'color':
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
				 
				 ave=np.array((int(ave[0]),int(ave[1]),int(ave[2])))

				 min_yellow =np.array([30,110,140],np.uint8)
				 max_yellow =np.array([100,160,190],np.uint8)
				 
				 min_red =np.array([0,0,100],np.uint8)
				 max_red =np.array([100,100,255],np.uint8)

				 min_orange = np.array([5,50,50],np.uint8)
				 max_orange = np.array([15,255,255],np.uint8)

				 min_pink = np.array([50,0,100],np.uint8)
				 max_pink = np.array([90,80,210],np.uint8)

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
					 if colorStr=='No Starburst':
					colorStr='Orange'
					 else:
						colorStr=colorStr+' or Orange'

				 if (min_pink[0] <= ave[0] <= max_pink[0]) and \
					(min_pink[1] <= ave[1] <= max_pink[1]) and \
					(min_pink[2] <= ave[2] <= max_pink[2]):
					# Found yellow starburst
					 if colorStr=='No Starburst':
					colorStr='Pink'
					 else:
						colorStr=colorStr+' or Pink'

				 if (min_red[0] <= ave[0] <= max_red[0]) and \
					(min_red[1] <= ave[1] <= max_red[1]) and \
					(min_red[2] <= ave[2] <= max_red[2]):
					# Found yellow starburst
					 if colorStr=='No Starburst':
					colorStr='Red'
					 else:
						colorStr=colorStr+' or Red'
				 orange=cv2.inRange(hsv,min_orange,max_orange)
				 pink=cv2.inRange(hsv,min_pink,max_pink)
				 red=cv2.inRange(hsv,min_red,max_red)
				 yellow=cv2.inRange(hsv,min_yellow,max_yellow)
				 rgbStr='bgr='+str(ave[0])+' '+str(ave[1])+' '+str(ave[2])
				 scx=root.winfo_screenwidth()/2
				 scy=root.winfo_screenwidth()/2
				 cv2.putText(image,colorStr,(scx+50,scy+10),cv2.FONT_HERSHEY_SIMPLEX,0.5, \
							(0,255,0),2)
				 cv2.putText(image,rgbStr,(scx+50,scy-10),cv2.FONT_HERSHEY_SIMPLEX,0.5, \
							 (0,255,0),2)
				 cv2.circle(image,(scx,scy),30,ave,-11)
				#-----------------------------------------------------------------------#
				 ocntrs=cv2.findContours(orange.copy(),cv2.RETR_EXTERNAL,
										cv2.CHAIN_APPROX_NONE)
				 ocntrs=ocntrs[1]
				 for c in ocntrs:
				  m=cv2.moments(c)
				  if m["m00"] == 0:
					cx = int(m["m10"]/.0001)
					cy = int(m["m10"]/.0001)
				  else:
					cx = int(m["m10"]/m["m00"])
					cy = int(m["m01"]/m["m00"])
				  cv2.drawContours(image,[c],-1,(0,125,255),1)
				#-----------------------------------------------------------------------#
				 pcntrs=cv2.findContours(pink.copy(),cv2.RETR_EXTERNAL,
										cv2.CHAIN_APPROX_NONE)
				 pcntrs=pcntrs[1]
				 for c in pcntrs:
				  m=cv2.moments(c)
				  if m["m00"] == 0:
					cx = int(m["m10"]/.0001)
					cy = int(m["m10"]/.0001)
				  else:
					cx = int(m["m10"]/m["m00"])
					cy = int(m["m01"]/m["m00"])
				  cv2.drawContours(image,[c],-1,(211,178,255),1)
				#-----------------------------------------------------------------------#
				 rcntrs=cv2.findContours(red.copy(),cv2.RETR_EXTERNAL,
										cv2.CHAIN_APPROX_NONE)
				 rcntrs=rcntrs[1]
				 for c in rcntrs:
				  m=cv2.moments(c)
				  if m["m00"] == 0:
					cx = int(m["m10"]/.0001)
					cy = int(m["m10"]/.0001)
				  else:
					cx = int(m["m10"]/m["m00"])
					cy = int(m["m01"]/m["m00"])
				  cv2.drawContours(image,[c],-1,(0,0,255),1)
				#-----------------------------------------------------------------------#
				 ycntrs=cv2.findContours(yellow.copy(),cv2.RETR_EXTERNAL,
										cv2.CHAIN_APPROX_NONE)
				 ycntrs=ycntrs[1]
				 for c in ycntrs:
				  m=cv2.moments(c)
				  if m["m00"] == 0:
					cx = int(m["m10"]/.0001)
					cy = int(m["m10"]/.0001)
				  else:
					cx = int(m["m10"]/m["m00"])
					cy = int(m["m01"]/m["m00"])
				  cv2.drawContours(image,[c],-1,(211,178,255),1)
				#-----------------------------------------------------------------------#
				 cv2.imshow("Image",image)
				 cv2.waitKey(1)

controler = SixAxis(dead_zone = 0.0, hot_zone = 0.00, connect=True)
exit = False
c = cyclopzkeys()
def handler_close(button):
    c.close()
def handler_exit(button):
    quit()
    
def handler_open(button):
    c.open()
def quit():
    global exit
    exit = True
prevx = 0
prevy = 0
controler.register_button_handler(handler_close, SixAxis.button_circle)
controler.register_button_handler(handler_open, SixAxis.button_square)
controler.register_button_handler(handler_exit, SixAxis.button_ps)
viewer = ImageThread()
current_milli_time = lambda: int(round(time.time()*10))
last_time = current_milli_time()

while not exit:
    #controler.handle_event()

    x = controler.axes[0].corrected_value()
    y = controler.axes[1].corrected_value()
    c.inc_base_rotation(10*x)
    c.inc_shoulder_angle(10*y)
    
    x = controler.axes[2].corrected_value()
    y = controler.axes[3].corrected_value()
    c.inc_elbow_angle(10*x)
    c.inc_wrist_angle(10*y)
    now = current_milli_time()
    if now > (last_time + 100):
        last_time = now

