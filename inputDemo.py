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
            edges = cv2.Canny(image,0,100,3)
            cv2.imshow("Image",edges)
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
   global exit = True
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

