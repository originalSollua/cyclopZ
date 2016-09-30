# initialization module. 
# call to initialize variable and imports
import serial
import time
from cv2.cv import *
#import picamera
#import picamera.array
class cyclopz:
    def __init__(self):
        self.usb = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            xonxoff=serial.XOFF,
            rtscts=False,
            dsrdtr=False
        )
        self.k_trash_pile = 500
        self.k_yellow_pile = 1000
        self.k_pile_pile = 1500
        self.k_pink_pile = 2000
        self.k_red_pile = 2500

        self.k_default_speed = 500
        self.k_default_shoulder = 1500
        self.k_default_elbow = 1500
        self.k_default_wrist = 1500
        self.k_default_hand = 2500

        try:
            self.usb.open()
        except serial.SerialException:
            self.usb.close()
            self.usb.open()
        else:
            print("error opening usb")

        self.usb.write("#1 P"+str(self.k_default_shoulder)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#2 P"+str(self.k_default_elbow)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#3 P"+str(self.k_default_wrist)+" S"+str(self.k_default_speed)+" \r") 
        self.usb.write("#4 P"+str(self.k_default_hand)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#0 P"+str(self.k_pile_pile)+" S"+str(self.k_default_speed)+" \r")

    def test(self):
        #test rotational base
        self.usb.write("#0 P"+str(self.k_red_pile)+"  S"+str(self.k_default_speed)+" \r")
        time.sleep(6)
        self.usb.write("#0 P"+str(self.k_yellow_pile)+"  S"+str(self.k_default_speed)+" \r")
        time.sleep(6)
        self.usb.write("#0 P"+str(self.k_pink_pile)+"  S"+str(self.k_default_speed)+" \r")
        time.sleep(6)
        self.usb.write("#0 P"+str(self.k_trash_pile)+" S"+str(self.k_default_speed)+" \r")
    def terminate(self):
        self.usb.close()

print("hear we go")
a = cyclopz()
time.sleep(6)
a.test()

