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

        try:
            self.usb.open()
        except serial.SerialException:
            self.usb.close()
            self.usb.open()
        else:
            print("error opening usb")

    def test(self):
        #test rotational base
        self.usb.write("#0 P0500 S500 \r")
        time.sleep(6)
        self.usb.write("#0 P2500 s500 \r")
        time.sleep(6)
        self.usb.write("#4 P2500 S500 \r") 
        time.sleep(6)
        self.usb.write("#4 P500 S500 \r")
        time.sleep(6)

    def terminate(self):
        self.usb.close()

print("hear we go")
a = cyclopz()
a.test()

